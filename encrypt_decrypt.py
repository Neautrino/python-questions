from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_file(key, input_file, output_file):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as f:
        file_data = f.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

def decrypt_file(key, input_file, output_file):
    cipher_suite = Fernet(key)
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Example usage:
# Generate and save a key
key = generate_key()
save_key(key, 'secret.key')

# Encrypt a file
encrypt_file(key, 'plaintext.txt', 'encrypted.txt')

# Decrypt the file
decrypt_file(key, 'encrypted.txt', 'decrypted.txt')
