FROM codingforentrepreneurs/python:3.9-webapp-cassandra

COPY ./reviews  /reviews/reviews
COPY ./req.txt  /reviews/req.txt
COPY .env  /reviews/.env
COPY ./entrypoint.sh  /reviews/entrypoint.sh
COPY ./exports /reviews/models
COPY ./pipelines /reviews/pipelines/

WORKDIR /reviews

RUN chmod +x entrypoint.sh

RUN python3 -m venv /opt/venv && /opt/venv/bin/python -m pip install -r req.txt

CMD [ "entrypoint.sh" ]
 
