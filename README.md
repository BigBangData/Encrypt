# Encrypt

Couple python scripts to encrypt a folder.

## How

Issue the following commands to encrypt and decrypt:

```python
# to encrypt a folder
$ python encrypt.py <folder_name/>
# provide encryption key at runtime

# to decrypt an encrypted folder
$ python decrypt.py <encrypted_folder_name.enc>
# provide the same key
```

## Example

After cloning repo, issue the following to decrypt:

```python
$ python decrypt.py Encrypt.enc
# key: inception
```

## Why

The scripts are more user friendly than:

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

## Todo

- Use https://github.com/FiloSottile/age?

---