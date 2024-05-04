import os
import subprocess
import sys
import shutil
import getpass

def get_key():
    """Get key securely from user and avoid errors."""

    err_msg = "Password cannot be blank or just spaces."

    key_1 = getpass.getpass("Enter password: ").strip()
    if not key_1:
        print(err_msg)
        sys.exit(1)

    key_2 = getpass.getpass("Confirm password: ").strip()
    if not key_2:
        print(err_msg)
        sys.exit(1)
    elif key_2 != key_1:
        print("Passwords do not match.")
        sys.exit(1)

    return key_1

def encrypt(input_file, output_file, dir):
    """Encrypt a file or bundled folder using OpenSSL."""

    key = get_key()

    # bundle the folder
    shutil.make_archive(dir, 'gztar', dir)

    command = [
        'openssl', 'enc',
        '-aes-256-cbc', '-salt', '-pbkdf2',
        '-in', input_file,
        '-out', output_file,
        '-pass', 'pass:' + key
    ]
    subprocess.run(command, check=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: python encrypt.py <folder/>")
        sys.exit(1)

    dir = sys.argv[1]
    dir = dir.replace("/", "")

    if not os.path.exists(dir):
        print(f"Folder {dir} not found.")
        sys.exit(1)

    unencrypted_bundle = ''.join([dir, ".tar.gz"])
    encrypted_bundle = ''.join([dir, ".enc"])

    # encrypt
    encrypt(unencrypted_bundle, encrypted_bundle, dir)

    # cleanup
    shutil.rmtree(dir)
    os.remove(unencrypted_bundle)


if __name__ == "__main__":
    main()
