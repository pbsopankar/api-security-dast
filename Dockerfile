# Dockerfile for DAST Application

# Use Python 3.11 base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files
COPY . .

# Command to run the application
CMD [ "python", "app.py" ]