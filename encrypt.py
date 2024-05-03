import os
import subprocess
import sys
import shutil

def bundle_folder(dir):
    """
    Bundle a folder into a tar.gz archive.
    """
    shutil.make_archive(dir, 'gztar', dir)

def encrypt(input, output, pswd):
    """
    Encrypt a file or bundled folder using OpenSSL.
    """
    command = [
        'openssl', 'enc',
        '-aes-256-cbc', '-salt', '-pbkdf2',
        '-in', input,
        '-out', output,
        '-pass', 'pass:' + pswd
    ]
    subprocess.run(command, check=True)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <folder_name> <password>")
        sys.exit(1)

    dir = sys.argv[1]
    pswd = sys.argv[2]

    if not os.path.exists(dir):
        print(f"Folder {dir} not found.")
        sys.exit(1)

    unencrypted_bundle = ''.join([dir, ".tar.gz"])
    encrypted_bundle = ''.join([dir, ".enc"])

    # bundle folder
    bundle_folder(dir)

    # encrypt
    encrypt(unencrypted_bundle, encrypted_bundle, pswd)

    # cleanup
    shutil.rmtree(dir)
    os.remove(unencrypted_bundle)


if __name__ == "__main__":
    main()
