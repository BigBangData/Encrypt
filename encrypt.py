import os
import subprocess
import sys
import shutil

def bundle_folder(folder_path):
    """
    Bundle a folder into a tar.gz archive.

    Args:
        folder_path (str): Path to the folder to be bundled.
        output_path (str): Path to save the resulting archive.
    """
    shutil.make_archive(folder_path, 'gztar', folder_path)

def encrypt_file(input_file, output_file, password):
    """
    Encrypt a file using OpenSSL.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to save the encrypted file.
        password (str): Password for encryption.
    """
    command = [
        'openssl', 'enc',
        '-aes-256-cbc', '-salt', '-pbkdf2',
        '-in', input_file,
        '-out', output_file,
        '-pass', 'pass:' + password
    ]
    subprocess.run(command, check=True)

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <folder_name> <password>")
        sys.exit(1)

    folder_path = sys.argv[1]
    password = sys.argv[2]

    # Encryption
    bundle_folder(folder_path)
    shutil.rmtree(folder_path)
    encrypt_file(folder_path + ".tar.gz", folder_path + ".enc", password)
    os.remove(folder_path + ".tar.gz")

if __name__ == "__main__":
    main()
