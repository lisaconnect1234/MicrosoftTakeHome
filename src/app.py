import json
from flask import Flask
from flask import request
from multiprocessing import context
from closest import *

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Microsoft!"

#This API endpoint will allow a user to enter thier latitude and longitude in the query string. 
#The API will return a JSON array with the five closest food trucks.
@app.route("/api/closest")
def closest():
    #Read query string
    if request.args:
        args = request.args
        if "lat" in args:
            try:
                lat = float(args["lat"])
            except ValueError:
                return "Latitude is not numeric.",200
        else:
            return "Latitude does not exist in input parameter.",200
        if "lon" in args:
            try:
                lon = float(args["lon"])
            except ValueError:
                return "Longitude is not numeric.",200
        else:
            return "Longitude does not exist in input parameter.",200
        if "numTrucks" in args:
                try:
                    numTrucks = int(args["numTrucks"])
                except ValueError:
                    return "Number of Trucks is not numeric.",200
        else:
            numTrucks = 5    
        #Call closest.findCloset to retrieve the closest 5 food trucks        
        closestLocations = findClosest(float(lat),float(lon), numTrucks)
        
        return closestLocations
    else:
        return "No Latitude and Longitude received",200

 