# Cloud Computing Lab-6: Lab Manual

## Introduction

This lab focuses on implementing a microservices architecture using modern cloud-native technologies including Docker containerization and Kubernetes orchestration. You will learn how to design, build, deploy, and manage distributed applications in a cloud environment.

## Objectives

By the end of this lab, you will be able to:

1. Understand microservices architecture principles
2. Containerize applications using Docker
3. Create multi-container applications with Docker Compose
4. Deploy applications to Kubernetes
5. Implement inter-service communication
6. Monitor and manage containerized applications

## Prerequisites

Before starting this lab, ensure you have:

- Basic knowledge of Python programming
- Understanding of HTTP and REST APIs
- Familiarity with command-line interfaces
- Docker Desktop installed on your system
- Kubernetes cluster access (optional, for Kubernetes exercises)

## Lab Architecture

This lab implements a two-tier microservices application:

### Frontend Service
- **Technology**: Flask (Python web framework)
- **Port**: 5000
- **Purpose**: Provides a web-based user interface
- **Features**: 
  - Interactive dashboard
  - Service communication demonstration
  - Real-time data display

### Backend Service
- **Technology**: Flask (Python web framework)
- **Port**: 5001
- **Purpose**: REST API for data operations
- **Features**:
  - RESTful API endpoints
  - In-memory data storage
  - Health monitoring
  - Statistics tracking

## Part 1: Understanding the Architecture

### Step 1: Explore the Project Structure

Navigate to the project directory and examine its structure:

```bash
tree CC_Lab-6
```

You should see:
```
CC_Lab-6/
├── README.md              # Project documentation
├── LAB_MANUAL.md          # This file
├── setup.sh               # Setup helper script
├── docker-compose.yml     # Docker Compose configuration
├── backend/               # Backend service
│   ├── app.py            # Backend application code
│   ├── Dockerfile        # Backend container image
│   └── requirements.txt  # Python dependencies
├── frontend/              # Frontend service
│   ├── app.py            # Frontend application code
│   ├── Dockerfile        # Frontend container image
│   ├── requirements.txt  # Python dependencies
│   └── templates/
│       └── index.html    # Web UI
└── kubernetes/            # Kubernetes manifests
    ├── backend-deployment.yaml
    ├── backend-service.yaml
    ├── frontend-deployment.yaml
    └── frontend-service.yaml
```

### Step 2: Review the Code

1. **Backend Application (`backend/app.py`)**:
   - Examine the Flask routes
   - Understand the API endpoints
   - Review data storage mechanism

2. **Frontend Application (`frontend/app.py`)**:
   - Study the proxy pattern
   - Understand service-to-service communication
   - Review environment variable usage

3. **Dockerfiles**:
   - Analyze the multi-stage build process
   - Understand layer caching optimization
   - Review security best practices

## Part 2: Running with Docker Compose

### Step 1: Build the Docker Images

```bash
docker compose build
```

This command:
- Reads `docker-compose.yml`
- Builds Docker images for both services
- Caches layers for faster rebuilds

### Step 2: Start the Services

```bash
docker compose up -d
```

The `-d` flag runs containers in detached mode (background).

### Step 3: Verify Services are Running

```bash
docker compose ps
```

You should see both services in "Up" status.

### Step 4: Test the Backend API

Test each endpoint:

```bash
# Health check
curl http://localhost:5001/api/health

# Get all data
curl http://localhost:5001/api/data

# Create new data
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"My first entry"}' \
  http://localhost:5001/api/data

# Get statistics
curl http://localhost:5001/api/stats
```

### Step 5: Access the Frontend

Open your web browser and navigate to:
```
http://localhost:5000
```

Interact with the web interface:
1. Check the service status
2. Create new data entries
3. View all entries
4. Check service statistics

### Step 6: View Logs

Monitor application logs in real-time:

```bash
# View all logs
docker compose logs -f

# View logs for specific service
docker compose logs -f backend
docker compose logs -f frontend
```

### Step 7: Stop the Services

```bash
docker compose down
```

## Part 3: Kubernetes Deployment (Optional)

If you have access to a Kubernetes cluster, follow these steps:

### Step 1: Build Images for Kubernetes

```bash
# Build backend image
docker build -t backend-service:latest ./backend

# Build frontend image
docker build -t frontend-service:latest ./frontend
```

### Step 2: Deploy to Kubernetes

```bash
# Apply all configurations
kubectl apply -f kubernetes/

# Or apply individually
kubectl apply -f kubernetes/backend-deployment.yaml
kubectl apply -f kubernetes/backend-service.yaml
kubectl apply -f kubernetes/frontend-deployment.yaml
kubectl apply -f kubernetes/frontend-service.yaml
```

### Step 3: Check Deployment Status

