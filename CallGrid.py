#CAll grid grabber

#!/usr/bin/python3


import requests
import json

callsign = ""

while True:

    callsign = input("Enter Callsign: <q> to QUIT  >> ").upper()
    
    if callsign == "Q" :
        break

    else:
        try:
            api_url = f"https://callook.info/{callsign}/json"
            response = requests.get(api_url)
            location = response.json()["location"]
            grid = location["gridsquare"]
            print (f"{callsign} GRID is {grid}")
            
        except:
            print (f"CALLSIGN {callsign} INVALID  <q> to QUIT")
