from cmath import rect
import cv2 as cv
import numpy as np
import os
from time import time,sleep
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
import pydirectinput
from threading import Thread

wincap = WindowCapture("lunarclient")


gpu_crash=cv.CascadeClassifier('cascade\cascade.xml')



#keys
def klik(x):
    pydirectinput.keyDown(x)
    sleep(0.3)
    pydirectinput.keyUp(x)

def dluzszy_klik(x):
    pydirectinput.keyDown(x)
    sleep(0.5)
    pydirectinput.keyUp(x)


vision_crash = Vision(None)

is_bot_in_action =False

def bot_actions(rectangles):
    if len(rectangles) > 0:
        targets=vision_crash.get_click_points(rectangles)
        target=wincap.get_screen_position(targets[0])
        print('znalezione')
        mouse_pos=pyautogui.position()
        pyautogui.moveTo(x=target[0], y=target[1])
        #klik('e')
        pyautogui.moveTo(mouse_pos)
    if len(rectangles) == 0:
        print('Nie znaleziono celu')

    global is_bot_in_action
    is_bot_in_action = False

loop_time = time()
while(True):

    screenshot = wincap.get_screenshot()

   
    rectangles=gpu_crash.detectMultiScale(screenshot)


    detection_image=vision_crash.draw_rectangles(screenshot, rectangles)

    


   
    cv.imshow('siusiak', detection_image)
    if not is_bot_in_action: 
        is_bot_in_action=True
        t= Thread(target=bot_actions, args=(rectangles,))

        t.start()

    # debug the loop rate
    print(' FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()


    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    #elif key==ord('f'):
    #    cv.imwrite('pozytywne/{}.jpg'.format(loop_time), screenshot)
    #elif key==ord('d'):
    #    cv.imwrite('negatywne/{}.jpg'.format(loop_time), screenshot)

print('Koniec.')


#   C:\Users\KUBAC\Downloads\opencv\build\x64\vc15\bin\opencv_annotation.exe --images=pozytywne/ --annotations=pos.txt