# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install requirements
RUN pip install -r requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir fastapi python-multipart uvicorn "python-jose[cryptography]"  "passlib[bcrypt]" 

# Make port 5000 available to the world outside this container
EXPOSE 8000

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]

