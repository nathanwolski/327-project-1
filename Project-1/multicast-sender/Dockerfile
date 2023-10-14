# Use an official Python runtime as the base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME multicast-sender

# Run multicast_sender.py when the container launches
CMD ["python3", "multicast_sender.py"]
