# Use the official Python base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose port
EXPOSE 10000

# Run the API using uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "10000"]
