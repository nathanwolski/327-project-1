# Use an official Python runtime as the base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME broadcast-sender

# Run broadcast_publisher.py when the container launches
CMD ["python3", "broadcast_publisher.py"]
