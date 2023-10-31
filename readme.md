# File Encryption and Decryption with Python

This Python script demonstrates file encryption and decryption using the Fernet symmetric encryption algorithm provided by the cryptography library.

## Installation

You need to install the `cryptography` library to use this script:

```bash
pip install cryptography
Usage
1. Generating a Key
Before encrypting or decrypting files, you need to generate a key. You can generate it using the script as follows:

python
key = generate_key()
save_key(key, 'secret.key')
This generates a random encryption key and saves it to a file (e.g., 'secret.key').

2. Encrypting a File
To encrypt a file, use the encrypt_file function:

python
encrypt_file(key, 'plaintext.txt', 'encrypted.txt')
This will take the 'plaintext.txt' file and encrypt its contents, saving the encrypted data in 'encrypted.txt'.

3. Decrypting a File
To decrypt a file, use the decrypt_file function:

python
decrypt_file(key, 'encrypted.txt', 'decrypted.txt')
This will decrypt the 'encrypted.txt' file and save the decrypted data in 'decrypted.txt'.

Please make sure to handle your encryption key securely and avoid losing it, as it is required for decryption.

Security Note
This script is provided for educational purposes. In a production environment, you should ensure proper key management, error handling, and secure file handling. Be cautious when working with sensitive data and encryption.

License
This project is open source and available under the MIT License. Feel free to use, modify, and share it.

Acknowledgments
The cryptography library for providing encryption capabilities in Python.
vbnet