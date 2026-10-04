# Personal Finance Planner

A simple monolithic personal finance application built for DevOps Individual Assignment 1.

The application allows users to manage financial transactions, budgets, and savings goals through a FastAPI REST API.

## Features

The application contains two distinct backend feature domains:

### 1. Transactions

Responsible for recording and retrieving financial transactions.

* Create transactions
* Retrieve transactions
* Calculate total income
* Calculate total expenses
* Calculate current balance

### 2. Planning

Responsible for financial planning.

* Create and retrieve budgets
* Calculate remaining budget
* Determine whether a budget has been exceeded
* Create and retrieve savings goals
* Calculate savings progress
* Calculate remaining savings
* Determine whether a savings goal is completed

## Architecture

The application follows a modular monolith architecture.

```text
Client
   |
   v
FastAPI Application
   |
   +-------------------+
   |                   |
   v                   v
Transactions        Planning
Domain              Domain
   |                   |
   +---------+---------+
             |
             v
          SQLite
          Database
```

The application runs as a single process while keeping the two feature domains separated into different modules.

Each domain contains:

* `models.py` — database models
* `schemas.py` — API validation schemas
* `service.py` — business logic
* `router.py` — API endpoints

## Technology Stack

* Python 3.13
* FastAPI
* Uvicorn
* SQLAlchemy
* SQLite
* Pydantic
* pytest
* pytest-cov
* uv

## Project Structure

```text
personal-finance-planner/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   │
│   ├── transactions/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── service.py
│   │   └── router.py
│   │
│   └── planning/
│       ├── __init__.py
│       ├── models.py
│       ├── schemas.py
│       ├── service.py
│       └── router.py
│
├── tests/
│   ├── test_transactions.py
│   └── test_planning.py
│
├── ADR.md
├── AI_USAGE.md
├── README.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

## Setup

This project uses `uv` for Python environment and dependency management.

Clone the repository and enter the project directory:

```bash
git clone <your-repository-url>
cd personal-finance-planner
```

Install the dependencies:

```bash
uv sync
```

## Running the Application

Start the application with:

```bash
uv run python -m app.main
```

The application runs on port `8000` by default.

Once running, the API can be accessed at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

## Environment Variables

The application supports two runtime environment variables.

### PORT

Controls the port used by the application.

Default:

```text
8000
```

Example:

```powershell
$env:PORT="8080"
uv run python -m app.main
```

### DATA_DIR

Controls the directory where the SQLite database is stored.

Default:

```text
.
```

The database file is:

```text
finance.db
```

For example:

```powershell
$env:DATA_DIR="data"
uv run python -m app.main
```

The application will create the directory if necessary.

## Database

The application uses SQLite for persistent storage.

The database contains three tables:

### `transactions`

Stores financial transactions.

* `id`
* `amount`
* `type`
* `category`
* `description`
* `date`

### `budgets`

Stores spending limits.

* `id`
* `category`
* `limit_amount`
* `period`

### `savings_goals`

Stores savings targets.

* `id`
* `name`
* `target_amount`
* `current_amount`
* `deadline`

The database file is named:

```text
finance.db
```

## Testing

Run the complete test suite with:

```bash
uv run pytest
```

The project currently contains **15 automated tests** covering both backend domains.

## Test Coverage

Run the coverage report with:

```bash
uv run pytest --cov=app --cov-report=term-missing
```

Latest result:

```text
15 passed
98% total coverage
```

The coverage exceeds the assignment requirement of at least 70%.

## API Endpoints

### Transactions

Create a transaction:

```text
POST /transactions/
```

Retrieve transactions:

```text
GET /transactions/
```

### Planning — Budgets

Create a budget:

```text
POST /planning/budgets
```

Retrieve budgets:

```text
GET /planning/budgets
```

### Planning — Savings Goals

Create a savings goal:

```text
POST /planning/savings-goals
```

Retrieve savings goals:

```text
GET /planning/savings-goals
```

Interactive API documentation can be used to test these endpoints at `/docs`.

## Architecture Decisions

The main architectural decisions are documented in `ADR.md`.

The five decisions cover:

1. FastAPI as the web framework
2. Modular monolith architecture
3. SQLite for persistence
4. pytest and pytest-cov for testing
5. Environment variables for runtime configuration

## AI Usage

AI assistance was used during development for understanding assignment requirements, discussing implementation approaches, explaining technical concepts, reviewing implementation ideas, and helping with documentation.

A detailed record of AI usage is available in:

```text
AI_USAGE.md
```

## Assignment 1 Scope

This application intentionally remains a single-process monolith.

The project does **not** include:

* Dockerfile
* Docker Compose
* CI workflow
* Infrastructure as Code
* Redis
* RabbitMQ
* Celery
* External managed database
* Public deployment

These technologies are outside the scope of this assignment and are intended for later DevOps work where appropriate.
