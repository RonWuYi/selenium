import os
import time
import pyautogui as pya


while True:
    x, y = pya.position()
    pos = "Position: {} , {}".format(str(x).rjust(4), str(y).rjust(4))

    print(pos)
    time.sleep(0.3)
    os.system('clear')

# print('ending...')
