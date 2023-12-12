# PC TO HDD BACKUP

## Description

Repository: https://github.com/kelvgooding/pc-to-hdd-backup

This script is used to back up files from PC to a External HDD. This is achieved by copying the files from each location listed on the PC, over to the external HDD.

- Documents
- Pictures
- Music
- Videos
- Software

Once this process starts, this will go in order of the script, and will move onto the next folder once the previous one is complete.

## OS Compatibility

- Linux
- Windows

## Dependencies

### Linux Packages

- python3
- python3-pip

### Python Modules

- from datetime import datetime
- from modules import exec_timer
- import os
- import shutil


## Installation

To download this web application, run the following commands on your linux environment:

Downloading the repository from GitHub:

```
cd ~
git clone https://github.com/kelvgooding/pc-to-hdd-backup.git
```

Installating the requirements.txt file to ensure the correct packages are available and installed:

```
cd ~/pc-to-hdd-backup
pip3 install -r requirements.txt
```

Running the application:

```
cd ~/pc-to-hdd-backup
python3 pc-to-hdd-backup.py
```

## Stakeholders

PM: Kelvin Gooding | kelv.gooding@outlook.com<br>
Design: Kelvin Gooding | kelv.gooding@outlook.com<br>
Dev: Kelvin Gooding | kelv.gooding@outlook.com<br>
QA: Kelvin Gooding | kelv.gooding@outlook.com<br>
Support: Kelvin Gooding | kelv.gooding@outlook.com

## Contribution
Issue Tracker: https://github.com/kelvgooding/pc-to-hdd-backup/issues<br>
Contact: Kelvin Gooding | kelv.gooding@outlook.com
