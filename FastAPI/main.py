
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, ConfigDict, field_validator

app = FastAPI(
    title="Student Management API",
    description="CRUD operations using FastAPI and Pydantic",
    version="1.0"
)


# -------------------------------
# PYDANTIC MODEL
# -------------------------------

class Student(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )

    roll_no: int = Field(gt=0, description="Student roll number")
    name: str = Field(min_length=2, max_length=50)
    branch: str = Field(min_length=2, max_length=30)
    year: int = Field(ge=1, le=4)

    @field_validator("name", "branch")
    @classmethod
    def validate_text(cls, value):
        if not value.strip():
            raise ValueError("Field cannot be empty")
        return value


# Separate model for partial updates
class StudentUpdate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid"
    )

    name: str | None = Field(default=None, min_length=2, max_length=50)
    branch: str | None = Field(default=None, min_length=2, max_length=30)
    year: int | None = Field(default=None, ge=1, le=4)


# -------------------------------
# TEMPORARY DATABASE
# -------------------------------

students = {}


@app.get("/")
async def home():
    return {
        "message": "Welcome to Student Management API",
        "docs": "/docs"
    }

# -------------------------------
# CREATE - POST
# -------------------------------

@app.post("/students", status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):

    if student.roll_no in students:
        raise HTTPException(
            status_code=409,
            detail="Student already exists"
        )

    students[student.roll_no] = student

    return {
        "message": "Student created successfully",
        "student": student
    }


# -------------------------------
# READ ALL - GET
# -------------------------------

@app.get("/students")
async def get_students():

    return {
        "message": "Students retrieved successfully",
        "students": list(students.values())
    }


# -------------------------------
# READ ONE - GET
# -------------------------------

@app.get("/students/{roll_no}", response_model=Student)
async def get_student(roll_no: int):

    student = students.get(roll_no)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# -------------------------------
# UPDATE - PUT
# -------------------------------

@app.put("/students/{roll_no}", response_model=Student)
async def update_student(roll_no: int, updated_student: Student):

    if roll_no not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    if updated_student.roll_no != roll_no:
        raise HTTPException(
            status_code=400,
            detail="Roll number cannot be changed"
        )

    students[roll_no] = updated_student

    return updated_student


# -------------------------------
# PARTIAL UPDATE - PATCH
# -------------------------------

@app.patch("/students/{roll_no}", response_model=Student)
async def partial_update(roll_no: int, update_data: StudentUpdate):

    if roll_no not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    changes = update_data.model_dump(exclude_unset=True)

    if not changes:
        raise HTTPException(
            status_code=400,
            detail="No update data provided"
        )

    existing_data = students[roll_no].model_dump()

    existing_data.update(changes)

    updated_student = Student.model_validate(existing_data)

    students[roll_no] = updated_student

    return updated_student


# -------------------------------
# DELETE - DELETE
# -------------------------------

@app.delete("/students/{roll_no}")
async def delete_student(roll_no: int):

    if roll_no not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    deleted_student = students.pop(roll_no)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }