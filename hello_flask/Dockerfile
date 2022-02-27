# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen to port 5000
EXPOSE 5000/tcp

# working directory
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["python","./app.py"]

