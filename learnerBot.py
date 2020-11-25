import time
import subprocess
import pyautogui


print('Hey, This must be your first time here! I will learn to join your classes if you show me how, only once.')
time.sleep(1)


def zoomPathCalib():
    # Zoom App Open Calibration
    zoomPath = input(
        'Please Enter the path to your zoom.exe. NOTE: Please use // insted of / in the path! ')
    zoomPathFile = open("ZoomPath.txt", "w+")
    zoomPathFile.write(zoomPath)
    zoomPathFile.close()

def openZoomfromtxt():    #Using the Zoom Path TXT
    zoomPathFile= open("ZoomPath.txt","r")
    subprocess.Popen(zoomPathFile.read())
    zoomPathFile.close()
    print('Please observe if ZOOM opens in 15 sec')
    time.sleep(14)


def accessCoods(FileName):
    ObjectName= open(FileName,"r")
    plusButtonX = int(ObjectName.read())
    ObjectName.close()
    return plusButtonX
    

    # plusYCoordinateFile= open("plusYCoordinate.txt","r")
    # plusButtonY = int(plusYCoordinateFile.read())
    # plusYCoordinateFile.close()


zoomPathCalib()


openZoomfromtxt()
zoomPathConfirm = input('Did it Open?(y/n)  ')

if zoomPathConfirm == 'y':
    print('Cool! Lets Proceed')
   

elif zoomPathConfirm == 'n':
    print('No Worries, Lets redo the zoom path thing')
    zoomPathCalib()


###############################################################################################
# Coordinates Calibration

###################################################
#Plus Button 


print('Okay, Now you got to show me how to join the meeting\n')
print('Please do not drag/ move the zoom window\n')
print('Please place your mouse at the centre of the Join(Plus) icon for the 15 seconds and wait\n')
time.sleep(15) #Waiting for user to place mouse on Join(+)

plusx,plusy=pyautogui.position()
plusXCoordinateFile = open("plusXCoordinate.txt", "w+")
plusXCoordinateFile.write(str(plusx))
plusXCoordinateFile.close()
plusYCoordinateFile = open("plusYCoordinate.txt", "w+")
plusYCoordinateFile.write(str(plusy))
plusYCoordinateFile.close()

#Practicing
print('Cool, i know how to click on the + button now, Lemme try it. Please dont touch your mouse for the next 15 secs\n')
openZoomfromtxt()
print('Opened Zoom, YAY!')

print('Trying the + Button!')
plusButtonX=accessCoods('plusXCoordinate.txt')
plusButtonY=accessCoods('plusYCoordinate.txt')

pyautogui.moveTo(plusButtonX,plusButtonY)
pyautogui.click()

print('I know I did well, Thanks! (Blush) \n')


###########################################################
#Join Button 
print('Okay One last thing, I need to see where the join button is after typing the code')
print('Please point your mouse at the join button that you gotta press after entering the code for 15 sec')
time.sleep(15)

joinX,joinY=pyautogui.position()
joinXCoordinateFile = open("joinXCoordinate.txt", "w+")
joinXCoordinateFile.write(str(joinX))
joinXCoordinateFile.close()
joinYCoordinateFile = open("joinYCoordinate.txt", "w+")
joinYCoordinateFile.write(str(joinY))
joinYCoordinateFile.close()

#######################################################

print('I will do everything you taught me to test, please close zoom and sit back')

time.sleep(8)

print('Opening Zoom')
openZoomfromtxt()

print('Clicking +')
plusButtonX=accessCoods('plusXCoordinate.txt')
plusButtonY=accessCoods('plusYCoordinate.txt')
pyautogui.moveTo(plusButtonX,plusButtonY)
pyautogui.click()

time.sleep(6)

#Will Open, read and close file
print('Clicking Join')
joinButtonX=accessCoods('joinXCoordinate.txt')  
joinButtonY=accessCoods('joinYCoordinate.txt')
pyautogui.moveTo(joinButtonX,joinButtonY)
pyautogui.click()

print('Done! Thanks for teaching me all this, if something did not go right, reopen me. OtherWise, Enjoy the main program!')

#######################################################


#########################################################################################################################
