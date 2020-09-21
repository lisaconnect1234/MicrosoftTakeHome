# MicrosoftTakeHome
This API returns a JSON object of the nearest food trucks in San Francisco based on the input latitude and longitude. 

- API: /api/closest?lat=x&lon=x&numTrucks  
  - query string inputs: 
    - lat = latitude
    - lon = longitude
    - numTrucks - number of clostes trucks to return (defaults to 5 if not present).
  - output JSON array: Distance, Applicant, Location Description, Latitude, Longitude, locationId 

Installation instructions:
- run install -r requirements.txt to import Flask, Flask-Caching and JSON
- you must have app.py, closest.py and haversine.py python code deployed
  - app.py is the flask api endpoint
  - closest.py reads the data and performs the logic to determine the file closest trucks
  - haversine.py has the calculation to determine the distance between 2 coordinates
- SanFranciscoFoodTrucks.json data must be in the directory, this includes the food trucks in San Franciso
