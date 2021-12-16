# Session based Microservices on k8s

## Running It Locally

```
docker-compose up
```

## On k8s Cluster

```
docker build -t <backend_image_name> ./backend
docker build -t <frontend_image_name> ./frontend
```

- push to a public repo or private repo(extra config for docker pull creds required if image is private)

- update image names accordingly in k8s/*-deployment.yaml files 

- kubectl apply -f k8s/*
