
# Case Study for Inventory Managedment
``` bash
├── app                    # Directory to host the building of Flask container
│   ├── app.py             # Hosts the flask app API on port 5000
│   ├── Dockerfile         # Image rebuilt on public python image and adding in app.py
│   ├── requirements.txt   # Overkill, but if more packages are needed this is cleaner from build aspect
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

This was my first time doing a multi-container application with Docker-Compose that work together, generally I've been working in the k8 and multi-container in same pod space. The setup is very familiar and uses similar YAML formatting but for this application you just need to run MYSQL container that I pulled from Dockerhub mysql:5.7 and custom built flask image on respective 3307/5000 ports. Docker compose has ability to build images on fly rather than using ```bash docker build -t flaskapp:v1 . ``` \

The run.sh command invokes a build and redeploy and doesn't cache so when adding additional functionality to flask app, you aren't stuck debugging for a redeployment that didn't pick up local change: ```bash docker-compose build && docker-compose up ```
