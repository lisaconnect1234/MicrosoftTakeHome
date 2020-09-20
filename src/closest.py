import json
import array
#import numpy as np
from haversine import *
 
def findClosest(inLat,inLon):
    #Open the file in read mode that contains the food truck data in the area and load it into a python array 
    with open('SanFranciscoFoodTrucks.json', 'r') as j:
        json_data = json.load(j)

    #Iterate through food truck json file and calculate the distance from the input latitude and longitude.
    #Store the distance and the food trucks in an array.
    distList = []
    for i in json_data['data']:
        #Use the haversine formula to compute the distance
        dist = haversine(inLat,inLon, i["Latitude"],i["Longitude"])
        distList.append([dist,i["Applicant"],i["LocationDescription"],i["Latitude"],i["Longitude"],i["locationid"]])

    #Set the distance as the key to store on
    def sortFirst(val): 
        return val[0]  

    #Store the distance in the array, so the closest is at the top
    distList.sort(key=sortFirst)
    
    #Add the 5 closest food trucks to an array
    x = 0
    closest = [];
    while (x < 5):
        closest.append(distList[x])
        x += 1
       
    #Return the 5 closest food trucks in the json array    
    return json.dumps(closest)


    