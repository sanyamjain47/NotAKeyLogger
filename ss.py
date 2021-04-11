import pyautogui
import data
import os
from time import time
import upload

# A basic function to take a screenshot and then delete it
def takeScreenshot():
    final_location = f'{os.path.expanduser(data.sspath)}/{round(time())}.png'
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(final_location, optimize = True)
    upload.upload_file(final_location)
    os.remove(final_location) 