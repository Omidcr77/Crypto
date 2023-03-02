import base64
from cryptography.fernet import Fernet

# Get the path of the input file from the user
input_file = input("Enter the path of the input file: ")

# Read the binary data from the input file
with open(input_file, 'rb') as f:
    binary = f.read()

# Decode the binary data from base64
ciphertext = base64.b64decode(binary)

# Get the encryption key from the user
key = input("Enter the encryption key: ").encode('utf-8')

# Create a Fernet object using the encryption key
fernet = Fernet(key)

# Decrypt the ciphertext using the Fernet object
plaintext = fernet.decrypt(ciphertext).decode('utf-8')

# Write the plaintext to a new file in the current directory
with open('output.txt', 'w') as f:
    f.write(plaintext)
