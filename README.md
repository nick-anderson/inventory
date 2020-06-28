
## Case Study for Inventory Managedment
``` bash
├── ...
├── app                    # Documentation files (alternatively `doc`)
│   ├── app.py             # Hosts the flask app API
│   ├── Dockerfile         # Image rebuilt on public python image and adding in app.py
│   ├── requirements.txt   # Overkill, but if more packages are needed this is cleaner from build
│   └── ...                
├── db                     
│   ├── init.sql           # Ad-hoc SQL queries to get DB/Tables and dummy data inserted
│   └── ...                
│── run.sh                 # Kicks off docker compose build and deploy - Nice to have for testing
│── docker-compose.yml     # 2-Container deployment of mysql and flask app
│── unit_testing.py        # Python Script to try various curl commands for POST/GET
└──
```

docker build -t flaskapp:v1 .
