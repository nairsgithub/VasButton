#VASTAUINE VasButton Program version-1
#MAKE SURE YOU HAVE ALL THESE LIBRARY

#sudo pip install retrying
#sudo pip install requests

# Change Your ID and Password.if you don't have one get at http://vastauine.com/signup

#LIBRARY
from retrying import retry
import requests,datetime,time,re,json

#META DATA
url="http://vastauine.com/VASAPI.php"

#Change This Field
MYUSR='YOUR-Vastauine-ID'
MYPASS='YOUR-Vastauine-PASSWORD'

#START MESSAGE
print("STARTED..", datetime.datetime.now().time())

@retry   
def PiUpdate(pin,state):        
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,state)
    

@retry
def Change(MYUSR,MYPASS,LastChange):    
        r=requests.post(url, data={'USERNAME' : MYUSR,'PASSWORD' : MYPASS, 'CHANGE' :'CHANGE'})
                  
        CHANGE=(json.loads(r.text.strip()))   
        if LastChange == CHANGE :            
            return [True,LastChange]
        else:
            LastChange=CHANGE            
            return [False,LastChange]
            
@retry
def Update(MYUSR,MYPASS):    
        r=requests.post(url, data={'USERNAME' : MYUSR,'PASSWORD' : MYPASS, 'GPIO' :'ALL'})   
        Save=(json.loads(r.text.strip()))
        for i in Save:
            pin=int(re.sub("[^0-9]", "",i))            
            state=int(Save[i])           
            PiUpdate(pin,state)
        
       
LastChange=0      
while True:
    var=Change(MYUSR,MYPASS,LastChange)
    LastChange=var[1]
 
    if (var[0] == False):        
        Update(MYUSR,MYPASS)        
    elif (var[0] == True):
        time.sleep(0.5)
    else:
        print('Unknown#ERR')
        


