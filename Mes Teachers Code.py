from meetCodeGiverF import meetCodeGiver
import pyperclip 
import subprocess
import keyboard
import time

while(True):
    x = input('Enter the Initial of the Teacher:  ')  #INPUT
    x= x.upper()


    print("Finding the Meeting Code, Just a Second...") #PROCESSING
    outputCode = meetCodeGiver(x)


    print (meetCodeGiver(x))    #OUTPUT 
    pyperclip.copy(outputCode)
    
    print("Code Copied to Clipboard, Opening Zoom, you're welcome :-)")
    subprocess.Popen("C:\\Users\\home\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    time.sleep(7)
    keyboard.write(str(outputCode))  #Keyboard can only iterate strings!
    print("Pasting the Code")
    time.sleep(7)
    keyboard.write("mesmpl")
    #All the TODOS, any additional features, will have to be coded here. 