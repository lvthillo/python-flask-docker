# python-flask-docker
[![Actions Status](https://github.com/look4regev/python-flask-docker/workflows/Docker%20Image%20CI/badge.svg)](https://github.com/look4regev/python-flask-docker/actions)
[![Known Vulnerabilities](https://snyk.io/test/github/look4regev/python-flask-docker/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/look4regev/python-flask-docker?targetFile=requirements.txt)

Basic Python Flask app in Docker (slim and best practices standards) which prints the hostname and IP of the container

### Build application
```
docker compose build
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/look4regev/python-flask-docker/).
```
docker pull look4regev/python-flask-docker
```

### Run the container
Create a container from the image.
```
docker compose up
```

Now visit http://localhost:8080
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container
Verify by checking the container ip and hostname (ID):
```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-container
172.17.0.2
$ docker inspect -f '{{ .Config.Hostname }}' my-container
6095273a4e9b
```

### Running service in dev-debug-watch-on-changes mode outside of container 
```
FLASK_APP=app/app.py FLASK_ENV=development flask run
```

### Running the service in development mode inside the container with watch on changes
TBD- Basically add mounts to the code path and run flask in development mode
