# MicrosoftTakeHome
This repository contains an API that returns a JSON object of the nearest food trucks in San Francisco based on the input latitude and longitude. 

API
base: "/${dev}/api" 
paths:
    /closest
        get:
            consumes:
            - "application/json"
            parameters:
            - in: "queryString"
                name: "lat"
                  description: "The latitude coordinate where the user is located."
                name: "lon"
                  description: "The longitude coordinate where the user is located."
                name: "numTrucks"
                description: "The number of clostes trucks to return (defaults to 5 if not present)."
            responses:
                - ouput: json
                  description: JSON array containing Distance, Applicant, Location Description, Latitude, Longitude, locationId 
                -return codes:
                  "200":
                    description: "Success"
                  "500":
                    description: "Query string is invalid. For example, the Latitude or Longitude does not exist in input parameter, is not numeric, or does not exist."
                  "403":
                    description: "Forbidden"
            security:
            - none

##Installation instructions:
- Python 3.X
- run install -r requirements.txt to import Flask, Flask-Caching and JSON
- you must have app.py, closest.py and haversine.py python code deployed
  - app.py is the flask api endpoint
  - closest.py reads the data and performs the logic to determine the file closest trucks
  - haversine.py has the calculation to determine the distance between 2 coordinates
- SanFranciscoFoodTrucks.json data must be in the directory, this includes the food trucks in San Franciso
