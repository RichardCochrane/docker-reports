# Docker Reports

Reports repository for testing the Docker implementations.

This service has two main API endpoints:
- /api/update: takes a update to number of exercises in one of two subjects: maths or science
- /api/stats: returns a total number of exercises as well as total per subject

## Installation (local development)

1. `virtualenv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `FLASK_APP=run.py flask run --host=0.0.0.0 --port=5656`

## Installation (docker)

1. Ensure that docker server is installed
2. Build image: `docker image build -t d_reports .`
3. Run container as part of network of Docker Main project: `docker container run -it -p 5656:5656 -e FLASK_APP=run.py --rm --name docker_reports --network d_test d_reports`
