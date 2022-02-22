import pyautogui
from subprocess import Popen
import time

Popen('calc')
time.sleep(0.5)

pyautogui.typewrite(' 123+456=', interval=0.2)
time.sleep(0.5)
