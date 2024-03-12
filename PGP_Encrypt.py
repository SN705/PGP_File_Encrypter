"""
PGP Encryption Script:

This script encrypts files located in a specified unencrypted directory using the Pretty Good Privacy (PGP) encryption method.
It utilizes the GnuPG library to perform encryption, with the recipient identified by their email address associated with the public key.
The script iterates through each file in the unencrypted directory, encrypts the file content, and saves the encrypted data in a separate directory.
Error handling ensures proper file overwrites, and the script concludes by displaying the encryption status.

By: Simon Nadeau
Date: 30 NOV 2023
"""

# Download and install Gpg4win version 4.2.0 (Kleopatra)
# Install the gnupg module in Python on Windows using the Command Prompt (pip install gnupg)

import os
import gnupg

# Variables
unencrypted_dir = r"C:\Users\simon\OneDrive - Das Computer Network Consulting Ltd\Desktop\PGP Automation (BBC)\Unencrypted"
encrypted_dir = r"C:\Users\simon\OneDrive - Das Computer Network Consulting Ltd\Desktop\PGP Automation (BBC)\Encrypted"
key_ID = "administrator@brewsters.ca"     #email address associated with the public key of the recipient

print("In progress...")

# Initialize the gnupg.GPG object
gpg = gnupg.GPG()

# Iterate over each file in the unencrypted directory
for file in os.listdir(unencrypted_dir):
    # Get the full path of the file
    file_path = os.path.join(unencrypted_dir, file)

    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file data
        file_data = f.read()

        # Encrypt the file data
        encrypted_data = gpg.encrypt(file_data, key_ID, always_trust=True)

        # Get the full path for the encrypted file
        encrypted_file_path = os.path.join(encrypted_dir, f"{file}.pgp")

        # ERROR HANDLING - If the file already exists, have it overwritten
        if os.path.exists(encrypted_file_path):
            os.remove(encrypted_file_path)

        # Write the encrypted data to the file
        with open(encrypted_file_path, 'wb') as ef:
            ef.write(str(encrypted_data).encode())

# Verify encryption is successful
if encrypted_data.ok:
    print("Encryption successful.")
else:
    print("Encryption failed.")
    print(encrypted_data.stderr)

print("Encryption to PGP complete.")
