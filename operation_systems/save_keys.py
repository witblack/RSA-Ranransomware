"""     libs        """
# Internal
from encryptor.RSA import RSA_encryptor_class

# External
from rsa import PublicKey

# Configs
from configs.encryptor import main_public_key_P1, main_public_key_P2, save_key_file

"""     Internal """
def save_keys(privatekey):
    RSA_encryptor = RSA_encryptor_class()

    # Load main public key
    RSA_encryptor.public_key = PublicKey(main_public_key_P1, main_public_key_P2)
    RSA_encryptor.private_key = None

    # Encrypt private key with main key
    data_code = RSA_encryptor.encryptor(privatekey)

    # Write to file
    file = open(save_key_file, 'wb')
    file.write(data_code)
    file.close()
