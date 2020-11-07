import pyperclip 

def meetCodeGiver(argument):    #PROCESSING
    switcher = { 
        "SV": 7931380267, 
        "JP": 7644991204, 
        "STP": 9257726874, 
        "SNK": 4302909682, 
        "AH":  4691762381, 
        "DCK": 5239834372, 
        "BS": 71616553872, 
        "VV": 7415289636, 
        "SKG": 9280360715, 
        "PB": 8938976636, 
        "SP": 4699455972,   
        "TP": 8469906757, 
        "SS": 9875924847, 
        "KNC": 5349366922,
        "UD": 8966028553, 
        "VRL": 6644191114, 
        "SH": 8234694854, 
        "VR": 8376828015,  
        "GS": 6507378241,
        "KGR": 9100203254, 
        "RS": 76154545722, 
       } #Table Complete 
  
    # get() method of dictionary data type returns  
    # value of passed argument if it is present  
    # in dictionary otherwise second argument will 
    # be assigned as default value of passed argument 
    return switcher.get(argument, "Didn't find a match. Check the Inital Again Maybe?") 


