import os
import subprocess
import sys
import shutil

def decrypt(input_file, output_file):
    """
    Decrypt a file or bundled folder using OpenSSL.
    """
    K_ = input("Please enter encryption key: ")
    command = [
        'openssl', 'enc',
        '-aes-256-cbc', '-d', '-pbkdf2',
        '-in', input_file,
        '-out', output_file,
        '-pass', 'pass:' + K_
    ]
    subprocess.run(command, check=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <folder_name>")
        sys.exit(1)

    dir = sys.argv[1]

    encrypted_bundle = ''.join([dir, ".enc"])
    decrypted_bundle = ''.join([dir, ".tar.gz"])

    if not os.path.exists(encrypted_bundle):
        print(f"Encrypted file {encrypted_bundle} not found.")
        sys.exit(1)

    # decrypt
    decrypt(encrypted_bundle, decrypted_bundle)

    # extract
    shutil.unpack_archive(decrypted_bundle, dir)

    # cleanup
    os.remove(encrypted_bundle)
    os.remove(decrypted_bundle)


if __name__ == "__main__":
    main()
