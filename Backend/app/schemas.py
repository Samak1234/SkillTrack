from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema with shared attributes
class StudentBase(BaseModel):
    name: str
    email: EmailStr

# Schema for creating a student (requires password)
class StudentCreate(StudentBase):
    password: str

# Schema for updating a student (all fields optional)
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

# Schema for returning student data (excludes sensitive info like password)
class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True