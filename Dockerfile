FROM alpine:latest

#  Installing python and pip
RUN apk add --no-cache python3 py3-pip

#  Copying all files to working directory called app
WORKDIR /app
COPY . /app

#  Installing requirements from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#  Opening ports Flask=5000 Redis=6379
EXPOSE 5000 6379

#  Running the app
CMD ["python3", "app.py"]