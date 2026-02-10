# todo-api-python-devops

Minimal FastAPI todo app scaffold with Docker, Compose, Alembic, and k8s/ArgoCD placeholders.

Quick start (local with Docker Compose):

```bash
# build and start postgres + app
docker-compose up --build

# API available at http://localhost:8000
# Swagger: http://localhost:8000/docs
```

Run locally without Docker (SQLite default):

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API endpoints:
- GET /todos/
- POST /todos/
- GET /todos/{id}
- PUT /todos/{id}
- DELETE /todos/{id}

Kubernetes, ArgoCD, and CI files exist as placeholders in `k8s/` and `.github/workflows/`.
