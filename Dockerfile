# Use an official Python 3.11 image
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (for numpy, pandas, etc.)
RUN apt-get update && apt-get install -y build-essential

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

# Copy the rest of your code
COPY . .

# Expose port (will be overridden by environment variable)
EXPOSE $PORT

# Start the API with dynamic port
CMD uvicorn main:app --host 0.0.0.0 --port $PORT
