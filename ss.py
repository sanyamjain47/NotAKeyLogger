import pyautogui
import data
import os
from time import time
myScreenshot = pyautogui.screenshot()
myScreenshot.save(f'{os.path.expanduser(data.sspath)}/screen.png' )