# DCE-Semestralka_1-Backend
Simple Python Web Server
It was created for the purposes of the KIV/DCE course at the University of West Bohemia. 

## Function
This web server returns a web page containing the server's IP address.

## Usage
The backend can be used as a package published on Github Container 

Registry available at: `ghcr.io/zdenekvavricka/dce-semestralka_1-backend:latest`

### Running the backend locally
It is also possible to run the backend locally using Docker by running the following commands in the project root directory:

Build the image: `docker build -t dce-simplest-backend .`

Run the container: `docker run -d -p 5000:5000 dce-simplest-backend`
