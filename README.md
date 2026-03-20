# DevOps Docker App

Simple containerized web application with:

- Nginx (reverse proxy)
- Flask API
- PostgreSQL database
- Docker & Docker Compose

## Architecture

User → Nginx → Flask App → PostgreSQL

## Features

- REST API
- Data persistence in PostgreSQL
- Reverse proxy routing
- Multi-container setup

## Run project

```bash
docker-compose up --build

## App available at:
http://localhost:8080

## API

POST /data
GET /data

## Lessons learned

Containers communicate via service names
Docker volumes and initialization scripts
Debugging Docker issues (cache, mounts)

