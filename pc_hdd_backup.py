"""
Author: Kelvin Gooding
Created: 2022-06-13
Updated: 2023-12-02
Version: 1.6
"""

# Modules

import shutil
from datetime import datetime
import os
from modules import exec_timer

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

file_bkup(fr'C:\Users\{user}\OneDrive', fr'{hdd_drive}:\Documents')
file_bkup(fr'D:\Pictures', fr'{hdd_drive}:\Pictures')
file_bkup(fr'D:\Software', fr'{hdd_drive}:\Software')
file_bkup(fr'D:\Music', fr'{hdd_drive}:\Music')
file_bkup(fr'D:\Videos', fr'{hdd_drive}:\Videos')

exec_timer.stop_timer()