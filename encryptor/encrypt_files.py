"""      libs       """
# Internal
from encryptor.RSA import RSA_encryptor_class

"""     Encrypt files       """
class encrypt_files:
    def __init__(self, public_key):
        # Generate class
        self.RSA_encryptor = RSA_encryptor_class()
        # Set public key
        self.RSA_encryptor.public_key = public_key
        self.RSA_encryptor.private_key = None

    def encrypt(self, filename):
        # Read files
        file = open(filename, 'rb')
        file_content = file.read()
        file.close()
        # Encrypt
        encrypted_content = self.RSA_encryptor.encryptor(file_content)
        # Write to file
        file = open(filename, 'wb')
        file.write(encrypted_content)
        file.close()
