#!/bin/bash
echo "Starting services..."
docker compose up -d

echo "Services running:"
echo "Flask App: http://localhost:5000"
echo "Static Site: http://localhost:8080"

echo ""
echo "To stop: docker-compose down"
echo "To view logs: docker-compose logs"
