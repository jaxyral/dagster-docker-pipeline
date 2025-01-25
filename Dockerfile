# Use Python 3.10 as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the default command to run the Dagster webserver
CMD ["dagster", "dagit", "-h", "0.0.0.0", "-p", "3000"]
