# Encrypt

Couple python scripts to encrypt a folder.

The scripts make it easier to do so than using the command line:

_encryption_

```bash
# Bundle folder
$ tar -czf bundle.tar.gz folder_name

# Delete folder
$ rm -r folder_name

# Encrypt bundle
$ openssl enc -aes-256-cbc -salt -pbkdf2 -in bundle.tar.gz -out folder_name.enc

# Delete unencrypted bundle
$ rm bundle.tar.gz
```

_decryption_
```bash
# Decrypt bundle:
$ openssl enc -aes-256-cbc -d -pbkdf2 -in dirname.enc -out bundle.tar.gz

# Delete encrypted bundle
$ rm dirname.enc

# Extract items
$ tar -xzf bundle.tar.gz

# Delete bundle
$ rm bundle.tar.gz
```

__Password Handling__


- user enters password interactively during runtime rather than as arguments, which would be vulnerable to various recall methos (shell history, memory dumps, ...)
- system prompts user for password twice to avoid user error, ensuring user knows and remembers the password before encryption