from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from database import cursor, connection
from typing import Optional
import cx_Oracle  # Ensure cx_Oracle is imported to handle exceptions

router = APIRouter()

class UserAccount(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

@router.post("/users")
def create_user(user: UserAccount):
    try:
        # Hash the password before storing it in the database

        # Insert the user into the database (user_id is auto-generated)
        cursor.execute("""
            INSERT INTO PUser_Account (username, password, email, phone)
            VALUES (:1, :2, :3, :4)
        """, (user.username, user.password, user.email, user.phone))
        connection.commit()

        return {"message": "User created successfully"}
    except cx_Oracle.IntegrityError as e:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users")
def get_all_users():
    cursor.execute("SELECT user_id, username, email, phone FROM PUser_Account")
    rows = cursor.fetchall()
    users = [
        {"user_id": row[0], "username": row[1], "password": [2], "email": row[3], "phone": row[4]}
        for row in rows
    ]
    return users

@router.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    cursor.execute("SELECT user_id, username, email, phone FROM PUser_Account WHERE user_id = :1", [user_id])
    row = cursor.fetchone()
    if row:
        return {"user_id": row[0], "username": row[1], "password":[2],"email": row[3], "phone": row[4]}
    else:
        raise HTTPException(status_code=404, detail="User not found")