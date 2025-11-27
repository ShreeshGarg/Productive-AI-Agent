# REST API Documentation

## Base URL
```
http://localhost:5000
```

## Authentication
Currently no authentication. Future versions support OAuth2.

## Endpoints

### 1. GET /health
**Description**: Check if agent is running and healthy.

**Response** (200 OK):
```json
{
    "status": "healthy",
    "agent": "operational"
}
```

### 2. POST /api/query
**Description**: Send a request/query to the agent.

**Request**:
```json
{
    "query": "Help me organize my tasks"
}
```

**Response** (200 OK):
```json
{
    "status": "success",
    "query": "Help me organize my tasks",
    "response": "Based on your preferences....",
    "timestamp": "2025-11-27T21:00:00.000000"
}
```

### 3. GET /api/status
**Description**: Get agent metrics and status.

**Response** (200 OK):
```json
{
    "metrics": {
        "total_requests": 5,
        "successful_tasks": 5,
        "failed_tasks": 0
    },
    "memory": {
        "total_entries": 12,
        "types": ["task", "preference"]
    },
    "status": "operational"
}
```

### 4. GET /api/memory
**Description**: Inspect agent memory.

**Response** (200 OK):
```json
{
    "memory": {
        "total_entries": 12,
        "types": ["task", "preference", "decision"],
        "oldest": "2025-11-27T20:00:00",
        "newest": "2025-11-27T21:00:00"
    }
}
```

### 5. GET /api/session
**Description**: Export complete session data.

**Response** (200 OK):
```json
{
    "interactions": [
        {
            "timestamp": "2025-11-27T21:00:00",
            "user_input": "Help with tasks"
        }
    ],
    "metrics": {
        "total_requests": 5,
        "successful_tasks": 5,
        "failed_tasks": 0
    }
}
```

## Usage Examples

### cURL
```bash
# Health check
curl http://localhost:5000/health

# Send query
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query":"Help organize my tasks"}'

# Get status
curl http://localhost:5000/api/status

# Get memory
curl http://localhost:5000/api/memory

# Export session
curl http://localhost:5000/api/session
```

### Python
```python
import requests

response = requests.post(
    "http://localhost:5000/api/query",
    json={"query": "Help with tasks"}
)
print(response.json())
```

## Error Handling

| Status | Meaning |
|--------|---------|
| 200 | Success |
| 400 | Bad request (missing query) |
| 500 | Server error |

Error response:
```json
{"error": "Error message"}
```

---

## Rate Limiting
Currently no rate limiting. Production deployments should implement.

## Response Time
Typical response time: < 2 seconds
API overhead: < 100ms
