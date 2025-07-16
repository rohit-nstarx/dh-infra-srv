# DH Infra Service

A monitoring service designed to track the health and status of multiple services by making HTTP requests to specified endpoints and checking for 200 OK responses.

## 🚧 Development Status

This service is currently in the **development phase** and is being actively developed for monitoring purposes.

## Overview

The DH Infra Service is a FastAPI-based monitoring solution that:
- Monitors multiple services by making HTTP requests to their health endpoints
- Tracks service status history with configurable limits
- Provides REST API endpoints to check service statuses
- Maintains an active avatar system for service personalization

## Features

- **Service Health Monitoring**: Continuously monitors registered services
- **Status History**: Maintains a rolling history of service statuses (configurable limit)
- **REST API**: Provides endpoints to query service statuses
- **Avatar Management**: Manages active avatar configurations
- **Async Operations**: Built with async/await for high performance
- **Logging**: Comprehensive logging system for debugging and monitoring

## Architecture

The service is structured with the following components:

```
app/
├── routes/
│   ├── services_router.py    # Service status endpoints
│   └── avatar_router.py      # Avatar management endpoints
├── core/
│   ├── shared.py            # Service status storage and management
│   └── logging.py           # Logging configuration
├── services/
│   └── monitoring/
│       └── monitor.py       # Monitoring service (in development)
└── config/
    └── http_client.py       # HTTP client for service requests
```

## API Endpoints

### Service Status Endpoints

#### Get All Service Statuses
```http
GET /api/v1/services/status
```

**Description**: Retrieves the current status of all monitored services.

**Response**:
```json
{
  "service_name_1": true,
  "service_name_2": false,
  "service_name_3": true
}
```

**Response Schema**:
- `service_name` (boolean): Service health status
  - `true`: Service is healthy (last 3 checks passed)
  - `false`: Service is unhealthy or insufficient check history

**Status Codes**:
- `200 OK`: Successfully retrieved service statuses

---

### Avatar Management Endpoints

#### Get Active Avatar
```http
GET /api/v1/data/avatars/active
```

**Description**: Retrieves the currently active avatar configuration.

**Response**:
```json
{
  "data": "kira"
}
```

**Response Schema**:
- `data` (string): Active avatar identifier

**Status Codes**:
- `200 OK`: Successfully retrieved active avatar
- `500 Internal Server Error`: Unable to fetch active avatar

**Error Response**:
```json
{
  "detail": "Unable to fetch active avatar"
}
```

## Service Status Logic

The service implements a sophisticated status tracking system:

### Status Determination
- **Healthy**: Service is considered healthy when the last 3 consecutive checks return `true`
- **Unhealthy**: Service is considered unhealthy if:
  - Any of the last 3 checks failed
  - Fewer than 3 checks have been performed
  - Service is not registered in the monitoring system

### Status History
- Each service maintains a rolling history of status checks
- Default history limit: 3 entries
- History is maintained using a `deque` with `maxlen=3`
- Thread-safe operations using `asyncio.Lock`

### Core Status Methods

```python
# Set service status
await ServiceStatusStore.set_status("service_name", True)

# Get specific service status
status = await ServiceStatusStore.get_status("service_name")

# Get all service statuses
all_statuses = await ServiceStatusStore.get_all_statuses()

# Check if all services are healthy
is_healthy = await ServiceStatusStore.is_everything_healthy()
```

## HTTP Client

The service includes an async HTTP client for making requests to monitored services:

### Features
- Configurable timeout settings
- GET and POST request support
- Automatic status code validation
- Comprehensive error handling
- Debug logging for requests and responses

### Usage Example
```python
async with AsyncHttpClient(timeout=30.0) as client:
    response = await client.get("https://service-endpoint/health")
    # Response will be validated automatically
```

## Configuration

### Environment Variables
- `HTTP_REQUEST_TIMEOUT`: Timeout for HTTP requests to monitored services

### Logging
- Structured logging with configurable levels
- Request/response logging for debugging
- Error tracking and monitoring

## Installation & Setup

1. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn httpx pydantic
   ```

2. **Environment Configuration**:
   ```bash
   export HTTP_REQUEST_TIMEOUT=30.0
   ```

3. **Run the Service**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Development

### Running in Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### API Documentation
Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Monitoring Integration

The service is designed to integrate with external monitoring systems:

1. **Service Registration**: Services can be registered for monitoring
2. **Health Checks**: Automated health checks via HTTP requests
3. **Status Reporting**: Real-time status reporting via REST API
4. **History Tracking**: Maintains historical status data

## Error Handling

The service implements comprehensive error handling:

- HTTP client errors are logged and propagated
- Service status failures are tracked in history
- API endpoints return appropriate HTTP status codes
- Detailed error messages for debugging

---

**Note**: This service is specifically designed for monitoring purposes and is currently in the development phase. Features and API endpoints may change as development progresses.