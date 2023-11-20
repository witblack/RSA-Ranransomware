"""     libs        """
# External
from time import sleep
from datetime import datetime

# Configs
from configs.encryptor import start_hour, end_hour, check_hour_interval

"""     get time        """
def wait_for_run_time():
    while True:
        # Check & Block time
        if datetime.now().hour in range(start_hour, end_hour + 1):
            break
        # Sleep for next time
        sleep(check_hour_interval)
