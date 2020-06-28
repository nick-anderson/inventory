
# Case Study for Inventory Management
``` bash
├── app                    # Directory to host the building of Flask container
│   ├── app.py             # Hosts the flask app API on port 5000
│   ├── Dockerfile         # Image rebuilt on public python image and adding in app.py
│   ├── requirements.txt   # Overkill, but if more packages are needed this is cleaner
│   └── ...                
├── db                     # Directory to host SQL files
│   ├── init.sql           # Ad-hoc SQL queries to get DB/Tables and dummy data inserted
│   └── ...                
│── run.sh                 # Kicks off docker compose build and deploy - Nice to have for testing
│── docker-compose.yml     # 2-Container deployment of mysql and flask app
│── unit_testing.py        # Python Script to try various curl commands for POST/GET
└──
```

## Building flask application with Docker

This was my first time doing a multi-container application with Docker-Compose that work together, generally I've been working in the k8 and multi-container in same pod space. The setup is very familiar and uses similar YAML formatting but for this application you just need to run MYSQL container that I pulled from Dockerhub mysql:5.7 and custom built flask image on respective 3307/5000 ports. Docker compose has ability to build images on fly rather than using ```docker build -t flaskapp:v1 . ``` \

The run.sh command invokes a build and redeploy and doesn't cache so when adding additional functionality to flask app, you aren't stuck debugging for a redeployment that didn't pick up local change: ```docker-compose build && docker-compose up ```\

## Docker compose networking and Volume mounts

For this application, I'm just running it local so the docker volume claim lives as long as I don't run ```docker-compose down```. For Kubernetes deployment using a storage class like AWS EFS where it uses NFS protocol, so that multiple pods can mount the same volume and use shared same space is very useful. For this application that's not needed as the Flask API is submitting queries to MySQL container. Exposing the port from containers, in this case just default but can always change client side port if there is a pre-existing application blocking it.\

## API functionality

In the provided directory there is a unit_testing.py that casts curl commands using python's OS library. These strings were generated from postman and can be invoked in a lot of different ways
