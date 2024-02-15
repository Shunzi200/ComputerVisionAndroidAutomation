
import os
import subprocess
import time
import win32gui
from multiprocessing import Pool, freeze_support, Process
import multiprocessing as mp
import re
from testScript import testScript
from snkrsPass import snkrsPass

def launch():
    cwd = os.getcwd()
    genfolder = os.path.dirname(__file__)
    toolspath = os.path.join(genfolder, 'scrpy')
    os.chdir(toolspath)
    os.system('adb devices')
    os.chdir(cwd)

def launchdevices():
    cwd = os.getcwd()
    genfolder = os.path.dirname(__file__)
    serial = os.path.join(genfolder, 'Settings', 'serial.txt')
    toolspath = os.path.join(genfolder, 'scrpy')
    SerialFile = open(serial, "r")
    SerialLine = list(SerialFile.read().splitlines())

    for serialname in SerialLine:
        os.chdir(toolspath)
        subprocess.Popen(
            'scrcpy --max-size 512 --window-borderless --window-title "' + serialname + '" --serial ' + serialname + '',
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        os.chdir(cwd)

def run_paralleltestScript():
    time.sleep(1)
    fileorexecute = __file__
    cwd = os.getcwd()
    genfolder = os.path.dirname(fileorexecute)
    toolspath = os.path.join(genfolder, 'scrpy')
    serial = os.path.join(genfolder, 'Settings', 'serial.txt')

    os.chdir(toolspath)
    listofdevices = str(subprocess.check_output("adb devices"))
    os.chdir(cwd)
    listofdevices = re.split(r"n|\\", listofdevices)
    numofdevices = int(((len(listofdevices) - 3) / 4) - 1)

    position = 0

    print("")
    print("LoopIO has detected " + str(numofdevices) + " devices")
    print("")

    delay = eval(input("Enter Delay: "))
    serialwrite = open(serial, 'w')
    serialwrite.write("")
    serialwrite.close()

    if int(len(listofdevices)) > 7:
        serialwrite = open(serial, 'w')
        serialwrite.write(listofdevices[3])
        serialwrite.close()
        position = position + 7
        for n in range(numofdevices):
            serialwrite = open(serial, 'a')
            serialwrite.write("\n")
            serialwrite.write(listofdevices[position])
            serialwrite.close()
            position += 4
            numofdevices -= 1

    SerialFile = open(serial, "r")
    SerialLine = list(SerialFile.read().splitlines())

    # os.close(po)
    time.sleep(3)

    pool = mp.Pool(mp.cpu_count())
    launchdevices()
    time.sleep(5)
    pool.starmap(testScript, [(n, delay) for n in SerialLine])
    # pool.close()

    subprocess.Popen('taskkill /IM scrcpy.exe', stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def run_parallelsnkrsPass():
    time.sleep(1)
    fileorexecute = __file__
    cwd = os.getcwd()
    genfolder = os.path.dirname(fileorexecute)
    toolspath = os.path.join(genfolder, 'scrpy')
    serial = os.path.join(genfolder, 'Settings', 'serial.txt')

    os.chdir(toolspath)
    listofdevices = str(subprocess.check_output("adb devices"))
    os.chdir(cwd)
    listofdevices = re.split(r"n|\\", listofdevices)
    numofdevices = int(((len(listofdevices) - 3) / 4) - 1)

    position = 0

    print("")
    print("LoopIO has detected " + str(numofdevices) + " devices")
    print("")

    delay = eval(input("Enter Delay: "))
    serialwrite = open(serial, 'w')
    serialwrite.write("")
    serialwrite.close()

    if int(len(listofdevices)) > 7:
        serialwrite = open(serial, 'w')
        serialwrite.write(listofdevices[3])
        serialwrite.close()
        position = position + 7
        for n in range(numofdevices):
            serialwrite = open(serial, 'a')
            serialwrite.write("\n")
            serialwrite.write(listofdevices[position])
            serialwrite.close()
            position += 4
            numofdevices -= 1

    SerialFile = open(serial, "r")
    SerialLine = list(SerialFile.read().splitlines())

    # os.close(po)
    time.sleep(3)

    pool = mp.Pool(mp.cpu_count())
    launchdevices()
    time.sleep(5)
    pool.starmap(snkrsPass, [(n, delay) for n in SerialLine])
    # pool.close()

    subprocess.Popen('taskkill /IM scrcpy.exe', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

