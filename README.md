# Loan Application Scoring

A simple full-stack project that evaluates loan applications and returns a risk score with a decision category.

## Features

- FastAPI backend with a single prediction endpoint
- Lightweight frontend form (HTML + JavaScript + Tailwind CDN)
- Deterministic scoring engine based on normalized financial inputs
- Dockerized backend and frontend with docker-compose orchestration
- Request and decision logging to data/api_logs.txt

## Project Structure

```text
Loan_Application_Scoring/
|- app/
|  |- backend/
|  |  |- main.py
|  |  |- score_eval.py
|  |  |- schemas.py
|  |  |- config.py
|  |  |- logger.py
|  |  |- requirements.txt
|  |  |- .env
|  |- frontend/
|     |- index.html
|     |- app.js
|- data/
|  |- api_logs.txt
|- docker-compose.yml
```

## How It Works

1. User submits age, income, requested loan amount, and credit score in the frontend.
2. Frontend sends POST /predict to the backend.
3. Backend validates input with Pydantic schema.
4. Scoring module normalizes values to a 0-100 scale and applies weighted scoring.
5. Backend returns:
   - risk_score (0-100)
   - risk_category: HIGH, MEDIUM, or LOW

## Scoring Model

Inputs are normalized and combined with fixed weights:

- Age weight: 0.1
- Income weight: 0.3
- Loan amount weight: 0.2
- Credit score weight: 0.4

The score is computed as:

```text
risk_score = (norm_age * 0.1)
					 + (norm_income * 0.3)
					 + (norm_loan_amount * 0.2)
					 + (norm_credit_score * 0.4)
```

Decision thresholds:

- HIGH: risk_score <= 30
- MEDIUM: 30 < risk_score < 70
- LOW: risk_score >= 70

## API Reference

### POST /predict

Request body:

```json
{
  "age": 35,
  "income": 85000,
  "loan_amount": 20000,
  "credit_score": 720
}
```

Response body:

```json
{
  "risk_score": 74.82,
  "risk_category": "LOW"
}
```

Interactive docs are available at:

- http://localhost:8000/docs

## Prerequisites

- Python 3.11+
- Docker and Docker Compose (for containerized run)

## Run Locally (Without Docker)

### 1. Start backend

From app/backend:

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Ensure app/backend/.env contains:

```env
FRONTEND_CORS_ORIGINS=http://localhost:8000,http://127.0.0.1:5500,http://localhost:5500
```

### 2. Start frontend

From app/frontend:

```powershell
python -m http.server 5500
```

Open:

- http://localhost:5500

## Run With Docker Compose

From the repository root:

```powershell
docker compose up --build
```

Services:

- Frontend: http://localhost:5500
- Backend API: http://localhost:8000
- Backend docs: http://localhost:8000/docs

To stop:

```powershell
docker compose down
```

## Logging

The backend writes logs to:

- data/api_logs.txt

Logs include request values and final decision outcome.

## Troubleshooting

- CORS errors:
  - Verify frontend URL is included in app/backend/.env under FRONTEND_CORS_ORIGINS.
- Frontend cannot reach backend:
  - Confirm backend is running on port 8000.
- Docker frontend opens but requests fail:
  - Ensure backend container is healthy and reachable at http://localhost:8000.
