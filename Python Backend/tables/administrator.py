from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class Administrator(BaseModel):
    user_id: int
    designation: str


@router.get("/administrators")
def get_all_administrators():
    cursor.execute("SELECT admin_id, user_id, designation FROM PAdministrator")
    rows = cursor.fetchall()
    admins = [
        {
            "admin_id": row[0],
            "user_id": row[1],
            "designation": row[2]
        } for row in rows
    ]
    return admins


@router.post("/administrators")
def create_administrator(admin: Administrator):
    try:
        cursor.execute("""
            INSERT INTO PAdministrator (user_id, designation)
            VALUES (:1, :2)
        """, (admin.user_id, admin.designation))
        connection.commit()
        return {"message": "Administrator created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="User ID does not exist in PUser_Account")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/administrators/{admin_id}")
def get_administrator_by_id(admin_id: int):
    cursor.execute("""
        SELECT admin_id, user_id, designation
        FROM PAdministrator
        WHERE admin_id = :1
    """, [admin_id])
    row = cursor.fetchone()
    if row:
        return {
            "admin_id": row[0],
            "user_id": row[1],
            "designation": row[2]
        }
    else:
        raise HTTPException(status_code=404, detail="Administrator not found")