import numpy as np
import sys
import cv2
import webbrowser
from mss import mss
from PIL import Image, ImageChops
import PIL
from time import sleep
import pyautogui

f = open("../settings.txt", "r",encoding="utf-8")
i=0
height = 0
width = 0
url = ''
delay = 0
oldsettings = []
for row in f:
    if i<4:
        oldsettings.append(row)
    setting = row.split(';')[0]
    val     = row.split(';')[1]
    if setting == 'screenWidth':
        width = int(val)
    elif setting == 'screenHeight':
        height = int(val)
    elif setting == 'url':
        url = val
    elif setting == 'delay':
        delay = int(val)
    i=i+1
f.close()

mon = {'top': 0, 'left': 0, 'width': width-1, 'height': height-1}

refPt = []
def on_click(event, x, y, p1, p2):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"{x} : {y}")
        refPt.append([x, y])
        #mark = {'top': x_1, 'left': y_1, 'width': abs(x_1-x), 'height': abs(y_1-x)}
        #zoom = img.get_pixels(mark)
        #zoom.save(r"zoom.png")
        #diff = imagechops.difference(zoomImg, zoomImg)
        #diff.save(r"diff.png")

sct = mss()
webbrowser.open(url)
sleep(delay)
sct.get_pixels(mon)
img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
delay = 0.3
sleep(delay)
pyautogui.hotkey("altleft", "tab")
sleep(delay)
pyautogui.hotkey("ctrlleft", "w")
sleep(delay)
pyautogui.hotkey("altleft", "tab")
sleep(delay)

while 1:
    cv2.imshow('test', np.array(img))
    cv2.namedWindow('test')
    cv2.moveWindow('test', 0, 0)
    cv2.setMouseCallback('test', on_click)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    i=0
    if len(refPt) == 3:
        x1=refPt[0][0]
        x2=refPt[1][0]
        y1=refPt[0][1]
        y2=refPt[1][1]

        x3=refPt[2][0]
        y3=refPt[2][1]
        #region = {'top': refPt[0][1], 'left': refPt[0][0], 'width': abs(refPt[0][0]-refPt[0][1]), 'height': abs(refPt[1][0]-refPt[1][1])}
        f = open("../settings.txt", "w",encoding="utf-8")
        for s in oldsettings:
            f.write(s)
        f.write(f"left;{x1}")
        f.write(f"\nright;{x2}")
        f.write(f"\ntop;{y1}")
        f.write(f"\nbottom;{y2}")
        f.write(f"\nclick x;{x3}")
        f.write(f"\nclick y;{y3}")
        f.close()
        zoom = img.crop((x1, y1, x2, y2))
        zoom.save(r"../pictures/zoom.png")
        cv2.destroyAllWindows()
        break
exit()
while 1:
    sct.get_pixels(mon)
    img = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
    diff = imagechops.difference(zoom, img)
    if list(targ.getdata()) == list(diff.getdata()):
        sleep(delay)
        pyautogui.hotkey("altleft", "tab")
        sleep(delay)
        pyautogui.hotkey("ctrlleft", "w")
        sleep(delay)
        pyautogui.hotkey("altleft", "tab")
        sleep(delay)
        if password != "x":
            pyautogui.click(800, 460)
            for c in password:
                pyautogui.typewrite([c]) 
            pyautogui.typewrite(["enter"]) 
        cv2.destroyAllWindows()
        exit()
    cv2.imshow('test', np.array(diff))
    cv2.moveWindow('test', 20, 20)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    #elif cv2.waitKey(25) & 0xFF == ord('s'):
        ##im2 = Image.open(r"D:/python/screen.jpg")  
        #img.save('D:/python/screen.jpg')
    #elif cv2.waitKey(25) & 0xFF == ord('d'):
        #if diff.getbbox():
            #diff.show()