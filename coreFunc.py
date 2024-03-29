import subprocess
import time
import pyperclip
import keyboard
import pyautogui
from meetCodeSwitcher import meetCodeGiver


def openZoomfromtxt():  # Using the Zoom Path TXT
    zoomPathFile = open("ZoomPath.txt", "r")
    subprocess.Popen(zoomPathFile.read())
    zoomPathFile.close()
    # print('Please observe if ZOOM opens in 15 sec')
    time.sleep(14)


def accessCoods(FileName):
    ObjectName = open(FileName, "r")
    plusButtonX = int(ObjectName.read())
    ObjectName.close()
    return plusButtonX


def coreFunc(initalsPlease):
    # Everyrhing down here is the core func. TODO: to be wrapped and kept somewhere and used if user command is a num btw 1-5(TeacherNumberCode.py)
    print()
    print('Teacher to Join: ' + initalsPlease)
    print("Finding the Meeting Code, Just a Second...")  # PROCESSING
    outputCode = meetCodeGiver(initalsPlease)

    print(meetCodeGiver(initalsPlease))  # OUTPUT

    if outputCode == "Didn't find a match. Check the Inital Again Maybe?":
        return

    pyperclip.copy(outputCode)

    # Open Zoom
    print("Meeting Code Retrieved, Opening Zoom, you're welcome :-)")
    openZoomfromtxt()

    # Wait until it opens
    time.sleep(14)

    # Close the "free trial ended thing"
    pyautogui.moveTo(x=683, y=468)
    pyautogui.click()
    time.sleep(2)

    # Click on the Join(+) Icon!
    print('Trying the + Button!')
    plusButtonX = accessCoods('plusXCoordinate.txt')
    plusButtonY = accessCoods('plusYCoordinate.txt')

    pyautogui.moveTo(plusButtonX, plusButtonY)
    pyautogui.click()
    time.sleep(2)  # Zoom is obviously slower than my code

    # Type the meeting ID
    keyboard.write(str(outputCode))  # Keyboard can only iterate strings!
    print("Typing the Code")
    # pyautogui.moveTo(527,457) #Turn off video button
    # pyautogui.click() #Not required cause there's a zoom setting.
    time.sleep(1)

    # Clicking Join
    print('Lets Go!')
    joinButtonX = accessCoods('joinXCoordinate.txt')
    joinButtonY = accessCoods('joinYCoordinate.txt')
    pyautogui.moveTo(joinButtonX, joinButtonY)
    pyautogui.click()

    time.sleep(5)  # Zoom is obviously slower than my code

    keyboard.write("mesmpl")
    print("There you go, the password!")
    # pyautogui.moveTo(691,498) #Join Meeting Button after entering password   #Not Req cause it occurs at same coordinates
    pyautogui.click()
    # cntd = input('Do you want to Rejoin? y/n')
    # if cntd=='y':
    #     coreFunc(initalsPlease)
    # else:
    #     pass

    # All the TODOS, any additional features, will have to be coded here.
