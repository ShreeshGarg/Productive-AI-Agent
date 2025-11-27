# Productivity AI Agent

Autonomous AI agent for intelligent task management and workflow optimization.

## Features

✅ Tool Integration (5 specialized tools)  
✅ Memory Management (long-term learning)  
✅ Observability (logging, metrics, tracing)  
✅ Production API (Flask with 5 endpoints)  
✅ Docker Support (containerization ready)  
✅ Unit Tests (8+ test cases)  

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY

# Run demo
python -c "from src.agent import ProductivityAgent; agent = ProductivityAgent('test'); print(agent.process_user_input('Hello'))"

# Start API server
python src/api.py

# Test API
curl http://localhost:5000/health

# Run tests
python tests/test_agent.py
```

## API Endpoints

- `GET /health` - Health check
- `POST /api/query` - Send query to agent
- `GET /api/status` - Agent metrics
- `GET /api/memory` - Memory summary
- `GET /api/session` - Session export

## Documentation

- `docs/ARCHITECTURE.md` - System architecture and design
- `docs/API_DOCUMENTATION.md` - Detailed API documentation

## Docker

```bash
docker-compose up --build
```

## Testing

```bash
python tests/test_agent.py
```

## Project Structure

```
productivity_agent_capstone/
├── src/
│   ├── agent.py (core agent)
│   └── api.py (flask api)
├── config/
│   └── config.py (configuration)
├── tests/
│   └── test_agent.py (unit tests)
├── docs/
│   ├── PROJECT_WRITEUP.md
│   ├── ARCHITECTURE.md
│   └── API_DOCUMENTATION.md
├── requirements.txt
├── setup.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Requirements

- Python 3.10+
- Google API key (get free from Google Cloud)

## License

MIT
