import json
import array
import numpy as np
from math import radians, cos, sin, asin, sqrt
#from array import *
inLat = 37.7849902793065
inLong = -122.405676629072
#"locationid": 1357615,
#        "Applicant": "FRUITYMANIA",
#       "FacilityType": "Push Cart",
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

with open('csvjson2.json', 'r') as j:
    json_data = json.load(j)
    #print(json_data)
    
#f = open('test.json',)
#data = json.load(f)
distList = []
for i in json_data['data']:
    dist = haversine(inLat,inLong, i["Latitude"],i["Longitude"])
    distList.append([dist,i["locationid"],i["Applicant"]])
    
    #np.append(distListNp,dist)
    ##closest = np.argpartition(distList, k)
    #if (first == 1):
    #    leastDist = dist
    #    first = 0
    #if (dist < leastDist):
    #    leastDist = dist
    #    name = i["Applicant"]
    #    loc = i["locationid"]
    #
def sortFirst(val): 
    return val[0]  

distList.sort(key=sortFirst)
x = 0
closest = [];
while (x < 5):
    closest.append(distList[x])
    print(distList[x])
    x += 1
    
print(json.dumps(closest))    
    #dist = test(i["Latitude"],i["Longitude"])
    #dist = test(i["Latitude"],i["Longitude"])

#print(name, loc,leastDist)


    
