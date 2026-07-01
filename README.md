# C4ADS Take-Home Exercise — Sanctioned Entities Viewer

A full-stack web feature built with Django REST Framework (backend) and React (frontend).
It serves fictitious sanctioned entity data from a CSV, exposes a filterable REST API,
and displays results in an interactive table.

---

## Project Structure

c4ads-take-home/
├── backend/       # Django REST Framework API
└── frontend/      # React (Vite) frontend

---

## Setup & Running Locally

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install django djangorestframework
python manage.py migrate
python manage.py load_entities   # loads entities.csv into SQLite
python manage.py runserver       # runs on http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev                      # runs on http://localhost:5173
```

Open **http://localhost:5173** to use the app.

---

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/entities/` | All entities |
| GET | `/api/entities/?country=Russia` | Filter by country |
| GET | `/api/entities/?entity_type=Individual` | Filter by type |
| GET | `/api/entities/?country=Russia&entity_type=Individual` | Combined filter |

---

## Running Tests

```bash
cd backend
source venv/bin/activate
python manage.py test entities
```

Expected output: `Ran 5 tests in ~0.006s — OK`

---

## AI Tool Usage (OpenSpec)

This project was built with AI assistance per the exercise guidelines.

| Part | Provider | Model |
|------|----------|-------|
| Django model, serializer, viewset, URL config | Anthropic | claude-sonnet-4-6 |
| CSV management command | Anthropic | claude-sonnet-4-6 |
| React frontend (App.jsx, App.css) | Anthropic | claude-sonnet-4-6 |
| Unit tests | Anthropic | claude-sonnet-4-6 |
| README structure | Anthropic | claude-sonnet-4-6 |

All code was reviewed, understood, and manually applied by the developer.
Each file was written step by step with full comprehension of the logic.

---

## Decisions & Tradeoffs

I used Django REST Framework's `ReadOnlyModelViewSet` for the API since the exercise
only requires GET operations — this kept the code minimal while still giving me a
router-based URL setup and built-in browsable API for easy manual testing. For filtering,
I chose to override `get_queryset()` directly rather than using a third-party package
like `django-filter`, which avoided an extra dependency while keeping the logic transparent
and easy to test. The CSV is loaded via a custom management command (`load_entities`)
rather than a data migration, making it easy to re-run and reset during development.
With more time, I would add pagination to the API and deploy using Docker Compose
to make the setup reproducible across environments.