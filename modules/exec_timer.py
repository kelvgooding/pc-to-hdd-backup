"""
Author: Kelv Gooding
Created: 2023-11-06
Updated: 2023-11-06
Version: 1.0
"""

# Modules

import time

# Function to start timer from 0

def start_timer():
    global start
    start = time.time()

# Function to stop timer

def stop_timer():
    finished = time.time() - start
    print(f'Completed in {round(finished, 2)} second(s).')