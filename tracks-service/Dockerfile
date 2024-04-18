FROM python:3.11

WORKDIR /app

COPY ./tracks-service/requirements.txt /app/requirements.txt
RUN pip install --upgrade -r requirements.txt

COPY ./tracks-service/ /app/

