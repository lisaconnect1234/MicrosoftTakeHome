import json
#import array as arr
#import numpy as np
from haversine import *


def read_data(cache):
    #Open the file in read mode that contains the food truck data in the area and load it into a python array and cache
    with open('SanFranciscoFoodTrucks.json', 'r') as j:
        json_data = json.load(j)
        cache.set("data",json_data)
        return json_data
    
def findClosest(inLat,inLon,numTrucks,cache):
    #Get food truck data from cache if exists, else read the food truck data and set the cache 
    json_data = cache.get("data")
    if (json_data == None):
        json_data = read_data(cache)
            
    #Iterate through food truck json file and calculate the distance from the input latitude and longitude.
    #Store the distance and the food trucks in an array.
    #For production, look into using array and numpy array for handling arrays, since they are quicker due to preallocation of memory. 
    distList = []
    for i in json_data['data']:
        #Use the haversine formula to compute the distance
        dist = haversine(inLat,inLon, i["Latitude"],i["Longitude"])
        distList.append([dist,i["Applicant"],i["LocationDescription"],i["Latitude"],i["Longitude"],i["locationid"]])
    
    #Set the distance as the key to store on
    def sortDist(val): 
        return val[0]  

    #Store the distance in the array, so the closest is at the top
    distList.sort(key=sortDist)
    
    #Add the numTrucks closest food trucks to an array
    x = 0
    closest = [];
    while (x < numTrucks):
        closest.append(distList[x])
        x += 1
       
    #Return the numTrucks closest food trucks in the json array    
    return json.dumps(closest)


    
