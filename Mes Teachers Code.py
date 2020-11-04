from meetCodeGiverF import meetCodeGiver
import pyperclip 



x = input('Enter the Initial of the Teacher:  ')  #INPUT
x= x.upper()


print("Finding the Meeting Code, Just a Second...") #PROCESSING
outputCode = meetCodeGiver(x)


print (meetCodeGiver(x))    #OUTPUT 
pyperclip.copy(outputCode)
print("Code Copied to Clipboard, you're welcome :-)")
#All the TODOS, any additional features, will have to be coded here. 