# python-flask-docker
Basic Python Flask app in Docker which prints the hostname and IP of the container

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/lvthillo/python-flask-docker.git
$ docker build -t lvthillo/python-flask-docker .
```

### Download precreated image
You can also just download the existing image from [DockerHub](https://hub.docker.com/r/lvthillo/python-flask-docker/).
```
docker pull lvthillo/python-flask-docker
```

### Run the container
Create a container from the image.
```
$ docker run --name my-container -d -p 8080:8080 lvthillo/python-flask-docker
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

### Run below commands to deploy in DOcker Desktop
1. git clone <url>
2. cd <repoName>
3. Update Docker file 
4. docker build --build-arg APP_PORT=7070 -t pyflask:1 .
5. docker run -d -p 8080:8080 pyflask:1
6. docker rm -f $(docker ps -aq) ; docker rmi -f $(docker images -q) --> !! Careful !! To delete all images & Containers
7. git add . ; git commit -m "updated" ; git push origin feature/test


