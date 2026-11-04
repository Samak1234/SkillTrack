from fastapi import FastAPI

app = FastAPI(
    title="SkillTrack API",
    description="Student Skills and Internship Tracker",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SkillTrack API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }