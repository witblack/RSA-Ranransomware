"""     libs        """
# Internal

# Configs
from configs.encryptor import readme_message, message_file

"""     Creaste file    """
def done():
    file = open(message_file, 'w')
    file.write(readme_message)
    file.close()
