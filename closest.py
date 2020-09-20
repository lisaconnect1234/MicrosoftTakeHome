import json
import array
#import numpy as np
from haversine import *
#from math import radians, cos, sin, asin, sqrt
 
#inLat = 37.7791572053411
#inLong = -122.411615430519

# "locationid": 1163794,
#        "Applicant": "SOHOMEI, LLC",
#"Latitude": 37.7791572053411,
#        "Longitude": -122.411615430519,

def findClosest(inLat,inLon):
    with open('csvjson2.json', 'r') as j:
        json_data = json.load(j)

    distList = []
    for i in json_data['data']:
        dist = haversine(inLat,inLon, i["Latitude"],i["Longitude"])
        distList.append([dist,i["Applicant"],i["LocationDescription"],i["locationid"]])

    def sortFirst(val): 
        return val[0]  

    distList.sort(key=sortFirst)
    x = 0
    closest = [];
    while (x < 5):
        closest.append(distList[x])
        #print(distList[x])
        x += 1
       
    #print(json.dumps(closest))    
    return json.dumps(closest)


    
