# Use an official Python runtime as a parent image
FROM python:3.7-alpine

# setup timezone
ENV TZ=Europe/Zurich
RUN apk add tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set the working directory to /app
WORKDIR /app

# Copy and install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Define default environment variable
ENV NAME World

# Command which is executed when docker run is executed
CMD ["python", "app.py"]