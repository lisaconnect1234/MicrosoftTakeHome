# MicrosoftTakeHome
Take home project

Solution Design Consideration

I created an API for this project, that reads the query string containing latitude and longitue.  The API returns an JSON array that contains the 5 closest food trucks.

I am using Python in this project, since I have want to learn Python some more and have been learning Python for a project at my current job.   I chose to use Flask WSGI Web application framework, since it is a lightweight framework with the ability to scale up to complex applications.  

One of the first things I did was research what formula to use to find the distance.  I looked for possible open source application to perform the calculation.  I decided to code the calculation in a separate function to call.  For the production application I would of investigated a cloud service that handle the calculation, as well as visualizations for displaying the coordinates on a Sanfrancisco map.  

Another thing I would of added in the production application is a caching mechanism for the data being read in, versus open the json file on every call.  Flask does not handle caching standalone.  I tried importing Flask_cache, but it would not import with the version of Python I was using.  I would use Redis or another caching mechanism.  Another performance enhancement I would do in production is split the truck data into areas, inorder to limit the amount of data the haversine algorithm is run with.  

I used Visual Studio Code and the Flask debugger for unit testing.  For deployment, I would create automated tests that execute in the CI/CD pipeline.  I would also use OpenAPI to document the endpoints for the project.  I would deploy in a cloud environment and create Terraform scripts to setup the environment. 


Documentation for using the API: 
http://127.0.0.1:5000/api/closest?lat=37.7791572053411&lon=-122.411615430519
