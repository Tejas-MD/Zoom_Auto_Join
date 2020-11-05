#Proudly mine #Tejas-MD

from firstTimeRun import runFirstTimeStuff
from meetCodeSwitcher import meetCodeGiver
from CommandHandler import commandHandler
import globalVars

runFirstTimeStuff()  #One time, accepts 5 teachers initals and stores in 5 vars: x1,x2,x3,x4,x5

while(True): #TODO: Wrongly looping, urgent fix needed! 

    cmd=input('Waiting for your Orders, use --help for list of commands')
    #TODO: Add commands list and teachers stored for this execution 
   
    if cmd=="--help":
        print("*Use --newT for reading teachers of the day ")
        print("*Use --listT for listing the number,order and Initials of already input teachers")
        print("*Enter a number btw 1-5 to join the particular class!") 

    elif cmd=="--listT":
        print(globalVars.x1,globalVars.x2,globalVars.x3,globalVars.x4,globalVars.x5) #TODO: Add Spaces #Cause this was causing issues in the command handler

    elif cmd=="--newT": 
        runFirstTimeStuff() #Cause this was causing issues in the command handler

    else:
        commandHandler(cmd) #TODO: NOT WORKING, URGENT FIX NEEDED.   # So this is like the base station. It intelligently divertes you to the right function.
        break
        # cmd="null"