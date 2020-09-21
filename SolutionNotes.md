# MicrosoftTakeHome
Take home project

Solution Design Consideration

- For the take home project I created an API that allows latitude, longitude and requested number of closest food trucks as input, and returns a JSON array that contains the closest food trucks based on the number of trucks requested.  If number of trucks is not requested, then the value defaults to five.

- I decided to use Python language for this project, because I thought it would be a good fit for performing the distance calculations needed for this project.   Some of the code at my curent job is in Python and the language efficiently peforms calculations.  Also, I am interested in learning Python.  I chose to use Flask WSGI Web application framework to create the api, since it is a lightweight framework with the ability to scale up to complex applications.  I added Flask-Caching to cache the data file.

 - I used Visual Studio Code IDE and Python Flask debugger for unit testing. 

- One of the first things I did was research what formula to use to find the closest coordinates to the input latitude and longitude. I found the haversine algoritm was a recommended algorithm.  

Following are some enhancements I would do if I had more time and for production deployment:

  - Investigate performance enhancements, such as:
  
    - Split the truck data into areas, inorder to limit the amount of data the haversine algorithm is run with.

     - I used the python built in list to store and sort the data retrieved from the input file.  As a performance enhancement, I would look into using the array and numpy lists, since they are predefined and more efficient. 
    
  - For production, I would refactor Flask-Caching to use Reddis because SimpleCache cache type is not thread safe.

  - Investigate a map cloud service to retrieving map data, handle the distance calculation, as well as visualizations for displaying the coordinates on a map. When the data layer becomes more complex, I would create a DAO and entity objects to handle the data layer. 

  - Create a web UI map visualization that allows the user to search for the closest food trucks based on their current location or entered coordinates.  The UI would call this api and then display on a map the closest five locations returned.
  
  - Create automated tests that execute in the CI/CD pipeline.  
  
  - Setup OpenAPI to document the endpoints for the project.  
  
  - I would deploy in a cloud environment and create Terraform scripts to setup the environment. 
