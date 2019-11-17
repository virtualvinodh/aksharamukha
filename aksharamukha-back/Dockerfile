# our base image
FROM python:3.6-slim

RUN pip3 install gunicorn

# Copy python files
ADD . / /usr/backend/

# install requirements
WORKDIR /usr/backend/
RUN pip install -r requirements.txt
RUN pip install aksharamukha

# tell the port number the container should expose
EXPOSE 8085

# run the application
WORKDIR /usr/backend/
CMD ["gunicorn", "--bind", "0.0.0.0:8085", "main:app"]

