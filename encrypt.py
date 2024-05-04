import os
import subprocess
import sys
import shutil
import getpass

def bundle_folder(dir):
    """Bundle a folder into a tar.gz archive."""

    shutil.make_archive(dir, 'gztar', dir)

def encrypt(input_file, output_file):
    """Encrypt a file or bundled folder using OpenSSL."""

    key = getpass.getpass("Please enter encryption key: ")

    if not key:
        print("Key cannot be blank or just spaces.")
        sys.exit(1)

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
