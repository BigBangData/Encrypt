import os
import subprocess
import sys
import shutil

def decrypt(input, output, pswd):
    """
    Decrypt a file or bundled folder using OpenSSL.
    """
    command = [
        'openssl', 'enc',
        '-aes-256-cbc', '-d', '-pbkdf2',
        '-in', input,
        '-out', output,
        '-pass', 'pass:' + pswd
    ]
    subprocess.run(command, check=True)

def main():
    if len(sys.argv) != 3:
        print("Usage: python decrypt.py <folder_name> <password>")
        sys.exit(1)

    dir = sys.argv[1]
    pswd = sys.argv[2]

    encrypted_bundle = ''.join([dir, ".enc"])
    decrypted_bundle = ''.join([dir, ".tar.gz"])

    if not os.path.exists(encrypted_bundle):
        print(f"Encrypted file {encrypted_bundle} not found.")
        sys.exit(1)

    # decrypt
    decrypt(encrypted_bundle, decrypted_bundle, pswd)

    # extract
    shutil.unpack_archive(decrypted_bundle, dir)

    # cleanup
    os.remove(encrypted_bundle)
    os.remove(decrypted_bundle)


if __name__ == "__main__":
    main()
