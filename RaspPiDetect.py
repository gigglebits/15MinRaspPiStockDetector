import requests
import time
from pushbullet import PushBullet
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def Main():
    while True:
        breaker = checkSite()
        if breaker == 0:
            time.sleep(60)
        else:
            sendNotification()
            time.sleep(900)


def sendNotification():
    token = "o.xVUJ34fxvGkw40mcZ4S3T6yRdOFAyBP4"
    data = 'RaspPi at Microcenter'
    text = "Your script just found that there was a Raspberry Pi at the Overland Park Microcenter."

    pb = PushBullet(token)
    push = pb.push_note(data,text)
    put_success("Message Sent")
    

def checkSite():
    #Set URL
    url = 'https://www.microcenter.com/product/621439/-?storeid=191'

    #Perform request and store result in data var. 
    data = requests.get(url)

    #Set what we're looking for.
    search="SOLD OUT"

    #Check if the search string is in the response text. 
    if search in data.text:
        print("Not Yet")
        return 0
    else:
        print("Try Now")
        return 1

#print(data.text)
Main()
