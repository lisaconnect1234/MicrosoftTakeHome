import json
from flask import Flask
from flask import request
from multiprocessing import context
from closest import *
from flask_caching import Cache

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "simple", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)

#Setup cacheing for the Flask app to cache the food truck data
app.config.from_mapping(config)
cache = Cache(app)

def read_data():
    #Open the file in read mode that contains the food truck data in the area and load it into a python array 
    with open('SanFranciscoFoodTrucks.json', 'r') as j:
        json_data = json.load(j)
        cache.set("data",json_data)
        return json_data
    
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
            
        #Get food truck data from cache if exists, else read the food truck data and set the cache 
        json_data = cache.get("data")
        if (json_data == None):
            json_data = read_data()
             
        #Call closest.findCloset to retrieve the closest food trucks        
        closestLocations = findClosest(float(lat),float(lon), numTrucks,json_data)
        
        return closestLocations
    else:
        return "No Latitude and Longitude received",200

 