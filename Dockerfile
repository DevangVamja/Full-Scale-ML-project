# Use an official Python image as a base
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY . /app
RUN apt update && apt install awscli -y
RUN pip install --no-cache-dir -r requirements.txt


# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["Python3","app.py"]
