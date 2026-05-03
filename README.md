# TaskFlow — Cloud-Native Task Management Platform

A production-grade Trello-like backend built with FastAPI, PostgreSQL,
Docker, Kubernetes, and GitHub Actions CI/CD.

## Tech Stack
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **CI/CD:** GitHub Actions
- **Monitoring:** Prometheus + Grafana
- **GitOps:** ArgoCD
- **Cloud:** AWS EC2

## Project Status
- [x] Phase 1 — Project Setup
- [ ] Phase 2 — FastAPI Basics
- [ ] Phase 3 — Database Integration
- [ ] Phase 4 — Authentication
- [ ] Phase 5 — Task APIs
- [ ] Phase 6 — Docker
- [ ] Phase 7 — Docker Hub
- [ ] Phase 8 — Kubernetes
- [ ] Phase 9 — CI/CD
- [ ] Phase 10 — Monitoring
- [ ] Phase 11 — GitOps
- [ ] Phase 12 — AWS EC2

## Quick Start

### Prerequisites
- Python 3.10+
- Git

### Run Locally

```bash
# Clone the repository
git clone https://github.com/anurag-devops03/taskflow.git
cd taskflow

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the application
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

### API Endpoints

| Method | Endpoint  | Description       |
|--------|-----------|-------------------|
| GET    | /         | Root welcome page |
| GET    | /health   | Health check      |
| GET    | /docs     | Swagger UI        |
