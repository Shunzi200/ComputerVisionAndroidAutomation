
import os
import subprocess
import time
import win32gui
from PIL import Image
import cv2
import numpy as np
import sys
import win32ui
import windll



def snkrsPass(serialname, delay):
    fileorexecute = __file__
    sys.tracebacklimit = 0
    time.sleep(0.3)
    cwd = os.getcwd()
    genfolder = os.path.dirname(fileorexecute)
    imagepath = os.path.join(genfolder, 'Image')
    imagee = os.path.join(imagepath, serialname + '.png')
    toolspath = os.path.join(genfolder, 'scrpy')
    serial = os.path.join(genfolder, 'Settings', 'serial.txt')
    print("")
    print("[" + serialname + "] Starting Script...")
    time.sleep(3)
    os.chdir(toolspath)
    displaysize = subprocess.check_output("adb -s " + serialname + " shell wm size")
    displaystring = str(displaysize)
    cha1 = displaystring[22]
    cha2 = displaystring[23]
    cha3 = displaystring[24]
    cha4 = displaystring[25]
    display = '' + cha1 + '' '' + cha2 + '' '' + cha3 + '' '' + cha4 + ''
    hwnd = win32gui.FindWindow(None, serialname)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top
    xaxis = 0
    yaxis = 0
    win32gui.MoveWindow(hwnd, xaxis, yaxis, w, h, True)
    time.sleep(2)
    print("")
    print("[" + serialname + "] Waiting for SNKRS Pass to Go Live")
    val = 0
    matched = 0
    matched2 = 0
    button1match = 0
    button2match = 0
    button3match = 0
    buttonclick1 = 0
    buttonclick2 = 0
    start_time = time.time()

    while val < 1:
        hwnd = win32gui.FindWindow(None, serialname)
        left, top, right, bot = win32gui.GetWindowRect(hwnd)
        w = right - left
        h = bot - top
        hwndDC = win32gui.GetWindowDC(hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

        saveDC.SelectObject(saveBitMap)
        result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)

        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwndDC)

        if result == 1:
            # PrintWindow Succeeded
            im.save(imagee)

        temp = os.path.join(imagepath, 'button1.png')
        temp2 = os.path.join(imagepath, 'button2.png')
        temp3 = os.path.join(imagepath, 'button3.png')

        template1 = cv2.imread(temp, 0)
        template2 = cv2.imread(temp2, 0)
        template3 = cv2.imread(temp3, 0)
        img = cv2.imread(imagee)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        for scale in np.linspace(0.7, 1.5, 20)[::- 1]:
            resized = cv2.resize(template1, None, None, fx=scale, fy=scale)
            res = cv2.matchTemplate(img_gray, resized, cv2.TM_CCOEFF_NORMED)
            resized2 = cv2.resize(template2, None, None, fx=scale, fy=scale)
            res2 = cv2.matchTemplate(img_gray, resized2, cv2.TM_CCOEFF_NORMED)
            resized3 = cv2.resize(template3, None, None, fx=scale, fy=scale)
            res3 = cv2.matchTemplate(img_gray, resized3, cv2.TM_CCOEFF_NORMED)
            w, h = resized.shape[::-1]
            w2, h2 = resized2.shape[::-1]
            w3, h3 = resized3.shape[::-1]
            threshold = 0.8
            threshold2 = 0.8
            threshold3 = 0.8

            loc = np.where(res >= threshold)
            loc2 = np.where(res2 >= threshold2)
            loc3 = np.where(res3 >= threshold3)

            for pt in zip(*loc[::-1]):
                he, wi, ca = img.shape
                c1 = round((pt[0] + pt[0] + w) / 2)
                d1 = round((pt[1] + pt[1] + h) / 2)
                s1 = round(((c1 * int(display)) / he))
                p1 = round(((d1 * int(display)) / he))
                button1match = 1

            for pt in zip(*loc2[::-1]):
                he, wi, ca = img.shape
                c2 = round((pt[0] + pt[0] + w2) / 2)
                d2 = round((pt[1] + pt[1] + h2) / 2)
                s2 = round(((c2 * int(display)) / he))
                p2 = round(((d2 * int(display)) / he))
                button2match = 1

            for pt in zip(*loc3[::-1]):
                he, wi, ca = img.shape
                c3 = round((pt[0] + pt[0] + w3) / 2)
                d3 = round((pt[1] + pt[1] + h3) / 2)
                s3 = round(((c3 * int(display)) / he))
                p3 = round(((d3 * int(display)) / he))
                button3match = 1

        if buttonclick1 == 0:
            if button1match == 1:
                time.sleep(delay)
                print("")
                print("[" + serialname + "] SNKRS PASS LIVE!")
                m1 = '"' + str(s1) + '"'
                n1 = '"' + str(p1) + '"'
                os.chdir(toolspath)
                subprocess.Popen('adb -s ' + serialname + ' shell input tap ' + m1 + ' ' + n1 + '')
                os.chdir(cwd)
                matched = 1
                button1match = 0
                time.sleep(delay)
                buttonclick1 = 1
        if buttonclick2 == 0:
            if button2match == 1 and matched == 1:
                time.sleep(delay)
                print("")
                print("[" + serialname + "] RESERVING...")
                m2 = '"' + str(s2) + '"'
                n2 = '"' + str(p2) + '"'
                os.chdir(toolspath)
                subprocess.Popen('adb -s ' + serialname + ' shell input tap ' + m2 + ' ' + n2 + '')
                os.chdir(cwd)
                matched2 = 1
                button2match = 0
                time.sleep(delay)
                buttonclick2 = 1

        if button3match == 1 and matched2 == 1:
            time.sleep(delay)
            print("")
            print("[" + serialname + "] SUBMITTING RESERVATION...")
            m3 = '"' + str(s3) + '"'
            n3 = '"' + str(p3) + '"'
            os.chdir(toolspath)
            subprocess.Popen('adb -s ' + serialname + ' shell input tap ' + m3 + ' ' + n3 + '')
            os.chdir(cwd)
            print("")
            print("--- %s seconds ---" % (time.time() - start_time))
            time.sleep(3)
            os.remove(imagee)
            subprocess.Popen('taskkill /IM scrcpy.exe', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            button3match = 0
            val = 3
            time.sleep(3)
            break

            sys.exit
