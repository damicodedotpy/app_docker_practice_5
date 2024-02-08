This aplication has a single endpoint ("/users) and it immediately saves a user entry into the
postgresql database.

Setup instructions:

1. Run Docker host by opening Docker desktop app
2. Create an image from the 'dockerfile' inside the repo --> docker build -t 'any name' .
3. Create a container based on the previous image --> 
docker run -p 5000:5000 -e POSTGRES_DATABASE_PASSWORD=passwordValue -e POSTGRES_DATABASE_NAME=databaseName--name 'any name' 'image name'
4. Make the http request to the ip address printed and the route "/users"

NOTE: Before connectig to the database you need to create a database on your local system, after that
you must provide that value on the command and its regarding passwrod. The value of the environment varibale in the docker run command must be the ones of your postgresql database previously created.