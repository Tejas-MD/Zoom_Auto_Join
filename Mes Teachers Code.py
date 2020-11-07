#Proudly mine #Tejas-MD

from firstTimeRun import runFirstTimeStuff
from meetCodeSwitcher import meetCodeGiver
import globalVars
from coreFunc import coreFunc

runFirstTimeStuff()  #One time, accepts 5 teachers initals and stores in 5 vars: x1,x2,x3,x4,x5

while(True): #TODO: Wrongly looping, urgent fix needed! 
    cmd=input('Waiting for your Orders, use --help for list of commands')
    #TODO: Add commands list and teachers stored for this execution 
   
    if cmd=="-h":
        print("*Use --nT for reading teachers of the day ")
        print("*Use --lT for listing the number,order and Initials of already input teachers")
        print("*Enter a number btw 1-5 to join the particular class!") 

    elif cmd=="-lT":
        print(globalVars.x1,globalVars.x2,globalVars.x3,globalVars.x4,globalVars.x5) #TODO: Add Spaces #Cause this was causing issues in the command handler

    elif cmd=="-nT": 
        runFirstTimeStuff() #Cause this was causing issues in the command handler

    else:
       if cmd=='1': #TODO: NOT WORKING, URGENT FIX NEEDED.   # So this is like the base station. It intelligently divertes you to the right function.
           coreFunc(globalVars.x1)
       elif cmd=='2':
           coreFunc(globalVars.x2)
       elif cmd=='3':
            coreFunc(globalVars.x3)
       elif cmd=='4':
            coreFunc(globalVars.x4)
       elif cmd=='5':
            coreFunc(globalVars.x5)
       else:
           print("")
           print("I Gave you so many commands to use but you have the audacity to enter the one I don't know about!")
           print("") 


#TODO:
# Add Spaces in terminal Prints
# Add confirm which teacher it understood in coreFunc. 