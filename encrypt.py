import base64
from cryptography.fernet import Fernet

# Generate a new encryption key
key = Fernet.generate_key()

# Create a Fernet object using the key
fernet = Fernet(key)

# Get the path of the input file from the user
input_file = input("Enter the path of the input file: ")

# Open the input file and read its contents
with open(input_file, 'r') as f:
    plaintext = f.read().encode('utf-8')

# Encrypt the plaintext using the Fernet object
ciphertext = fernet.encrypt(plaintext)

# Convert the encrypted text to binary using base64 encoding
binary = base64.b64encode(ciphertext)

# Write the binary data to a new file in the current directory
with open('output.bin', 'wb') as f:
    f.write(binary)
    
# Print the encryption key for the user to save
print(f"Encryption key: {key}")
