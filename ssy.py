import secrets
import cv2 as cv
import numpy as np
import os
from time import time,sleep
from windowcapture import WindowCapture
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture("Garry's Mod")

#load the trained model
gpu_crash=cv.CascadeClassifier('cascade/cascade.xml')
#load empty vision class
vision_crash = Vision(None)

sleep(3)

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    #object detection
    #rectangles= gpu_crash.detectMultiScale(screenshot)

    #draw the detection on original image

    #detection_image=vision_crash.draw_rectangles(screenshot, rectangles)

    #display images
    cv.imshow('Tracker by kuba#4158', screenshot)


    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    cv.imwrite('negatywne2/{}.jpg'.format(loop_time), screenshot)
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
    elif key==ord('f'):
        cv.imwrite('pozytywne/{}.jpg'.format(loop_time), screenshot)
    elif key==ord('d'):
        cv.imwrite('negatywne/{}.jpg'.format(loop_time), screenshot)

print('Done.')


#   C:\Users\KUBAC\Downloads\opencv\build\x64\vc15\bin\opencv_annotation.exe --images=pozytywne/ --annotations=pos.txt