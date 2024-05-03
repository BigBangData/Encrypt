import os
import subprocess
import sys
import shutil

def decrypt_file(input_file, output_file, password):
    """
    Decrypt a file using OpenSSL.

    Args:
        input_file (str): Path to the input encrypted file.
        output_file (str): Path to save the decrypted file.
        password (str): Password for decryption.
    """
    command = [
        'openssl', 'enc',
        '-aes-256-cbc', '-d', '-pbkdf2',
        '-in', input_file,
        '-out', output_file,
        '-pass', 'pass:' + password
    ]
    subprocess.run(command, check=True)

def main():
    if len(sys.argv) != 4:
        print("Usage: python decrypt.py <folder_name> <password>")
        sys.exit(1)

    folder_name = sys.argv[1]
    password = sys.argv[2]

    # Decryption
    decrypt_file(folder_name + ".enc", folder_name + ".tar.gz", password)
    os.remove(folder_name + ".enc")
    shutil.unpack_archive(folder_name + ".tar.gz", folder_name)
    os.remove(folder_name + ".tar.gz")

if __name__ == "__main__":
    main()
