import secrets
import cv2 as cv
import numpy as np
import os
from time import time,sleep
from windowcapture import WindowCapture
from vision import Vision


os.chdir(os.path.dirname(os.path.abspath(__file__)))



wincap = WindowCapture("Garry's Mod")


gpu_crash=cv.CascadeClassifier('cascade/cascade.xml')

vision_crash = Vision(None)

sleep(3)

loop_time = time()
while(True):


    screenshot = wincap.get_screenshot()


    cv.imshow('Tracker by kuba.#4158', screenshot)



    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    sleep(0.1)
    cv.imwrite('pozytywne/{}.jpg'.format(loop_time), screenshot)
    #key = cv.waitKey(1)
    #if key == ord('q'):
    #    cv.destroyAllWindows()
    #    break
    #elif key==ord('f'):
    #        cv.imwrite('pozytywne/{}.jpg'.format(loop_time), screenshot)
    #elif key==ord('d'):
    #        cv.imwrite('negatywne/{}.jpg'.format(loop_time), screenshot)



