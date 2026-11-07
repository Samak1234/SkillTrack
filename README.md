# SkillTrack Backend

A REST API backend for **SkillTrack – Student Skills and Internship Tracker**, developed using FastAPI, PostgreSQL, SQLAlchemy, and Alembic.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | Object Relational Mapper (ORM) |
| Alembic | Database schema migrations |
| Psycopg | PostgreSQL database driver |
| Pydantic Settings | Environment configuration |
| Uvicorn | ASGI server |

## Project Structure

```text
Backend/
│
├── alembic/
│   ├── versions/
│   │   └── 2b36b20b3acc_create_students_table.py
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app/
│
├── Docs/
│   └── screenshots/
│       ├── 01_skilltrack_database_connection.png
│       ├── 02_students_table_schema.png
│       ├── 03_alembic_migration_verification.png
│       └── 04_database_tables_verification.png
│
├── .env
├── alembic.ini
├── requirements.txt
└── test_db.py
```

## Folder and File Description

| Folder/File | Description |
|---|---|
| `alembic/` | Contains Alembic database migration configuration and scripts. |
| `alembic/versions/` | Stores generated database migration files. |
| `alembic/env.py` | Connects Alembic with SQLAlchemy metadata and database configuration. |
| `alembic.ini` | Main configuration file for Alembic. |
| `app/` | Contains the main FastAPI application source code. |
| `Docs/` | Stores project documentation and development evidence. |
| `Docs/screenshots/` | Contains screenshots of database setup and migration verification. |
| `.env` | Stores environment variables and database credentials. |
| `requirements.txt` | Lists Python dependencies required by the backend. |
| `test_db.py` | Contains database connection testing code. |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Samak1234/SkillTrack.git
cd SkillTrack/Backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file inside the Backend directory.

```env
DATABASE_URL=postgresql+psycopg://username:password@localhost:5432/skilltrack
```

Replace the username and password with your PostgreSQL credentials.

**Note:** Never upload your `.env` file or database credentials to GitHub.

## Database Configuration

The project uses PostgreSQL as its primary database.

| Configuration | Value |
|---|---|
| Database | PostgreSQL |
| Database Name | skilltrack |
| Schema | public |
| ORM | SQLAlchemy |
| Migration Tool | Alembic |

SQLAlchemy manages database models and connections, while Alembic handles database schema migrations.

## Database Migrations

Alembic is configured to manage database schema changes.

Initialize Alembic:

```bash
alembic init alembic
```

Generate a migration:

```bash
alembic revision --autogenerate -m "create students table"
```

Apply migrations:

```bash
alembic upgrade head
```

Check the current migration:

```bash
alembic current
```

## Database Schema

### Students Table

The `students` table has been successfully created in the PostgreSQL `skilltrack` database.

| Column | Data Type | Constraint |
|---|---|---|
| id | Integer | Primary Key |
| full_name | VARCHAR(100) | NOT NULL |
| email | VARCHAR(150) | NOT NULL |
| password_hash | VARCHAR | NOT NULL |
| created_at | TIMESTAMP WITH TIME ZONE | NOT NULL |

## Database Screenshots

The following screenshots document the database setup, table creation, and migration verification process.

### 1. SkillTrack Database Connection

Shows the SkillTrack PostgreSQL database connection in pgAdmin.

![SkillTrack Database Connection](Docs/screenshots/01_skilltrack_database_connection.png)

### 2. Students Table Schema

Shows the structure and columns of the students table in PostgreSQL.

![Students Table Schema](Docs/screenshots/02_students_table_schema.png)

### 3. Alembic Migration Verification

Shows the Alembic migration version after successfully applying the database migration.

![Alembic Migration Verification](Docs/screenshots/03_alembic_migration_verification.png)

### 4. Database Tables Verification

Shows the database tables available in the SkillTrack database, including the students table and Alembic version table.

![Database Tables Verification](Docs/screenshots/04_database_tables_verification.png)

## API Documentation

FastAPI provides interactive API documentation through Swagger UI.

Start the development server:

```bash
uvicorn app.main:app --reload
```

Open the following URLs:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Current Development Progress

- [x] FastAPI project initialization
- [x] PostgreSQL database creation
- [x] SQLAlchemy configuration
- [x] Alembic initialization
- [x] Students table creation
- [x] Database migration generation
- [x] Migration execution and verification
- [x] Database connection verification
- [x] Swagger UI verification
- [ ] Student registration and login APIs
- [ ] Authentication and authorization
- [ ] Skills management APIs
- [ ] Internship management APIs
- [ ] Student dashboard APIs

## Author

Developed as part of the **SkillTrack – Student Skills and Internship Tracker** project.