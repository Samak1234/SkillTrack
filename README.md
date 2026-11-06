# SkillTrack — Student Skills and Internship Tracker

SkillTrack is a student-focused platform designed to help students organize their technical skills, projects, certifications, internship experience, and career preparation progress in one place.

The project is being developed as a student project, with the goal of creating a centralized system for tracking skill development and internship readiness.

---

## Project Objectives

- Maintain student profiles and academic information.
- Track technical and professional skills.
- Record projects and certifications.
- Manage internship information and applications.
- Monitor career preparation and interview practice.
- Explore student skill-readiness analysis and prediction features.

---

## Current Development Status

**Status:** Backend foundation completed; PostgreSQL connection verified.

The project is currently in its initial backend development phase. The FastAPI application has been created and successfully connected to the PostgreSQL database.

---

## Technology Stack

| Component | Technology |
|---|---|
| Backend language | Python |
| Backend framework | FastAPI |
| ASGI server | Uvicorn |
| Database | PostgreSQL |
| Database toolkit | SQLAlchemy |
| PostgreSQL driver | Psycopg |
| Configuration | Pydantic Settings |
| API documentation | FastAPI Swagger UI |
| Version control | Git and GitHub |
| Development environment | Visual Studio Code |

---

## Project Structure

```text
SkillTrack/
│
├── Backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   └── database.py
│   │
│   ├── test_db.py
│   ├── requirements.txt
│   └── .env
│
├── venv/
├── .gitignore
└── README.md
```

### File and Folder Description

| File or Folder | Purpose |
|---|---|
| `Backend/app/main.py` | Initializes the FastAPI application and defines the initial API endpoints. |
| `Backend/app/database.py` | Configures the SQLAlchemy engine, database sessions, and declarative base. |
| `Backend/app/__init__.py` | Initializes the backend application directory as a Python package. |
| `Backend/test_db.py` | Tests whether the backend can connect to PostgreSQL. |
| `Backend/requirements.txt` | Lists Python dependencies required by the backend. |
| `Backend/.env` | Stores local environment configuration, including the database connection URL. |
| `venv/` | Contains the local Python virtual environment. |
| `.gitignore` | Excludes generated files, virtual environments, and private configuration from Git. |
| `README.md` | Documents the project, setup, progress, and planned work. |

> **Security note:** The `.env` file contains private configuration and should not be committed to GitHub.

---

## Completed Development Work

### 1. Repository and Environment Setup

- Created the SkillTrack GitHub repository.
- Cloned the repository to the local computer.
- Created the initial project folder structure.
- Created a Python virtual environment.
- Activated the virtual environment for backend development.
- Set up the project in Visual Studio Code.

### 2. FastAPI Backend Setup

- Installed FastAPI.
- Installed Uvicorn.
- Created the initial FastAPI application.
- Configured the API title, description, and version.
- Added a welcome endpoint.
- Added a health-check endpoint.
- Started the backend using Uvicorn.
- Verified the API endpoints successfully.
- Verified the automatically generated API documentation.

### 3. Git Configuration

- Created a `.gitignore` file.
- Added rules to exclude Python cache files.
- Added rules to exclude virtual environment folders.
- Added rules to exclude `.env` files.
- Added rules to exclude local VS Code settings.
- Began organizing Git history with separate commits for individual files and changes.

### 4. PostgreSQL Setup

- Installed and opened pgAdmin 4.
- Connected to the PostgreSQL 17 server.
- Created the `skilltrack` database.
- Installed SQLAlchemy.
- Installed Psycopg for PostgreSQL connectivity.
- Installed Pydantic Settings for environment-based configuration.

### 5. Database Configuration and Verification

- Created the database configuration module.
- Configured the database URL to load from the `.env` file.
- Created the SQLAlchemy database engine.
- Configured the SQLAlchemy session factory.
- Created the declarative base for future database models.
- Created a database connection test script.
- Successfully verified the connection between the SkillTrack backend and PostgreSQL.

---

## API Endpoints

The following initial endpoints are available:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Returns a welcome message and API running status. |
| `GET` | `/health` | Returns the health status of the API. |
| `GET` | `/docs` | Opens the automatically generated Swagger API documentation. |

---

## Local Development Setup

### Prerequisites

Install the following tools:

- Python
- PostgreSQL
- pgAdmin 4
- Visual Studio Code
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Samak1234/SkillTrack.git
cd SkillTrack
```

### 2. Create a Virtual Environment

```powershell
python -m venv venv
```

### 3. Activate the Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Install Backend Dependencies

```powershell
pip install -r Backend\requirements.txt
```

### 5. Configure the Database

Create a file named `.env` inside the `Backend` folder.

Add the following configuration, replacing the placeholder with your PostgreSQL password:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_POSTGRES_PASSWORD@localhost:5432/skilltrack
```

Keep your actual password private. Do not upload or commit the `.env` file.

### 6. Start the Backend

```powershell
cd Backend
python -m uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### 7. Open API Documentation

Visit:

```text
http://127.0.0.1:8000/docs
```

---

## Verify the PostgreSQL Connection

From the `Backend` folder, run:

```powershell
python test_db.py
```

A successful connection displays:

```text
SkillTrack database connected successfully!
```

---

## Planned Development Tasks

The following features are planned but **have not yet been implemented**.

### Backend

- Create database models.
- Configure database table creation.
- Set up database migrations.
- Develop student profile endpoints.
- Develop technical skill tracking endpoints.
- Develop project and certification endpoints.
- Develop internship tracking endpoints.
- Implement authentication and authorization.
- Add request validation and error handling.

### Frontend

- Set up the frontend application.
- Create student dashboard pages.
- Create profile and skills management pages.
- Create project and certification pages.
- Create internship tracking pages.
- Connect the frontend to the FastAPI backend.

### Analytics and Readiness Features

- Define student skill-readiness criteria.
- Collect and organize relevant student progress data.
- Explore skill-gap analysis.
- Explore mock interview and performance tracking.
- Explore machine-learning-based readiness predictions.

---

## Current Project Milestone

The initial development milestone is complete:

- FastAPI backend created.
- Initial API endpoints tested.
- PostgreSQL database created.
- SQLAlchemy configuration added.
- PostgreSQL connection successfully verified.

The next milestone is to create the first database models and begin implementing the core student-tracking functionality.

---

## Project Repository

GitHub: https://github.com/Samak1234/SkillTrack

---

## Disclaimer

SkillTrack is currently under development as a student project. Features listed under **Planned Development Tasks** are future goals and are not yet available in the application.

## Screenshots

### FastAPI Swagger Documentation
Shows the running SkillTrack API and its initial Home endpoint.

![SkillTrack FastAPI Swagger Documentation](screenshots/skilltrack-fastapi-swagger-home-endpoint.png)