import pyautogui
from icecream import ic
import time 

print("Waiting 10 seconds until you move to where req")
time.sleep(10)
plusx,plusy=pyautogui.position()
ic(plusx , plusy)
