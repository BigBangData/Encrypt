import os
import subprocess
import sys
import shutil
from encrypt import get_key

def decrypt(input_file, output_file):
    """Decrypt a file or bundled folder using OpenSSL."""

    key =  get_key()

    if not key:
        print("Key cannot be blank or just spaces.")
        sys.exit(1)

    command = [
        'openssl', 'enc',
        '-aes-256-cbc', '-d', '-pbkdf2',
        '-in', input_file,
        '-out', output_file,
        '-pass', 'pass:' + key
    ]

    try:
        subprocess.run(
            command, check=True, 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
    except subprocess.CalledProcessError as e:
        print("Decryption key failed:", e.stderr.decode().strip())
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encrypted_file.enc>")
        sys.exit(1)

    user_input = sys.argv[1]
    dir, ext = os.path.splitext(user_input)

    if not ext == '.enc':
        print("Please provide the encrypted file's extension.")
        print("Usage: python decrypt.py <encrypted_file.enc>")
        sys.exit(1)

    encrypted_bundle = ''.join([user_input])
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
