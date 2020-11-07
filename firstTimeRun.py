import globalVars

def runFirstTimeStuff(): 

    print('Good Morning, Please Enter the Initial of the Teachers, in Order:  ')
    globalVars.x1 = input('1st teacher: ')  # INPUT
    globalVars.x1 = globalVars.x1.upper()

    globalVars.x2 = input('2nd teacher: ')  # INPUT
    globalVars.x2 = globalVars.x2.upper()

    globalVars.x3 = input('3rd teacher: ')  # INPUT
    globalVars.x3 = globalVars.x3.upper()

    globalVars.x4 = input('4th teacher: ')  # INPUT
    globalVars.x4 = globalVars.x4.upper()

    globalVars.x5 = input('5th teacher: ')  # INPUT
    globalVars.x5 = globalVars.x5.upper()

    print('Great! I goddit. Just use numbers from now on in the day!')
    print('Also, If you forget the order, just say -lt and I will help!')