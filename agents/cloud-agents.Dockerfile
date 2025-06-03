FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy only what you need
COPY agents/ ./agents/
COPY config/.env ./config/.env
COPY requirements.txt ./requirements.txt

# Install deps
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python3"]
