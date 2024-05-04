# Encrypt

Couple python scripts to encrypt a folder.

## How

Issue the following commands to encrypt and decrypt:
- tab-complete as necessary (recommended)
- spaces in folder name are okay
- ending in / or not

```python
# to encrypt a folder
$ python encrypt.py <folder_name/>
# provide encryption key (password)

# to decrypt an encrypted folder
$ python decrypt.py <encrypted_folder_name.enc>
# provide the same key
```

## Try

After cloning repo, issue the following to decrypt:

```python
$ python decrypt.py Birdcall\ Timer.enc
```

Enter password: `bird`

(or yes, just revert to a previous commit... pro tip: don't keep version history!)


## Why

The scripts make it easier to do so than using the command line, which entails the following:

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

## SecOps

- user enters password interactively during runtime rather than, say, as an argument in the command line, which is vulnerable to recall via hell history, memory dump, etc.
- system prompts user for password twice to avoid user error
---