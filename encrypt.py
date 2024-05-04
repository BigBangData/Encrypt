import os
import subprocess
import sys
import shutil
import getpass

def bundle_folder(dir):
    """Bundle a folder into a tar.gz archive."""

    shutil.make_archive(dir, 'gztar', dir)

def get_key():
    """Get key securely from user and avoid errors."""

    key_1 = getpass.getpass("Enter password: ").strip()
    if not key_1:
        print("Key cannot be blank or just spaces.")
        sys.exit(1)

    key_2 = getpass.getpass("Confirm password: ").strip()
    if not key_2:
        print("Key cannot be blank or just spaces.")
        sys.exit(1)
    elif key_2 != key_1:
        print("Passwords do not match.")
        sys.exit(1)

    return key_1

def encrypt(input_file, output_file):
    """Encrypt a file or bundled folder using OpenSSL."""

    key = get_key()

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

    # bundle folder
    bundle_folder(dir)

    # encrypt
    encrypt(unencrypted_bundle, encrypted_bundle)

    # cleanup
    shutil.rmtree(dir)
    os.remove(unencrypted_bundle)


if __name__ == "__main__":
    main()
