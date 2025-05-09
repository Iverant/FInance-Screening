# 📊 Financial Screener API - FastAPI

A backend system built with FastAPI and SQLite for defining, storing, and managing financial screening strategies based on key metrics like PE ratio, market cap, etc.

---

##  Overall Design & Architecture

The system is designed with simplicity, modularity, and extensibility in mind. It uses **FastAPI** to expose RESTful endpoints for screen creation and management. The data is persisted using **SQLite**, and validation is handled using **Pydantic schemas**.




### Flow

- Client sends a POST request with a screening strategy.
- FastAPI parses and validates it using Pydantic.
- If valid, the data is persisted into a SQLite database using SQLAlchemy ORM.
- GET endpoints allow retrieval of saved screens.

This design ensures the separation of concerns (API logic, DB models, validation) and is easy to extend with authentication or screening logic later.


##  Sample Endpoints


`POST /create_screen — Create and save a new screen`

`GET /screens — Retrieve all stored screens`

`GET /screens/{id} — Get details of a specific screen`

---

## Sample Output

![image](https://github.com/user-attachments/assets/d06b4134-5478-43bb-92a0-1871eccd0aea)



##  Effectiveness of the Chosen Database (SQLite)

**Why SQLite?**

- 🚀 **Lightweight and fast** — Ideal for low to moderate traffic applications or MVPs.
- 🛠️ **No setup needed** — Easy for local development and testing.
- 📁 **File-based** — The database is a single `.db` file, making it easy to manage.
- 🔒 **ACID compliant** — Ensures reliable transactions.

For a prototype-level financial screener backend or a personal portfolio tool, **SQLite** strikes the right balance between performance and simplicity. However, this design is database-agnostic and can easily be switched to PostgreSQL or MySQL when needed.

---

##   Code Quality & Structure

The project is organized into the following components:

```
├── main.py             # API routes and FastAPI app
├── models.py           # SQLAlchemy DB models and DB setup
├── schemas.py          # Pydantic data validation schemas
├── db_setup.sql        # SQL script for initializing database
├── screener.db         # SQLite database file (auto-generated)
├── test_main.py        # Tests for API endpoints
├── requirements.txt    # Dependencies
└── README.md           # Documentation

```

### 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/financial-screener.git
cd financial-screener

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload
```
