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
