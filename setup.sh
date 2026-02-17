#!/bin/bash

# Cloud Computing Lab-6 Setup Script
# This script helps you set up and run the microservices application

set -e

echo "=========================================="
echo "Cloud Computing Lab-6 Setup"
echo "Microservices with Docker and Kubernetes"
echo "=========================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

echo "✅ Docker is installed: $(docker --version)"

# Check if Docker Compose is available
if ! docker compose version &> /dev/null; then
    echo "❌ Docker Compose is not available. Please install Docker Compose."
    exit 1
fi

echo "✅ Docker Compose is available: $(docker compose version)"
echo ""

# Menu
echo "Select an option:"
echo "1. Build and start all services"
echo "2. Stop all services"
echo "3. View logs"
echo "4. Check service status"
echo "5. Test backend API"
echo "6. Clean up (remove containers and volumes)"
echo ""
read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo ""
        echo "Building and starting services..."
        docker compose build
        docker compose up -d
        echo ""
        echo "✅ Services are starting up!"
        echo ""
        echo "Wait a few seconds for services to be ready, then access:"
        echo "  Frontend: http://localhost:5000"
        echo "  Backend API: http://localhost:5001"
        echo ""
        echo "Run './setup.sh' and choose option 4 to check status."
        ;;
    2)
        echo ""
        echo "Stopping services..."
        docker compose down
        echo "✅ Services stopped."
        ;;
    3)
        echo ""
        echo "Displaying logs (press Ctrl+C to exit)..."
        docker compose logs -f
        ;;
    4)
        echo ""
        echo "Service Status:"
        docker compose ps
        echo ""
        echo "Testing Backend Health:"
        curl -s http://localhost:5001/api/health | python3 -m json.tool || echo "Backend not responding"
        ;;
    5)
        echo ""
        echo "Testing Backend API Endpoints:"
        echo ""
        echo "1. Health Check:"
        curl -s http://localhost:5001/api/health | python3 -m json.tool
        echo ""
        echo "2. Get Data:"
        curl -s http://localhost:5001/api/data | python3 -m json.tool
        echo ""
        echo "3. Get Stats:"
        curl -s http://localhost:5001/api/stats | python3 -m json.tool
        ;;
    6)
        echo ""
        echo "Cleaning up..."
        docker compose down -v
        echo "✅ Cleanup complete."
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again and select 1-6."
        exit 1
        ;;
esac

echo ""
