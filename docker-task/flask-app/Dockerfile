# Use Python base image
FROM python:slim

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app files
COPY . .

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
