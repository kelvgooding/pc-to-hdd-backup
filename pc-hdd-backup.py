# Modules

import shutil
import datetime
import os

# Variables

user = os.getlogin()

# Source

pc_documents = fr"C:\Users\{user}\Dropbox"
pc_pictures = r"D:\Pictures"
pc_music = r"D:\Music"
pc_videos = r"D:\Videos"
pc_software = r"D:\Software"

# Destination

hdd_documents = r"E:\Documents"
hdd_pictures = r"E:\Pictures"
hdd_music = r"E:\Music"
hdd_videos = r"E:\Videos"
hdd_software = r"E:\Software"

# Copy from PC to HDD

input("Press any key to start PC to HDD backup ..")
print("\n{} - Backup Started!".format(datetime.datetime.today().strftime("%H:%M:%S")))

try:

    # Documents

    try:

        if os.path.isdir(hdd_documents):
            print("\nExisting Directory Found! Deleting {} ..".format(hdd_documents))
            os.system('rmdir /S /Q "{}"'.format(hdd_documents))
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_documents, hdd_documents))
            shutil.copytree(pc_documents, hdd_documents)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))
        else:
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_documents, hdd_documents))
            shutil.copytree(pc_documents, hdd_documents)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))

    except FileExistsError:
        print("Folder already exists: '{}'".format(hdd_documents))

    except PermissionError:
        print("Access is denied: '{}'".format(hdd_documents))

    # Pictures

    try:

        if os.path.isdir(hdd_pictures):
            print("\nDirectory Found! Deleting {} ..".format(hdd_pictures))
            os.system('rmdir /S /Q "{}"'.format(hdd_pictures))
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_pictures, hdd_pictures))
            shutil.copytree(pc_pictures, hdd_pictures)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))
        else:
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_pictures, hdd_pictures))
            shutil.copytree(pc_pictures, hdd_pictures)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))

    except FileExistsError:
        print("Folder already exists: '{}'".format(hdd_pictures))

    except PermissionError:
        print("Access is denied: '{}'".format(hdd_pictures))

    # Music

    try:

        if os.path.isdir(hdd_music):
            print("\nDirectory Found! Deleting {} ..".format(hdd_music))
            os.system('rmdir /S /Q "{}"'.format(hdd_music))
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_music, hdd_music))
            shutil.copytree(pc_music, hdd_music)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))
        else:
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_music, hdd_music))
            shutil.copytree(pc_music, hdd_music)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))

    except FileExistsError:
        print("Access is denied: '{}'".format(hdd_music))

    except PermissionError:
        print("Access is denied: '{}'".format(hdd_music))

    # Videos

    try:

        if os.path.isdir(hdd_videos):
            print("\nDirectory Found! Deleting {} ..".format(hdd_videos))
            os.system('rmdir /S /Q "{}"'.format(hdd_videos))
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_videos, hdd_videos))
            shutil.copytree(pc_videos, hdd_videos)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))
        else:
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_videos, hdd_videos))
            shutil.copytree(pc_videos, hdd_videos)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))

    except FileExistsError:
        print("Access is denied: '{}'".format(hdd_videos))

    except PermissionError:
        print("Access is denied: '{}'".format(hdd_videos))

    # Software

    try:

        if os.path.isdir(hdd_software):
            print("\nDirectory Found! Deleting {} ..".format(hdd_software))
            os.system('rmdir /S /Q "{}"'.format(hdd_software))
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_software, hdd_software))
            shutil.copytree(pc_software, hdd_software)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))
        else:
            print("{} - Copying {} to {}".format(datetime.datetime.today().strftime("%H:%M:%S"), pc_software, hdd_software))
            shutil.copytree(pc_software, hdd_software)
            print("{} - Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))

    except FileExistsError:
        print("Access is denied: '{}'".format(hdd_software))

    except PermissionError:
        print("Access is denied: '{}'".format(hdd_software))

    # Backup Log File

    log = open(r"E:\readme.txt", "a")
    log.write("\n{} - Backup Complete".format(datetime.datetime.today().strftime("%d/%m/%Y")))
    log.close()

except FileNotFoundError:
    print("\nBackup Drive is not connected. Please check connection and try again..")

print("\n{} - Backup Complete!".format(datetime.datetime.today().strftime("%H:%M:%S")))
input("\nPress any key to exit ..")
