"""
Author: Kelvin Gooding
Created: 2022-06-13
Updated: 2023-12-08
Version: 1.6.1
"""

# Modules

from datetime import datetime
from modules import exec_timer
import os
import shutil

# Variables

user = os.getlogin()
timestamp = datetime.today().strftime("%H:%M:%S")

# Script

hdd_drive = input('Input HDD drive letter: ')
input("Press any enter to confirm and start backup .. ")

def file_bkup(bkup_source, bkup_destination):

    try:

        if os.path.isdir(bkup_destination):
            print(f'\nExisting Directory Found! Deleting {bkup_destination} ..')
            os.system(f'rmdir /S /Q "{bkup_destination}"')

            print(f'{datetime.today().strftime("%H:%M:%S")} - Copying {bkup_source} to {bkup_destination}')
            shutil.copytree(bkup_source, bkup_destination)

            print(f'{datetime.today().strftime("%H:%M:%S")} - Complete!')
        else:
            print(f'\n{datetime.today().strftime("%H:%M:%S")} - Copying {bkup_source} to {bkup_destination}')
            shutil.copytree(bkup_source, bkup_destination)
            print(f'{datetime.today().strftime("%H:%M:%S")} - Complete!')

    except FileNotFoundError:
        print('Directory does not exist. Passing')
        pass

    except:
        pass

exec_timer.start_timer()

# Add the function here - including the backup source and destination paths.

exec_timer.stop_timer()