# Dockerized Flask + Nginx + Redis Setup

This project demonstrates running a **Flask application**, **Nginx static site**, and **Redis** using **Docker Compose**.

---

## 🚀 Services & Ports

| Service | Description             | Host Port | Container Port |
|---------|-------------------------|-----------|----------------|
| Flask   | Visit counter app       | 5000      | 5000           |
| Nginx   | Static site (HTML page) | 8080      | 80             |
| Redis   | In-memory database      | 6379      | 6379           |

---

## 🔧 Setup Instructions

### 1. Build all images
```bash
docker-compose build

2. Start all services
docker-compose up -d

3. List running containers
docker-compose ps

4. View logs
docker-compose logs

5. Stop and remove containers
docker-compose down

🌐 Testing

Flask App (Visit Counter)

Open: http://localhost:5000

Refresh the page → counter should increase

Static Site (Nginx)

Open: http://localhost:8080

Should display a static HTML page

Navigation links between Flask and Nginx pages should work

✅ You now have a fully running Flask + Nginx + Redis environment with Docker Compose!


Do you also want me to add a **Quick Start section with `build.sh` and `run.sh`** like in 
