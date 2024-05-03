
Encryption
----------
Bundle folder:
    tar -czf bundle.tar.gz dirname

Delete original:
    rm -r dirname

Encrypt bundle:
    openssl enc -aes-256-cbc -salt -pbkdf2 -in bundle.tar.gz -out dirname.enc

Delete unencrypted bundle:
    rm bundle.tar.gz


Decryption
----------

Decrypt bundle:
    openssl enc -aes-256-cbc -d -pbkdf2 -in dirname.enc -out bundle.tar.gz

Delete encrypted bundle:
    rm dirname.enc

Extract:
    tar -xzf bundle.tar.gz

Delete bundle:
    rm bundle.tar.gz