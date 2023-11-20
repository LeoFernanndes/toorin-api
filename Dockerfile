# app/Dockerfile

# Get the python image
FROM python:3.9

# Set the working directory for the container
WORKDIR /app

# Installing system utilities
RUN apt-get update && apt-get install -y \
    curl apt-utils

# Copy the requirements
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files and directories
COPY . /app

CMD gunicorn --bind 0.0.0.0:8000 setup.wsgi --workers 5 --timeout 120