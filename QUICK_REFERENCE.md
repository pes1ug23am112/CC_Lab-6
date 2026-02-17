# Cloud Computing Lab-6: Quick Reference Guide

## Project Overview
A complete microservices demonstration for Cloud Computing Lab-6, featuring:
- **Backend API Service** (Flask REST API on port 5001)
- **Frontend Web Service** (Flask web app on port 5000)
- **Docker Containerization** (Dockerfile for each service)
- **Docker Compose** (Multi-container orchestration)
- **Kubernetes Deployment** (Production-ready manifests)

## Quick Start Commands

### Using Docker Compose (Recommended for Local Development)
```bash
# Start everything
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f

# Stop everything
docker compose down
```

### Using Helper Script
```bash
# Make script executable (first time only)
chmod +x setup.sh

# Run interactive menu
./setup.sh
```

### Testing the Application
```bash
# Backend API endpoints
curl http://localhost:5001/api/health          # Health check
curl http://localhost:5001/api/data            # Get all data
curl http://localhost:5001/api/stats           # Get statistics

# Create data
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"Test entry"}' \
  http://localhost:5001/api/data

# Frontend (open in browser)
http://localhost:5000
```

## Project Structure
```
CC_Lab-6/
├── README.md              # Main documentation
├── LAB_MANUAL.md         # Detailed lab instructions
├── QUICK_REFERENCE.md    # This file
├── setup.sh              # Helper script
├── docker-compose.yml    # Docker Compose config
├── .gitignore           # Git ignore rules
│
├── backend/             # Backend microservice
│   ├── app.py          # Flask REST API (131 lines)
│   ├── Dockerfile      # Container image definition
│   └── requirements.txt # Python dependencies
│
├── frontend/            # Frontend microservice
│   ├── app.py          # Flask web app (67 lines)
│   ├── Dockerfile      # Container image definition
│   ├── requirements.txt # Python dependencies
│   └── templates/
│       └── index.html  # Web UI (319 lines)
│
└── kubernetes/          # Kubernetes manifests
    ├── backend-deployment.yaml
    ├── backend-service.yaml
    ├── frontend-deployment.yaml
    └── frontend-service.yaml
```

## API Endpoints Reference

### Backend API (Port 5001)

#### GET /api/health
Health check endpoint
```bash
curl http://localhost:5001/api/health
```
Response:
```json
{
  "status": "healthy",
  "service": "backend-api",
  "version": "1.0.0",
  "timestamp": "2026-02-17T09:00:00.000000"
}
```

#### GET /api/data
Get all data entries
```bash
curl http://localhost:5001/api/data
```
Response:
```json
{
  "success": true,
  "data": [...],
  "count": 0
}
```

#### POST /api/data
Create new data entry
```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"content":"My entry"}' \
  http://localhost:5001/api/data
```
Response:
```json
{
  "success": true,
  "data": {
    "id": 1,
    "content": "My entry",
    "timestamp": "2026-02-17T09:00:00.000000"
  },
  "message": "Data created successfully"
}
```

#### GET /api/data/:id
Get specific data entry by ID
```bash
curl http://localhost:5001/api/data/1
```

#### GET /api/stats
Get service statistics
```bash
curl http://localhost:5001/api/stats
```
Response:
```json
{
  "success": true,
  "stats": {
    "total_requests": 10,
    "total_entries": 5,
    "service_uptime": "running",
    "timestamp": "2026-02-17T09:00:00.000000"
  }
}
```

## Frontend Proxy Endpoints (Port 5000)
All backend endpoints are also accessible through the frontend proxy at:
- `/api/proxy/health`
- `/api/proxy/data`
- `/api/proxy/stats`

## Environment Variables

### Backend Service
- `PORT` - Port to run on (default: 5001)
- `FLASK_DEBUG` - Enable debug mode (default: False)

