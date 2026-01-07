import requests
import json

while True:

    callsign = input("Enter Callsign: <q> to QUIT <b> to do BULK  >> ").upper()
    
    if callsign == "Q" :
        break

    database = input("Enter database (<c> for callook.info, <d> for HamDB) >>").upper()

    if database == "C":
        api_url = f"https://callook.info/{callsign}/json"
        path = ["","location", "gridsquare"]
        try:
            response = requests.get(api_url)
            grid = response.json()[path[1]][path[2]]
            print (f"{callsign} GRID is {grid}")
        except:
            print (f"CALLSIGN {callsign} INVALID  <q> to QUIT")
    if database == "D":
        api_url = f"https://api.hamdb.org/v1/{callsign}/json/"
        path = ["hamdb","callsign", "grid"]
        try:
            response = requests.get(api_url)
            grid = response.json()[path[0]][path[1]][path[2]]
            print (f"{callsign} GRID is {grid}")
        except:
            print (f"CALLSIGN {callsign} INVALID  <q> to QUIT")