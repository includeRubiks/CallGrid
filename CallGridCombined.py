import requests
import json

while True:

    callsign = input("Enter Callsign: <q> to QUIT <b> to do BULK  >> ").upper()
    
    if callsign == "Q" :
        break

    if callsign == "B" :
        bulk = True
        bulkfile = input("Path to file with callsigns >> ")
        try:
            with open(bulkfile) as file:
                callsigns = [s.replace("\n", "") for s in file.readlines()]
        except:
            print(f"PATH {bulkfile} INVALID. Quitting...")
            break
        database = input("Enter database (<c> for callook.info, <d> for HamDB) >>").upper()
        if database == "C":
            for call in callsigns:
                try:
                    response = requests.get(f"https://callook.info/{call}/json")
                    grid = response.json()["location"]["gridsquare"]
                    print (f"{call} GRID is {grid}")
                except:
                    print (f"CALLSIGN {call} INVALID. Quitting...")
        if database == "D":
            for call in callsigns:
                try:
                    response = requests.get(f"https://api.hamdb.org/v1/{call}/json/")
                    grid = response.json()["hamdb"]["callsign"]["grid"]
                    print (f"{call} GRID is {grid}")
                except:
                    print (f"CALLSIGN {call} INVALID. Quitting...")
        
    if bulk == False:
            database = input("Enter database (<c> for callook.info, <d> for HamDB) >>").upper()

            if database == "C":
                path = ["","location", "gridsquare"]
                try:
                    response = requests.get(f"https://callook.info/{call}/json")
                    grid = response.json()[path[1]][path[2]]
                    print (f"{callsign} GRID is {grid}")
                except:
                    print (f"CALLSIGN {callsign} INVALID. Quitting...")
                    break
            if database == "D":
                path = ["hamdb","callsign", "grid"]
                try:
                    response = requests.get(f"https://api.hamdb.org/v1/{call}/json/")
                    grid = response.json()[path[0]][path[1]][path[2]]
                    print (f"{callsign} GRID is {grid}")
                except:
                    print (f"CALLSIGN {callsign} INVALID. Quitting...")
                    break