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

### Factions

* `GET /factions`: Returns a list of all factions
* `GET /factions/{faction_id}`: Returns a single faction by ID
* `POST /factions`: Creates a new faction
* `PUT /factions/{faction_id}`: Updates a faction
* `DELETE /factions/{faction_id}`: Deletes a faction

### Killteams

* `GET /killteams`: Returns a list of all killteams
* `GET /killteams/{killteam_id}`: Returns a single killteam by ID
* `POST /killteams`: Creates a new killteam
* `PUT /killteams/{killteam_id}`: Updates a killteam
* `DELETE /killteams/{killteam_id}`: Deletes a killteam

### Operatives

* `GET /operatives`: Returns a list of all operatives
* `GET /operatives/{operative_id}`: Returns a single operative by ID
* `POST /operatives`: Creates a new operative
* `PUT /operatives/{operative_id}`: Updates an operative
* `DELETE /operatives/{operative_id}`: Deletes an operative

### Equipment

* `GET /equipment`: Returns a list of all equipment
* `GET /equipment/{equipment_id}`: Returns a single equipment by ID
* `POST /equipment`: Creates new equipment
* `PUT /equipment/{equipment_id}`: Updates equipment
* `DELETE /equipment/{equipment_id}`: Deletes equipment

## Running the Application

To run the application, you will need to have docker installed on your machine. This will spin up the backend, frontend, and database containers:
```bash
docker compose up
```