# Use the official Python 3.11 image as a base image
FROM python:3.11.5-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
# EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app-py
ENV FLASK_RUN_HOST=0.0.0.0

# Use gunicorn as the entry-point, replace 'app:app' with 'yourmodule:yourapp' if necessary
#CD ""gunicorr、"ーが，"：5000， "app:app"］
CMD gunicorn -b 0.0.0.0:$PORT app:app