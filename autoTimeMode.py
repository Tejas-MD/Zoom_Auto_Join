import time
from coreFunc import coreFunc as coreFunc
import globalVars

stale = [False,False,False,False,False,False]

def timeClassComparer(hours,mins,arrayIndex,globalVarHere):
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    if ((hour==hours) and (min== mins)):
        if stale[arrayIndex]==False:
            coreFunc(globalVarHere)
            stale[arrayIndex]=True
    else:
        pass


def autoTimeModee():
    print("I will take care of the classes myself, Tejas.")
    while(True):
        # year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
        # if ((hour==11) and (min== 18)):
        #     if stale[0]==False:
        #         coreFunc(globalVars.x1)
        #         stale[0]=True
        #     else:
        #         pass
        timeClassComparer(10,2,0,globalVars.x1)
        timeClassComparer(11,2,1,globalVars.x2)
        timeClassComparer(12,2,2,globalVars.x3)
        timeClassComparer(13,17,3,globalVars.x4)
        timeClassComparer(14,17,4,globalVars.x5)
        timeClassComparer(15,17,5,globalVars.x6)
        
        # #test
        # timeClassComparer(13,21,1,globalVars.x2) #WORKING!


# autoTimeModee()




    