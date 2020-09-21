# MicrosoftTakeHome
This API returns a JSON object of the nearest food trucks in San Francisco based on the input latitude and longitude. 

The API reads the query string containing the user's latitude,longitude and the number of food trucks they want returned.  The API returns an JSON array that contains the 5 closest food trucks.

- API: /api/closest?lat=x&lon=x&numTrucks  (note: numTrucks is optional, defaults to 5)
Returns JSON: Distance, Applicant, Location Description, Latitude, Longitude, locationId 

Installation instructions:
- run install -r requirements.txt to import Flask and JSON
- you must have app.py, closest.py and haversine.py python code
- SanFranciscoFoodTrucks.json data must be in the directory, this include the food trucks in San Franciso
