# Use a minimal Python 3.11 image as the base
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY app/requirements.txt .

# Install Python dependencies without caching to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder into the container
COPY app/ .

# Command to start the FastAPI server when the container runs
# --host 0.0.0.0 makes it accessible from outside the container
# --port 8000 sets the port for the API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
