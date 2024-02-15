
from art import tprint
import sys
from utils import show_exception_and_exit, clear
from device_management import launch, launchdevices, run_paralleltestScript, run_parallelsnkrsPass
import time
import os
import subprocess

def menu():
    cwd = os.getcwd()
    genfolder = os.path.dirname(__file__)
    toolspath = os.path.join(genfolder, 'scrpy')
    os.chdir(toolspath)
    subprocess.Popen('adb start-server', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    os.chdir(cwd)
    sys.tracebacklimit = 0
    tprint("LoopIO")

    print("Main Menu:")
    print("1. Get Devices ID")
    print("2. Test Script")
    print("3. SNKRS Pass Script")
    print("4. Exit")
    choice1 = input("Enter: ")
    if choice1 == "1":
        launch()
        print("")
        waituntil = input("Enter any key to go back to Main Menu: ")
        if waituntil == "":
            clear()
            menu()
    if choice1 == "2":
        run_paralleltestScript()
        time.sleep(3)
        print("")
        waituntil = input("Enter any key to go back to Main Menu: ")
        if waituntil == "":
            clear()
            menu()
    if choice1 == "3":
        run_parallelsnkrsPass()
        time.sleep(3)
        print("")
        waituntil = input("Enter any key to go back to Main Menu: ")
        if waituntil == "":
            clear()
            menu()
    if choice1 == "4":
        sys.exit()

    else:
        print("Invalid Choice")
        time.sleep(0.5)
        clear()
        menu()

if __name__ == '__main__':
    sys.excepthook = show_exception_and_exit
    menu()
