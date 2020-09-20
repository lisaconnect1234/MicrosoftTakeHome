# MicrosoftTakeHome
Take home project

Solution Design Consideration

I created an API for this project, that reads the query string containing latitude and longitue.  The API returns an JSON array that contains the 5 closest food trucks.


API: /api/closest?lat=x&lon=x&numTrucks  (note: numTrucks is optional, defaults to 5)
Returns JSON: Distance, Applicant, Location Description, Latitude, Longitude, locationId 
For production, I would create swagger documentation for the apis.  I would also ask the customer what documentation method they are currently using.

For production, this api can be used by mobile app and web UI map visualizations that allow the user to search for the closest food trucks based on their current location or entered coorinates.  The app will call the api and then display on a map the closest five locations.

I decided to use Python language for this project, since I am interested in learning Python.  Some of the code at my curent job is in Python and the language efficiently peforms calculations.  Also, I thought it would be a good fit for performing the distance calculations needed for this project.  I chose to use Flask WSGI Web application framework to create the api, since it is a lightweight framework with the ability to scale up to complex applications.  

One of the first things I did was research what formula to use to find the closest food trucks to the input latitude and longitude. I found the haversine algoritm was a recommended algorithm.  I looked for possible open source application to perform the calculation.  I decided to code the calculation in a separate function to call.  Later I did find a haversine import I could use for production. For the production application I would of investigated a cloud service that handle the calculation, as well as visualizations for displaying the coordinates on a Sanfrancisco map.  

Another thing I would of added in the production application is a caching mechanism such as Redis for the data being read in, versus open the json file on every call.  Flask does not handle caching standalone.  I tried importing Flask_cache, but it would not import with the version of Python I was using. Another performance enhancement I would do in production is split the truck data into areas, inorder to limit the amount of data the haversine algorithm is run with.

I used the python built in list to store and sort the data retrieved from the input file.  For production, I would look into using the array and numpy lists, since they are predefined and more efficient. 

I used Visual Studio Code and the Flask debugger for unit testing.  For deployment, I would create automated tests that execute in the CI/CD pipeline.  I would also use OpenAPI to document the endpoints for the project.  I would deploy in a cloud environment and create Terraform scripts to setup the environment. 

