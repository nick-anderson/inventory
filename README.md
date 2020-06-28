
## Case Study for Inventory Managedment
``` bash
├── ...
├── app                    # Documentation files (alternatively `doc`)
│   ├── app.py              # Table of contents
│   ├── Dockerfile              # Frequently asked questions
│   ├── requirements.txt             # Miscellaneous information
│   └── ...                 # etc.
├── db                    # Documentation files (alternatively `doc`)
│   ├── init.sql              # Table of contents
│   └── ...                 # etc.
│── run.sh              # Table of contents
│── docker-compose.yml              # Table of contents
│── unit_testing.py              # Table of contents
│── run.sh              # Table of contents
└── ...

docker build -t flaskapp:v1 .
The [.gitlab-ci.yml](.gitlab-ci.yml) file can be used in GitLab to build,
test, and deploy the code, as in https://gitlab.com/TrendDotFarm/docker-tutorial
For more information, read the [Docker Compose Integration to GitLab
CI](GitLab-CI.md) guide.
o
```
