# Architecture Decision Records

## ADR-1: Use FastAPI for the Backend

**Status:** Accepted

**Context:**
The application needs a lightweight Python backend capable of exposing HTTP endpoints while keeping the project simple enough for a single-process monolithic application.

**Decision:**
Use FastAPI as the backend web framework.

**Consequences:**
FastAPI provides automatic API documentation, request validation, and straightforward dependency injection. It also works well with Python and keeps the application lightweight. The project remains a single backend process without introducing unnecessary infrastructure.

---

## ADR-2: Use a Modular Monolith with Two Feature Domains

**Status:** Accepted

**Context:**
The application must contain at least two genuinely distinct backend feature domains while remaining a single-process application for this assignment.

**Decision:**
Organize the application into two domains: **Transactions** and **Planning**. Each domain has its own models, schemas, services, and API router.

**Consequences:**
The application remains simple to run as a monolith while maintaining clear boundaries between responsibilities. The separation also provides seams that could support extracting the domains into separate services in future work.

---

## ADR-3: Use SQLite for Persistence

**Status:** Accepted

**Context:**
The application requires persistent storage for both backend domains but external managed databases are outside the scope of the assignment.

**Decision:**
Use SQLite with SQLAlchemy as the persistence layer.

The database contains three main tables:

* `transactions`
* `budgets`
* `savings_goals`

The domains do not depend on direct relationships between their tables.

**Consequences:**
SQLite keeps deployment simple because the application requires only a local database file. SQLAlchemy provides a consistent database interface and keeps database operations separate from the domain logic. The database can be replaced by another relational database in future work if required.

---

## ADR-4: Use pytest and pytest-cov for Automated Testing

**Status:** Accepted

**Context:**
The assignment requires automated unit tests for the core business logic of both domains and at least 70% code coverage.

**Decision:**
Use pytest for automated testing and pytest-cov for measuring code coverage.

Tests cover the financial calculations in the Transactions and Planning domains as well as service operations and API endpoints.

**Consequences:**
Business logic can be verified automatically during development. Coverage measurement provides evidence that the application meets the assignment's testing requirement. The latest test run contains 15 passing tests with 99% coverage.

---

## ADR-5: Use Environment Variables for Runtime Configuration

**Status:** Accepted

**Context:**
The application must be runnable as a single process while allowing the runtime port and SQLite storage location to be configured without modifying source code.

**Decision:**
Use the `PORT` environment variable for the HTTP port and `DATA_DIR` for the SQLite database directory. The application uses port `8000` and the current directory as defaults.

**Consequences:**
The same application can run in different environments without source-code changes. The application binds to `0.0.0.0`, reads its port from the environment, and stores its SQLite database as `finance.db` inside the configured data directory.
