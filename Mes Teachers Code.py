#Proudly mine #Tejas-MD

from firstTimeRun import runFirstTimeStuff
from meetCodeSwitcher import meetCodeGiver
import globalVars
from coreFunc import coreFunc
from autoTimeMode import autoTimeModee as autoTimeMode

runFirstTimeStuff()  #One time, accepts 5 teachers initals and stores in 5 vars: x1,x2,x3,x4,x5

recommendedNumberToJoin = 1

while(True): #TODO: Wrongly looping, urgent fix needed! 
    print()
    cmd=input('Waiting for your Orders, use -h for list of commands\n' + 'Recommended Number cause you are forgetful: ' + str(recommendedNumberToJoin))
    print()
    #TODO: Add commands list and teachers stored for this execution 
   
    if cmd=="-h":
        print()
        print("*Use -nt for reading teachers of the day ")
        print("*Use -lt for listing the number,order and Initials of already input teachers")
        print("*Enter a number btw 1-6 to join the particular class!") 
        print()

    elif cmd=="-lt":
        print()
        print(globalVars.x1,globalVars.x2,globalVars.x3,globalVars.x4,globalVars.x5,globalVars.x6) #TODO: Add Spaces #Cause this was causing issues in the command handler
        print()

    elif cmd=="-nt": 
        runFirstTimeStuff() #Cause this was causing issues in the command handler

    elif cmd=='auto':
        autoTimeMode()

    else:
       if cmd=='1': #TODO: NOT WORKING, URGENT FIX NEEDED.   # So this is like the base station. It intelligently divertes you to the right function.
           coreFunc(globalVars.x1)    
           recommendedNumberToJoin=recommendedNumberToJoin+1
       elif cmd=='2':
           coreFunc(globalVars.x2)
           recommendedNumberToJoin=recommendedNumberToJoin+1
       elif cmd=='3':
            coreFunc(globalVars.x3)
            recommendedNumberToJoin=recommendedNumberToJoin+1
       elif cmd=='4':
            coreFunc(globalVars.x4)
            recommendedNumberToJoin=recommendedNumberToJoin+1
       elif cmd=='5':
            coreFunc(globalVars.x5)
            recommendedNumberToJoin=recommendedNumberToJoin+1
       elif cmd=='6':
            coreFunc(globalVars.x6)
            recommendedNumberToJoin=recommendedNumberToJoin+1
       else:
           print()
           print("I Gave you so many commands to use but you have the audacity to enter the one I don't know about!")
           print() 