```bash
# Check pods
kubectl get pods

# Check services
kubectl get services

# Check deployments
kubectl get deployments
```

### Step 4: Access the Application

```bash
# Port forward frontend service
kubectl port-forward service/frontend-service 5000:80

# Access at http://localhost:5000
```

### Step 5: Scale the Services

```bash
# Scale backend to 3 replicas
kubectl scale deployment backend-deployment --replicas=3

# Verify scaling
kubectl get pods
```

### Step 6: Clean Up

```bash
kubectl delete -f kubernetes/
```

## Part 4: Lab Exercises

### Exercise 1: Add a New API Endpoint

**Task**: Add a DELETE endpoint to remove data entries by ID.

1. Modify `backend/app.py` to add:
```python
@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    # Your implementation here
    pass
```

2. Rebuild and test the new endpoint.

### Exercise 2: Implement Data Persistence

**Task**: Replace in-memory storage with a database (e.g., SQLite or MongoDB).

1. Update `backend/requirements.txt` with database library
2. Modify `backend/app.py` to use persistent storage
3. Update Docker Compose to add database service
4. Test data persistence across container restarts

### Exercise 3: Add Authentication

**Task**: Implement basic authentication for API endpoints.

1. Install Flask-HTTPAuth
2. Add authentication decorator to sensitive endpoints
3. Update frontend to pass credentials
4. Test authenticated requests

### Exercise 4: Implement Logging

**Task**: Add structured logging to both services.

1. Configure Python logging
2. Add log statements for important operations
3. View logs through Docker Compose
4. Implement log aggregation (optional)

### Exercise 5: Performance Monitoring

**Task**: Add performance metrics collection.

1. Install Prometheus client library
2. Add metrics endpoints
3. Collect request duration, count, and error rates
4. Visualize metrics (optional: use Grafana)

## Part 5: Lab Questions

Answer the following questions after completing the lab:

1. **Microservices Architecture**:
   - What are the advantages of microservices over monolithic architecture?
   - What challenges do microservices introduce?

2. **Docker Containerization**:
   - How does Docker ensure application portability?
   - What is the difference between Docker images and containers?
   - What is the purpose of multi-stage builds?

3. **Service Communication**:
   - How do the frontend and backend services communicate?
   - What happens if the backend service is unavailable?
   - How would you implement service discovery?

4. **Kubernetes Orchestration**:
   - What is the difference between a Pod and a Deployment?
   - What is the purpose of a Service in Kubernetes?
   - How does Kubernetes handle service scaling?

5. **Cloud-Native Practices**:
   - How does this application follow the 12-factor app methodology?
   - What improvements would make this application more production-ready?
   - How would you implement rolling updates?

## Part 6: Troubleshooting

### Common Issues and Solutions

#### Issue: Port Already in Use

**Error**: `Bind for 0.0.0.0:5000 failed: port is already allocated`

**Solution**:
```bash
# Find process using the port
lsof -i :5000

# Kill the process or change the port in docker-compose.yml
```

#### Issue: Container Fails to Start

**Solution**:
```bash
# Check container logs
docker compose logs backend

# Check container status
docker compose ps

# Restart specific service
docker compose restart backend
```

#### Issue: Services Can't Communicate

**Solution**:
- Verify both services are on the same network
- Check service names in environment variables
- Ensure backend is healthy before frontend starts

#### Issue: Docker Build Fails

**Solution**:
```bash
# Clear Docker cache
docker system prune -a

# Rebuild without cache
docker compose build --no-cache
```

## Part 7: Additional Resources

### Documentation
- [Docker Documentation](https://docs.docker.com/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [Flask Documentation](https://flask.palletsprojects.com/)

### Tutorials
- [Docker for Beginners](https://docker-curriculum.com/)
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [Microservices Patterns](https://microservices.io/patterns/)

### Best Practices
- [The Twelve-Factor App](https://12factor.net/)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)

## Conclusion

Congratulations! You have successfully completed Cloud Computing Lab-6. You have:

- ✅ Built a microservices application
- ✅ Containerized services with Docker
- ✅ Orchestrated multi-container applications
- ✅ Deployed to Kubernetes (optional)
- ✅ Implemented inter-service communication
- ✅ Applied cloud-native best practices

## Submission Guidelines

Submit the following:

1. **Code**: Modified application with completed exercises
2. **Screenshots**: 
   - Running services in Docker
   - Web interface showing functionality
   - Kubernetes deployment (if completed)
3. **Report**: Document answering the lab questions
4. **Documentation**: Any additional features or modifications made

## Assessment Criteria

Your lab will be evaluated on:

- **Functionality** (40%): All services work correctly
- **Code Quality** (20%): Clean, well-structured code
- **Documentation** (20%): Clear explanations and comments
- **Exercises** (20%): Completion of bonus exercises

Good luck with your lab!
