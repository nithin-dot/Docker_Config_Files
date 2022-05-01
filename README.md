# Docker_compose_files
Docker Compose is an file which used to setup the docker Containers with its configuration the file consist of Configuartions which help to deploy the containers

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration.

  -  Define your app’s environment with a ```Dockerfile``` so it can be reproduced anywhere.

  -  Define the services that make up your app in ```docker-compose.yml``` so they can be run together in an isolated environment.

  -  Run ```docker compose up``` and the Docker compose command starts and runs your entire app. You can alternatively run ```docker-compose up``` using the docker-compose binary.

  - A ```docker-compose.yml``` looks like this:
```
version: '3.7'
services:
  jenkins:
    image: jenkins/jenkins:lts
    privileged: true
    user: root
    ports:
      - 8081:8080
      - 50000:50000
    container_name: jenkins
    volumes:
      - ~/jenkins:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
      - /usr/local/bin/docker:/usr/local/bin/docker
```
