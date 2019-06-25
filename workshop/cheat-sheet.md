# Docker hands on workshop - cheat sheet
## Docker version and info
```docker version``` Show Docker version  
```docker info``` Show info about docker installation  

## Execute Docker image
```docker run [repository]:[TAG]```  
```docker run -p [HOST Port]:[CONTAINER Port] [repository]:[TAG]```  
```docker run -e [ENV Name]=[Value] [repository]:[TAG]```  

## Handle Docker images
```docker image ls``` (oder auch ```docker images```) List images  
```docker image rm [IMAGE ID oder REPOSITORY]```  
(oder auch ```docker rmi [IMAGE ID oder REPOSITORY]```) Delete Image  
```docker image prune``` clean up dangling images  
```docker image prune -a``` clean up unused images  

dangling=all images where no name is given (ist in der Menge der unused images enthalten)  
unused=all images that are not associated with any container  

```docker history [IMAGE ID]``` check how the image was created  
```docker tag [IMAGE ID] [NEW IMAGE ID]```  
```docker push [IMAGE ID]```  
```docker pull [IMAGE ID]```  

## Create Images
```docker build --tag=[repository]:[TAG] .``` Create docker image from Dockerfile  
```docker run -it [repository]:[TAG] sh``` check for content inside container  

## Handle Docker containers
```docker container ls``` (oder auch ```docker ps```)  
```docker container ls --all``` (oder auch ```docker ps --all```)  
```docker container ls -aq```  
```docker container inspect [CONTAINER ID or Name]```  
```docker container stop [CONTAINER ID or Name]```  stops a container  
```docker stop $(docker ps -a -q)``` stop all container  
```docker rm [CONTAINER ID or Name]``` remove one container  
```docker rm $(docker ps -a -q)``` remove all container  
```docker container start [CONTAINER ID or Name]```  starts a container  
```docker container prune``` remove all stopped containers  

## Handling Docker volumes
```docker volume create [VOLUME Name]```  
```docker volume ls```  
```docker volume inspect [VOLUME Name]``` Display detailed information on one or more volumes  
```docker volume rm [VOLUME Name]```  
```docker volume prune``` remove unused local volumes  

## Working with docker-compose
```docker-compose up``` Run the defined container  
```docker-compose down``` stops and removes the defined containers  
```docker-compose rm``` remove stopped, defined containers  