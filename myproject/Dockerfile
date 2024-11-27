# Step 1: Use an official Python runtime as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Install dependencies
# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the current directory contents into the container at /app
COPY . /app/

# Step 6: Expose port 8000 (for the Django app to be accessible)
EXPOSE 8000

# Step 7: Define the environment variable for the Django settings
ENV DJANGO_SETTINGS_MODULE=pension_calculator.settings

# Step 8: Run migrations and start the Django app
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
