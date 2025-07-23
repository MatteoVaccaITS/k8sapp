FROM python:3.11-slim           # Use a slim Python 3.11 base image

WORKDIR /app                    # Set working directory inside the container

COPY requirements.txt ./        # Copy requirements file to the working directory
RUN pip install --no-cache-dir -r requirements.txt  # Install Python dependencies

COPY . .                        # Copy all files from current directory to container

EXPOSE 5000                    # Expose port 5000 for the application

CMD ["python", "app.py"]        # Run app.py with Python when the container starts