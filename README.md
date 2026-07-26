# lvthillo/python-flask-docker

Basic Python Flask app in Docker which prints the hostname and IP of the container

[![Docker Pulls](https://img.shields.io/docker/pulls/lvthillo/python-flask-docker)](https://hub.docker.com/r/lvthillo/python-flask-docker)
[![License](https://img.shields.io/github/license/lvthillo/python-flask-docker)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/lvthillo/python-flask-docker)](https://github.com/lvthillo/python-flask-docker/stargazers)

## About

Launches a Flask web server inside a Docker container. When you visit the page, it displays:

```
The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2.
```

This confirms the container is running and shows key networking info -- useful for demos, testing, and learning Docker networking.

## Quick Start

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
docker build -t lvthillo/python-flask-docker .
docker run -d -p 8080:8080 --name flask-demo lvthillo/python-flask-docker
```

## Verify It's Running
```bash
# Check container IP
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' flask-demo

# Check container hostname
docker inspect -f '{{ .Config.Hostname }}' flask-demo

# View logs
docker logs flask-demo
```

## Project Structure
```
python-flask-docker/
├── src/
│   └── app.py      # Flask application
├── Dockerfile       # Docker build instructions
├── requirements.txt # Python dependencies
└── README.md
```

## Stop & Clean Up
```bash
docker stop flask-demo
docker rm flask-demo
```

## License

MIT
