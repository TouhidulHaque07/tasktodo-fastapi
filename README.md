# TODO Task Manager API
A simple RESTful Task or Todo management API built with FastAPI and SQLite, containerized with Docker and deployed on Render.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.141-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-orange)

## Features

- Create, read, update, and delete tasks (full CRUD)
- Persistent storage using SQLite
- Docker containerized
- Docker volume with data persistence
- Deployed live on Render
- Swagger UI (/docs) with interactive API documentation

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| GET | / | Root endpoint |
| GET | /task/{task_id} | Get a single task by ID (path parameter) |
| GET | /search | Search tasks using query parameters (keyword, limit) |
| GET | /task | Get all tasks from the database |
| POST | /tasks | Create a new task in the database |
| POST | /item | Create an item (Pydantic model demo) |
| PUT | /update/{task_id} | Update a task's status (mark as done) |
| DELETE | /delete/{task_id} | Delete a task by ID |

## Tech Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **Database:** SQLite3
- **Validation:** Pydantic
- **Containerization:** Docker
- **Deployment:** Render (Docker environment)
- **Version Control:** Git & GitHub

## Live Demo

The API is deployed and live on Render:

🔗 [https://tasktodo-fastapi.onrender.com/docs](https://tasktodo-fastapi.onrender.com/docs)

> Note: Render's free tier spins down after inactivity, so the first request may take ~50 seconds to wake up.

## Setup & Installation

### Run locally

```bash
# Clone the repository
git clone https://github.com/TouhidulHaque07/tasktodo-fastapi.git
cd tasktodo-fastapi

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000/docs`

### Run with Docker

```bash
# Build the image
docker build -t tasktodo-app .

# Run the container
docker run -d -p 8000:8000 -v tasktodo-data:/app/data --name tasktodo-container tasktodo-app
```

The API will be available at `http://localhost:8000/docs`