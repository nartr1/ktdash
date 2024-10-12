# Contributing Guide

Thank you for your interest in contributing to the KTDash Backend! We welcome contributions from anyone who wants to help improve the project.

## Getting Started

Before you start contributing, please make sure you have the following:

* Python 3.12 or later installed on your system
* Docker installed on your system
* The required dependencies installed using pip: `pip install -r server/requirements.txt`
* A code editor or IDE of your choice
* A GitHub account (if you want to submit a pull request)

## Execution

The application can be run one of two ways:
- Through the `docker-compose.yml`
- Running locally

### Running through Docker

The quickest way to get the full stack up and running is by running the following at the root of this repository:
```bash
docker compose up
```
This will build and configure the 3 services (frontend, backend, database) from the `.env.dev` settings.

### Running locally

The backend can be run locally (after [installing the requirements](#getting-started)) with the following:
```bash
python3 server/run.py
```
This will only run the backend server, so be sure to have the database container running. Running the frontend is not necessary to use the backend.

## Documentation

Documentation is automatically generated using `redoc` from the code and is accessible at `http://localhost:8000/redoc` when running the backend (both locally and through Docker).

## Code Structure

The code is organized into the following directories:

* `app`: contains the FastAPI application code
* `models`: contains the Pydantic models used for data validation
* `routes`: contains the API endpoint definitions
* `services`: contains the business logic for the application
* `static`: contains generated frontend code (see [KTDash Frontend](./ktdash_backend/ktdash_frontend/README.md) for more information)

## Branching Strategy

We use a simple branching strategy:

* `master`: the s branch, where all changes are merged
* `feature/*`: feature branches, where new features are developed
* `fix/*`: fix branches, where bugs are fixed

## Submitting Changes

To submit changes, please follow these steps:

1. Fork the repository on GitHub
2. Create a new branch from the `master` branch (e.g. `feature/my-feature`)
3. Make your changes and commit them with a meaningful commit message
4. Push your changes to your forked repository
5. Submit a pull request to the `master` branch

## Pull Request Guidelines

When submitting a pull request, please make sure:

* The title of the pull request is descriptive and concise
* The description of the pull request includes a brief summary of the changes
* The changes are reviewed and tested before submitting the pull request
* The pull request is submitted to the correct branch (e.g. `master`)

## Code Review

All pull requests will be reviewed by the maintainers of the project. We will check for:

* Code quality and readability
* Adherence to the project's coding standards
* Correctness and functionality of the changes
* Test coverage and testing quality

## Coding Standards

We follow the PEP 8 coding standards for Python. Please make sure to adhere to these standards when writing code.

## Commit Messages

Please use meaningful and descriptive commit messages. The commit message should include:

* A brief summary of the changes
* A description of the changes (if necessary)
* Any relevant issue numbers or references

## Issues

If you find a bug or want to request a feature, please submit an issue on GitHub. Please include as much detail as possible, including:

* A clear description of the issue or feature request
* Steps to reproduce the issue (if applicable)
* Any relevant code or logs

## License

By contributing to this project, you agree to license your contributions under the MIT License.