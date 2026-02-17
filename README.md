# Cloud Computing Lab-6: Microservices with Docker and Kubernetes

## Lab Objectives
This lab demonstrates the implementation of a microservices architecture using containerization and orchestration technologies commonly used in cloud computing.

## Topics Covered
1. **Microservices Architecture**: Design and implementation of distributed services
2. **Docker Containerization**: Creating and managing Docker containers
3. **Kubernetes Orchestration**: Deploying and managing containerized applications
4. **RESTful APIs**: Building and consuming REST APIs
5. **Service Communication**: Inter-service communication in a distributed system
6. **Cloud-Native Development**: Best practices for cloud-native applications

## Project Structure
```
CC_Lab-6/
├── README.md
├── frontend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── templates/
│       └── index.html
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── kubernetes/
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── backend-deployment.yaml
│   └── backend-service.yaml
└── docker-compose.yml
```

## Architecture
This lab implements a simple two-tier microservices application:
- **Frontend Service**: A web interface for user interaction
- **Backend Service**: A REST API service for data processing

## Prerequisites
- Docker Desktop or Docker Engine
- Kubernetes (kubectl)
- Python 3.8+
- Basic understanding of cloud computing concepts

## Quick Start

### Using Docker Compose (Local Development)
```bash
# Build and start all services
docker-compose up --build

# Access the application
# Frontend: http://localhost:5000
# Backend API: http://localhost:5001
```

### Using Kubernetes
```bash
# Apply all Kubernetes configurations
kubectl apply -f kubernetes/

# Check deployment status
kubectl get pods
kubectl get services

# Access the application
kubectl port-forward service/frontend-service 5000:80
```

## Services

### Frontend Service
- Port: 5000
- Technology: Flask (Python)
- Purpose: Provides a web UI for interacting with the backend service

### Backend Service
- Port: 5001
- Technology: Flask (Python)
- Purpose: Provides REST API endpoints for data operations

## API Endpoints

### Backend API
- `GET /api/health` - Health check endpoint
- `GET /api/data` - Retrieve data
- `POST /api/data` - Create new data
- `GET /api/stats` - Get service statistics

## Learning Outcomes
After completing this lab, students should be able to:
1. Design and implement a microservices architecture
2. Containerize applications using Docker
3. Deploy containerized applications using Kubernetes
4. Understand service discovery and communication
5. Apply cloud-native development best practices
6. Work with container orchestration platforms

## Cleanup

### Docker Compose
```bash
docker-compose down
```

### Kubernetes
```bash
kubectl delete -f kubernetes/
```

## Additional Resources
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Microservices Architecture Patterns](https://microservices.io/patterns/)

## Author
Cloud Computing Lab-6 Assignment

## License
Educational Use Only