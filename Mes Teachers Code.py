from meetCodeGiverF import meetCodeGiver
import pyperclip 
import subprocess


x = input('Enter the Initial of the Teacher:  ')  #INPUT
x= x.upper()


print("Finding the Meeting Code, Just a Second...") #PROCESSING
outputCode = meetCodeGiver(x)


print (meetCodeGiver(x))    #OUTPUT 
pyperclip.copy(outputCode)
print("Code Copied to Clipboard, Opening Zoom, you're welcome :-)")
subprocess.Popen("C:\\Users\\home\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
#All the TODOS, any additional features, will have to be coded here. 