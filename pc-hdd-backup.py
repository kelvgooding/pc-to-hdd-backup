"""
Author: Kelvin Gooding
Created: 2022-06-13
Updated: 2023-03-27
Version: 1.2
"""

# Modules

import shutil
from datetime import datetime
import os
import time

# Variables

user = os.getlogin()
timestamp = datetime.today().strftime("%H:%M:%S")

# Script

input("Press any key to start ..")


# Write to log file with Backup Start Time

def file_bkup(bkup_source, bkup_destination):
    start_time = time.time()

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

    finish_time = time.time() - start_time

    print(f'Section Complete! Duration: {round(finish_time, 2)}')

    time.sleep(20)

# Documents

file_bkup(fr'C:\Users\{user}\Desktop\source\pictures', fr'C:\Users\{user}\Desktop\destination\pictures')

# Pictures

file_bkup(fr'C:\Users\{user}\Desktop\source\docs', fr'C:\Users\{user}\Desktop\destination\docs')

# Software

file_bkup(fr'C:\Users\{user}\Desktop\source\music', fr'C:\Users\{user}\Desktop\destination\music')

# Music

file_bkup(fr'C:\Users\{user}\Desktop\source\software', fr'C:\Users\{user}\Desktop\destination\software')

# Videos

file_bkup(fr'C:\Users\{user}\Desktop\source\videos', fr'C:\Users\{user}\Desktop\destination\videos')

start_time = time.time()
finish_time = time.time() - start_time
print('\n---------------')
print(f'Full Backup Complete! Duration: {round(finish_time, 2)}')
print()
input("Press any key to exit ..")
