import pydirectinput
import pyautogui
from time import sleep 



def klik(x):
    pydirectinput.keyDown(x)
    sleep(0.3)
    pydirectinput.keyUp(x)

def dluzszy_klik(x):
    pydirectinput.keyDown(x)
    sleep(0.5)
    pydirectinput.keyUp(x)

sleep(2)

ab=pyautogui.position()

cd=pyautogui.position()
print(ab)
print(cd)


dluzszy_klik('w')
klik('e')
dluzszy_klik('s')
