# Slim base image (Debian 12 Bookworm)
FROM python:3.13-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=UTC

# Set working directory
WORKDIR /assessment

# Copy requirements first to leverage Docker cache
COPY ./requirements.txt .

# Install dependencies and clean up
RUN apt-get update && \
    apt-get install -y --no-install-recommends && \
    apt-get clean && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run Uvicorn with single worker for synchronous endpoints
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4", "--no-server-header"]