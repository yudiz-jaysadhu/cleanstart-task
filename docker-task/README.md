Simple Docker Assessment

This project demonstrates how to run a Flask application with Redis and serve a static website with Nginx, all orchestrated using Docker Compose.

📦 What’s Inside
Flask App →  Python app with Redis visit counter
Nginx Static Site →  Simple HTML page served with Nginx
Redis →  In-memory data store used by Flask
Docker Compose →  Runs all services together

⚡ Quick Start

1. Clone the repository
git clone <your-repo-url> docker-assessment
cd docker-assessment

2. Make scripts executable
chmod +x build.sh run.sh

3. Build Docker images
./build.sh

4. Start all services
./run.sh

🌍 Access Applications

Flask App (with Redis counter): http://localhost:5000

Static Site (served by Nginx): http://localhost:8080

🐳 Docker Commands (Manual)
# Build all images
docker-compose build

# Start all services
docker-compose up -d

# List running containers
docker-compose ps

# View logs
docker-compose logs

# Stop and remove containers
docker-compose down

🔌 Port Mapping
Service	Container Port	Host Port
Flask	5000	5000
Nginx	80	8080
Redis	6379	6379

✅ Testing
Open http://localhost:5000
 → should show visit counter.

Refresh Flask page → counter should increase.

Open http://localhost:8080
 → should show static page.

Use links between Flask and Nginx pages → navigation works.
