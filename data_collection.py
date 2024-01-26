# takes screenshots for dataset

import pyscreenshot as ImageGrab
import keyboard
import time
import dxcam
from PIL import Image


x1 = 946 # equal to 1920/2-14
x2 = 974 # equal to 1920/2+14
y1 = 526 # equal to 1080/2-14
y2 = 554 # equal to 1080/2+14

camera = dxcam.create()
i = 0
while True:
    if keyboard.is_pressed("j"):
        try:
            SS = camera.grab(region=(x1, y1, x2, y2))
            
            im = Image.fromarray(SS)
            save_path = "./OW2dataset/target/" + str(time.time()) + "t.png"
            im.save(save_path)
            print("add target" + str(i))
            i+=1
        except:
            continue
        time.sleep(0.25)
    if keyboard.is_pressed("k"):
        try:
            SS = camera.grab(region=(x1, y1, x2, y2))
            
            im = Image.fromarray(SS)
            save_path = "./OW2dataset/not/" + str(time.time()) + "n.png"
            im.save(save_path)
            print("add not" + str(i))
            i+=1
        except:
            continue
        time.sleep(0.25)
