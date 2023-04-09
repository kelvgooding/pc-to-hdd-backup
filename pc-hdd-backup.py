"""
Author: Kelvin Gooding
Created: 2022-06-13
Updated: 2023-04-09
Version: 1.3
"""

# Modules

import shutil
from datetime import datetime
import os
import time

# Variables
2
user = os.getlogin()
timestamp = datetime.today().strftime("%H:%M:%S")

# Script

input("Press any key to start ..")

# Write to log file with Backup Start Time

def file_bkup(bkup_source, bkup_destination):
    start_time = time.time()

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

    except:
        pass

    finish_time = time.time() - start_time

    print(f'Section Complete! Duration: {round(finish_time, 2)}')

start_time = time.time()

# Documents
file_bkup(fr'C:\Users\{user}\OneDrive', fr'D:\Documents')

# Pictures
file_bkup(fr'C:\Users\{user}\Pictures', fr'D:\Pictures')

# Software
file_bkup(fr'C:\Users\{user}\Desktop\source\music', fr'D:\Software')

# Music
file_bkup(fr'C:\Users\{user}\Music', fr'D:\Music')

# Videos
file_bkup(fr'C:\Users\{user}\Videos', fr'D:\Videos')

finish_time = time.time() - start_time

print('\n---------------')
print(f'Full Backup Complete! Duration: {round(finish_time, 2)}')
print()
input("Press any key to exit ..")
