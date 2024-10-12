# KTDash Backend

This is a FastAPI backend application that provides a RESTful API for managing factions, killteams, operatives, and equipment.

## Features

* Supports CRUD operations for factions, killteams, operatives, and equipment
* Validates data using Pydantic models
* Returns JSON responses

## Continubuting
See the [CONTRIBUTING.md](./CONTRIBUTING.md) guide for full installation and execution instructions.

## Endpoints

Full API documemntation can be found at `http://localhost:8000/redoc` when running this backend locally.

## Running the Application

To run the application, you will need to have docker installed on your machine. This will spin up the backend, frontend, and database containers:
```bash
docker compose up
```