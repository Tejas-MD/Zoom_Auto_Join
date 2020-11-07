import subprocess,time,pyperclip,keyboard
from meetCodeSwitcher import meetCodeGiver

def coreFunc(initalsPlease):
    #Everyrhing down here is the core func. TODO: to be wrapped and kept somewhere and used if user command is a num btw 1-5(TeacherNumberCode.py)
    print()
    print("Finding the Meeting Code, Just a Second...")  # PROCESSING
    outputCode = meetCodeGiver(initalsPlease)

    print(meetCodeGiver(initalsPlease))  # OUTPUT
    pyperclip.copy(outputCode)

    print("Code Copied to Clipboard, Opening Zoom, you're welcome :-)")
    subprocess.Popen("C:\\Users\\home\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(7)
    keyboard.write(str(outputCode))  # Keyboard can only iterate strings!
    print("Pasting the Code")
    time.sleep(5)
    keyboard.write("mesmpl")
    print("There you go, the password!")

    #All the TODOS, any additional features, will have to be coded here.
