# Use a slim Python 3.11 base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file to the working directory
COPY requirements.txt ./
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from current directory to container
COPY . .

# Expose port 5000 for the application
EXPOSE 5000

# Run app.py with Python when the container starts
CMD ["python", "app.py"]