### Frontend Service
- `PORT` - Port to run on (default: 5000)
- `BACKEND_URL` - Backend service URL (default: http://localhost:5001)
- `FLASK_DEBUG` - Enable debug mode (default: False)

## Kubernetes Commands

### Deploy Application
```bash
# Apply all configurations
kubectl apply -f kubernetes/

# Check deployment status
kubectl get pods
kubectl get services
kubectl get deployments
```

### Access Application
```bash
# Port forward frontend service
kubectl port-forward service/frontend-service 5000:80

# Access at http://localhost:5000
```

### Scale Services
```bash
# Scale backend to 3 replicas
kubectl scale deployment backend-deployment --replicas=3

# Scale frontend to 4 replicas
kubectl scale deployment frontend-deployment --replicas=4
```

### View Logs
```bash
# Get pod name
kubectl get pods

# View logs
kubectl logs <pod-name>

# Follow logs
kubectl logs -f <pod-name>
```

### Clean Up
```bash
kubectl delete -f kubernetes/
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 5000 or 5001
lsof -i :5000
lsof -i :5001

# Kill process or change port in docker-compose.yml
```

### Container Won't Start
```bash
# Check logs
docker compose logs backend
docker compose logs frontend

# Restart specific service
docker compose restart backend
```

### Services Can't Communicate
- Ensure both services are on the same Docker network
- Check `BACKEND_URL` environment variable in frontend
- Verify backend is healthy: `curl http://localhost:5001/api/health`

### Clear Docker Cache
```bash
# Remove all containers and images
docker compose down
docker system prune -a

# Rebuild from scratch
docker compose build --no-cache
docker compose up -d
```

## Key Features Implemented

### 1. Microservices Architecture
- ✅ Separation of concerns (frontend/backend)
- ✅ Independent deployment and scaling
- ✅ Service-to-service communication
- ✅ API-first design

### 2. Containerization
- ✅ Docker images for each service
- ✅ Multi-stage builds
- ✅ Optimized layer caching
- ✅ Health checks

### 3. Orchestration
- ✅ Docker Compose for local development
- ✅ Kubernetes deployments for production
- ✅ Service discovery
- ✅ Load balancing

### 4. Best Practices
- ✅ Thread-safe implementation
- ✅ Environment-based configuration
- ✅ Proper error handling
- ✅ Security considerations
- ✅ Resource limits
- ✅ Liveness and readiness probes

### 5. Security
- ✅ No vulnerabilities (CodeQL scan: 0 alerts)
- ✅ Updated dependencies (Werkzeug 3.0.3)
- ✅ Debug mode disabled in production
- ✅ CORS configuration for API access
- ✅ Thread-safe concurrent operations

## Learning Outcomes

After completing this lab, you should understand:
1. How to design microservices architecture
2. How to containerize applications with Docker
3. How to orchestrate multi-container apps
4. How to deploy to Kubernetes
5. How services communicate in distributed systems
6. How to implement health checks and monitoring
7. How to scale services horizontally
8. Cloud-native development best practices

## Additional Resources

- **Documentation**: See `README.md` for overview
- **Lab Instructions**: See `LAB_MANUAL.md` for detailed exercises
- **Docker Docs**: https://docs.docker.com/
- **Kubernetes Docs**: https://kubernetes.io/docs/
- **Flask Docs**: https://flask.palletsprojects.com/

## Support

If you encounter issues:
1. Check this quick reference
2. Review the troubleshooting section
3. Check container logs: `docker compose logs`
4. Verify services are running: `docker compose ps`
5. Test endpoints individually with curl

## Success Checklist

- [ ] Cloned the repository
- [ ] Read README.md and LAB_MANUAL.md
- [ ] Built Docker images successfully
- [ ] Started services with Docker Compose
- [ ] Accessed frontend at http://localhost:5000
- [ ] Tested backend API endpoints
- [ ] Created and retrieved data
- [ ] Viewed service statistics
- [ ] Stopped services cleanly
- [ ] (Optional) Deployed to Kubernetes
- [ ] Completed lab exercises
- [ ] Answered lab questions

---

**Lab-6 Complete!** 🎉

You've successfully implemented a microservices application with Docker and Kubernetes!
