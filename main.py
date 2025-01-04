import os
import time
from datetime import datetime

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()
        current_time = datetime.now().strftime("%I:%M:%S %p")
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("\n" + " Clock ".center(30, "="))
        print(f"\n Time: {current_time}")
        print(f"\n Date: {current_date}")
        time.sleep(1)

main()