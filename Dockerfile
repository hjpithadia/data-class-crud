# Use a base image with Python preinstalled
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the entire project directory to the container
COPY . .

# Install python-dotenv for loading environment variables from .env file
RUN pip install python-dotenv

# Set the command to load environment variables from .env file
CMD ["python", "-m", "dotenv", "run", "--", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
