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
    subprocess.Popen("C:\\Users\\home\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

    #Wait until it opens 
    time.sleep(10)

    #Type ID and click Join
    join_btn = pyautogui.locateCenterOnScreen('join_button.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()


    # Type the meeting ID
    meeting_id_btn =  pyautogui.locateCenterOnScreen('meeting_id_button.png')
    pyautogui.moveTo(meeting_id_btn)
    pyautogui.click()
    keyboard.write(str(outputCode))  # Keyboard can only iterate strings!
    print("Typing the Code")
    time.sleep(5)

    
    keyboard.write("mesmpl")
    print("There you go, the password!")
    cntd = input('Do you want to Rejoin? y/n')
    if cntd=='y':
        coreFunc(initalsPlease)
    else:
        pass

    #All the TODOS, any additional features, will have to be coded here.
