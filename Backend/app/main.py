from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import models, schemas

app = FastAPI(
    title="SkillTrack API",
    description="Student Skills and Internship Tracker",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome/to SkillTrack API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# --- STUDENT CRUD ENDPOINTS ---

@app.post("/students/", response_model=schemas.StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    existing_student = db.query(models.Student).filter(models.Student.email == student.email).first()
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    db_student = models.Student(
        name=student.name,
        email=student.email,
        hashed_password=student.password 
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


@app.get("/students/", response_model=List[schemas.StudentResponse])
def get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = db.query(models.Student).offset(skip).limit(limit).all()
    return students


@app.get("/students/{student_id}", response_model=schemas.StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    return student


@app.delete("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found"
        )
    db.delete(student)
    db.commit()
    return None