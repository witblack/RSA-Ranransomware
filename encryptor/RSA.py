"""     libs        """
# Internal
from rsa import decrypt, encrypt, newkeys

# Configs
from configs.encryptor import RSA_key_bit_size


"""     RSA class     """
class RSA_encryptor_class:
    # Init RSA
    def __init__(self):
        public_key = None
        private_key = None
        self.new_key(RSA_key_bit_size)

    # Generate new key
    def new_key(self, key_bit_size: int = RSA_key_bit_size):
        self.public_key, self.private_key = newkeys(key_bit_size)
        return [self.public_key, self.private_key]

    # Encrypt with
    def encryptor(self, data: bytes):
        return encrypt(data, self.public_key)

    def decryptor(self, encoded_data: bytes):
        return decrypt(encoded_data, self.private_key)
