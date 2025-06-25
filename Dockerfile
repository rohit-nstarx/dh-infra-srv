FROM python:3.10-slim

# Set working directory
WORKDIR /dh-infra

# Set environment variable for protobuf
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Install dependencies
COPY requirements/prod.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY ./app ./app

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI app via Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
