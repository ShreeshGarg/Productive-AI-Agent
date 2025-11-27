# System Architecture

## Core Components

### 1. Agent (Core Decision Engine)
- Orchestrates tool selection and execution
- Manages conversation context
- Implements decision logic
- Tracks session state

### 2. LongTermMemory (Persistent Context)
- Stores interactions, preferences, decisions
- Enables learning and personalization
- Provides context-aware retrieval
- Handles overflow automatically

### 3. ToolKit (5 Specialized Tools)
- parse_task: Structure task descriptions
- check_dependencies: Find task blockers
- generate_schedule: Create time-blocks
- evaluate_progress: Track completion
- calculate_metrics: Performance analytics

### 4. Metrics (Observability)
- Track success rate
- Monitor latency
- Record memory size
- Export for analysis

### 5. Flask API (REST Interface)
- 5 functional endpoints
- Request/response handling
- Error recovery
- Health monitoring

## Data Flow

```
User Input
    ↓
POST /api/query
    ↓
Agent.process_user_input()
    ↓
Retrieve relevant memory
    ↓
Select appropriate tools
    ↓
Execute tools
    ↓
Aggregate results
    ↓
Generate response
    ↓
Store in memory
    ↓
Update metrics
    ↓
Return to user
```

## Deployment Architecture

### Local Development
```
User → Flask App → Agent → Tools, Memory, Metrics
```

### Docker Container
```
Docker Image
├── Python runtime
├── Dependencies (requirements.txt)
├── Application code
└── Configuration (env vars)
```

### Cloud Deployment (Ready)
- Google Cloud Run
- AWS Lambda/ECS
- Azure Container Instances
- Kubernetes clusters

## API Endpoints

- `GET /health` - Health check
- `POST /api/query` - Process query
- `GET /api/status` - Agent metrics
- `GET /api/memory` - Memory summary
- `GET /api/session` - Session export

## Scalability

- Stateless agent design
- Memory can be moved to external DB
- Metrics exportable for monitoring
- Session-independent operations
