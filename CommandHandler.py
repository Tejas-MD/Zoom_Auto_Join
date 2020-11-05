#list of commands and their callbacks!
from firstTimeRun import runFirstTimeStuff
import globalVars
from coreFunc import coreFunc

def commandHandler(whatCommand):
    switcher = {
      #TODO: Replace with core functionality with each var
      1: coreFunc(globalVars.x1), 
      2: coreFunc(globalVars.x2),
      3: coreFunc(globalVars.x3),
      4: coreFunc(globalVars.x4),
      5: coreFunc(globalVars.x5),
           
    }
    return switcher.get(whatCommand, "Invalid Command") 
    