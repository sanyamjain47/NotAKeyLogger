import pyautogui
import data
import os
from time import time
import upload

def takeScreenshot():
    final_location = f'{os.path.expanduser(data.sspath)}/{round(time())}.png'
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(final_location, optimize = True)
    upload.upload_file(final_location)
