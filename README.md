# 🐳 Python Flask + Docker

A minimal, ready-to-run Python Flask application containerized with Docker. Perfect for learning Docker basics, testing container orchestration, or using as a starter template.

[![Docker Pulls](https://img.shields.io/docker/pulls/lvthillo/python-flask-docker)](https://hub.docker.com/r/lvthillo/python-flask-docker)
[![License](https://img.shields.io/github/license/lvthillo/python-flask-docker)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/lvthillo/python-flask-docker)](https://github.com/lvthillo/python-flask-docker/stargazers)

## 🎯 What It Does

Launches a Flask web server inside a Docker container. When you visit the page, it displays:

```
The hostname of the container is abc123 and its IP is 172.17.0.2.
```

This confirms the container is running and shows key networking info — useful for demos, testing, and learning Docker networking.

## ⚡ Quick Start

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed

### Option 1: Pull from Docker Hub (fastest)
```bash
docker pull lvthillo/python-flask-docker
docker run -d -p 8080:8080 --name flask-demo lvthillo/python-flask-docker
```
Visit http://localhost:8080

### Option 2: Build from source
```bash
git clone https://github.com/lvthillo/python-flask-docker.git
cd python-flask-docker
docker build -t python-flask-docker .
docker run -d -p 8080:8080 --name flask-demo python-flask-docker
```

## 🔍 Verify It's Running
```bash
# Check container IP
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' flask-demo

# Check container hostname
docker inspect -f '{{ .Config.Hostname }}' flask-demo

# View logs
docker logs flask-demo
```

## 📁 Project Structure
```
python-flask-docker/
├── app.py          # Flask application
├── Dockerfile       # Docker build instructions
├── requirements.txt # Python dependencies
└── README.md
```

## 🧹 Stop & Clean Up
```bash
docker stop flask-demo
docker rm flask-demo
```

## 🤝 Contributing

Pull requests are welcome! This project is actively maintained. If you have ideas for improvements, feel free to open an issue or submit a PR.

## 📄 License

MIT © [Lorenz Vanthillo](https://github.com/lvthillo)
