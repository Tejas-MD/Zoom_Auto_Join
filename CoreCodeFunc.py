import subprocess,time,pyperclip,keyboard,pyautogui
import pandas as pd
from datetime import datetime


#reading the meeting details
df = pd.read_csv('meetingschedule.csv')
df_new = pd.DataFrame()

def openZoomfromtxt():    #Using the Zoom Path TXT
    zoomPathFile= open("ZoomPath.txt","r")
    subprocess.Popen(zoomPathFile.read())
    zoomPathFile.close()
    time.sleep(14)

def accessCoods(FileName):
    ObjectName= open(FileName,"r")
    plusButtonX = int(ObjectName.read())
    ObjectName.close()
    return plusButtonX


def coreCodeFunc():
    
   #Check the current system time
    timestr = datetime.now().strftime("%H:%M")
    #Check if the current time is mentioned in the Dataframe
    if timestr in df.Time.values:
        df_new = df[df['Time'].astype(str).str.contains(timestr)]
        #Open Zoom
        print("Meeting Code Retrieved, Opening Zoom, you're welcome :-)")
        openZoomfromtxt()

        #Wait until it opens 
        time.sleep(14)


        #Click on the Join(+) Icon!
        print('Trying the + Button!')
        plusButtonX=accessCoods('plusXCoordinate.txt')
        plusButtonY=accessCoods('plusYCoordinate.txt')

        pyautogui.moveTo(plusButtonX,plusButtonY)
        pyautogui.click()
        time.sleep(2)    #Zoom is obviously slower than my code


        # Type the meeting ID
        keyboard.write(df_new.iloc[0,1])  # Keyboard can only iterate strings!
        print("Typing the Code")
        # pyautogui.moveTo(527,457) #Turn off video button
        # pyautogui.click() #Not required cause there's a zoom setting.
        time.sleep(1)

        #Clicking Join 
        print('Lets Go!')
        joinButtonX=accessCoods('joinXCoordinate.txt')  
        joinButtonY=accessCoods('joinYCoordinate.txt')
        pyautogui.moveTo(joinButtonX,joinButtonY)
        pyautogui.click()
        
        time.sleep(7)

        keyboard.write(str(int(df_new.iloc[0,2])))
        print("There you go, the password!")
        pyautogui.click()
        time.sleep(10) #So that it can only have the capacity to run once in that minute.
   
 #Too much iteration to use this!   
    # cntd = input('Do you want to Rejoin? y/n')
    # if cntd=='y':
    #     coreFunc(initalsPlease)
    # else:
    #     pass

    #All the TODOS, any additional features, will have to be coded here.
