import json
from flask import Flask
from flask import request
from multiprocessing import context
from closest import *
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/api/closest")
def closest():
    if request.args:
        args = request.args
        if "lat" in args:
            try:
                lat = float(args["lat"])
            except ValueError:
                return "Latitude not numeric.",200
        else:
            return "Latitude does not exist in input parameter.",200
        if "lon" in args:
            try:
                lon = float(args["lon"])
            except ValueError:
                return "Longitude not numeric.",200
                
        closetLocations = findClosest(float(lat),float(lon))
        return closetLocations
    else:
        return "No Latitude and Longitude received",200

 