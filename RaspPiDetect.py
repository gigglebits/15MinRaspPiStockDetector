import requests
import time

#need to install pushbullet with pip install pushbullet.py
from pushbullet import PushBullet
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def Main():
    #Set URL
    url_2gb = 'https://www.microcenter.com/product/621439/-?storeid=191'
    url_4gb = 'https://www.microcenter.com/product/637834/raspberry-pi-4-model-b-4gb-ddr4?storeid=191'
    url_8gb = 'https://www.microcenter.com/product/622539/raspberry-pi-4-model-b-8gb-ddr4?storeid=191'

    #Set counter to break the loop if it's sent me 10 or more notifications. 
    counter = 0

    #Infinite loop to check for raspberry Pis.
    while counter < 11:
        if checkSite(url_2gb):
            sendNotification("2GB")
            counter += 1
            time.sleep(900)
        elif checkSite(url_4gb):
            sendNotification("4GB")
            counter += 1
            time.sleep(900)
        elif checkSite(url_8gb):
            sendNotification("8GB")
            counter += 1
            time.sleep(900)
        else:
            time.sleep(15)
        



def sendNotification(mem_config):
    token = "o.xVUJ34fxvGkw40mcZ4S3T6yRdOFAyBP4"
    data = f'{mem_config} RaspPi at Microcenter'
    text = f"Your script just found that there was a {mem_config} Raspberry Pi at the Overland Park Microcenter."

    pb = PushBullet(token)
    push = pb.push_note(data,text)
    put_success("Message Sent")
    

def checkSite(url):
    #Perform request and store result in data var. 
    data = requests.get(url)

    #Set what we're looking for.
    search="SOLD OUT"

    #Check if the search string is in the response text. 
    if search in data.text:
        print("Not Yet")
        return False
    else:
        print("Try Now")
        return True

#print(data.text)
Main()
