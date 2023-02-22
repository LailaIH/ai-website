FROM codingforentrepreneurs/python:3.9-webapp-cassandra

COPY ./reviews  /reviews/reviews
COPY ./req.txt  /reviews/req.txt

WORKDIR /reviews

RUN python3 -m venv /opt/venv && /opt/venv/bin/python -m pip install -r req.txt
 
