# Use lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies first (faster rebuilds)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY app.py .

# Run app
CMD ["python", "app.py"]
