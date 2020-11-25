import subprocess,time,pyperclip,keyboard,pyautogui
from meetCodeSwitcher import meetCodeGiver

def coreFunc(initalsPlease):
    #Everyrhing down here is the core func. TODO: to be wrapped and kept somewhere and used if user command is a num btw 1-5(TeacherNumberCode.py)
    print()
    print('Teacher to Join: '+ initalsPlease)
    print("Finding the Meeting Code, Just a Second...")  # PROCESSING
    outputCode = meetCodeGiver(initalsPlease)

    print(meetCodeGiver(initalsPlease))  # OUTPUT
    
    if outputCode=="Didn't find a match. Check the Inital Again Maybe?":
        return

    pyperclip.copy(outputCode)

    #Open Zoom
    print("Code Copied to Clipboard, Opening Zoom, you're welcome :-)")
    openZoom = subprocess.Popen("C:\\Users\\home\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

    #Wait until it opens 
    time.sleep(14)

    #Click on the Join(+) Icon!
    pyautogui.moveTo(590,283)
    pyautogui.click()

    time.sleep(2)
    # Type the meeting ID
    keyboard.write(str(outputCode))  # Keyboard can only iterate strings!
    print("Typing the Code")
    # pyautogui.moveTo(527,457) #Turn off video button
    # pyautogui.click() #Not required cause there's a zoom setting.
    time.sleep(1)
    pyautogui.moveTo(707,498) #Join Button
    pyautogui.click()
    time.sleep(5)
    
    keyboard.write("mesmpl")
    print("There you go, the password!")
    # pyautogui.moveTo(691,498) #Join Meeting Button after entering password   #Not Req cause it occurs at same coordinates
    pyautogui.click() 
    # cntd = input('Do you want to Rejoin? y/n')
    # if cntd=='y':
    #     coreFunc(initalsPlease)
    # else:
    #     pass

    #All the TODOS, any additional features, will have to be coded here.
