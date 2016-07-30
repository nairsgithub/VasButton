#LIBRARY
import requests
import datetime
import re
import time
import json

#META DATA
url="http://vastauine.com/VASAPI.php"

#START MESSAGE
MYUSR='change_USERNAME'
MYPASS='change_PASSWORD'
print("STARTED..", datetime.datetime.now().time())

#FUNCTIONS
def Write(text):
    file = open("vasButtonLog.txt", "a")
    file.write(text)
    file.close()
    
def PiUpdate(pin,state):        
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,state)
    


def Change(MYUSR,MYPASS,LastChange):
    try : 
        r=requests.post(url, data={'USERNAME' : MYUSR,'PASSWORD' : MYPASS, 'CHANGE' :'CHANGE'})
    except requests.ConnectionError as e:
        time.sleep(0.5)
        return ['CHANGE*ERR',LastChange]
    else:
        try:
            CHANGE=(json.loads(r.text.strip()))
        except ValueError as e:
            return [False,LastChange]
        else:
            if LastChange == CHANGE :
                #print(LastChange,"returning NoChange",CHANGE)
                return [True,LastChange]
            else:
                LastChange=CHANGE
                #print(LastChange,"returning Change",CHANGE)
                return [False,LastChange]

def Update(MYUSR,MYPASS):
    try : 
        r=requests.post(url, data={'USERNAME' : MYUSR,'PASSWORD' : MYPASS, 'GPIO' :'ALL'})
    except requests.ConnectionError as e:
        return 'UPDATE*ERR'
    else:
        try:
            Save=(json.loads(r.text.strip()))
        except ValueError as e:
            time.sleep(1)
        else:        
            for i in Save:
                pin=int(re.sub("[^0-9]", "",i))            
                state=int(Save[i])            
                #print(pin,type(pin),state,type(state))
                PiUpdate(pin,state)

        
LastChange=0      
while True:
    var=Change(MYUSR,MYPASS,LastChange)
    LastChange=var[1]
 
    if (var[0] == False):        
        Update(MYUSR,MYPASS)
        #print("Updated at : ",datetime.datetime.now().time())        
 
    elif (var[0] == True):
        time.sleep(0.1)
        #print("Rechecking")        
    elif (var[0] == 'CHANGE*ERR'):
        time.sleep(0.01)
    else:
        time.sleep(0.01)
       



