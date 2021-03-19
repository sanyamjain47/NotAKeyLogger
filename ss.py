import pyautogui
import data
import os
from time import time

def takeScreenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'{os.path.expanduser(data.sspath)}/{round(time())}.png', optimize = True)

#takeScreenshot()