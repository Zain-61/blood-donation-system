from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class Organizer(BaseModel):
    user_id: int
    organization_name: str

@router.post("/organizers")
def create_organizer(organizer: Organizer):
    try:
        cursor.execute("""
            INSERT INTO POrganizer (user_id, organization_name)
            VALUES (:1, :2)
        """, (organizer.user_id, organizer.organization_name))
        connection.commit()
        return {"message": "Organizer created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="User ID does not exist in PUser_Account")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/organizers")
def get_all_organizers():
    cursor.execute("SELECT organizer_id, user_id, organization_name FROM POrganizer")
    rows = cursor.fetchall()
    organizers = [
        {
            "organizer_id": row[0],
            "user_id": row[1],
            "organization_name": row[2]
        } for row in rows
    ]
    return organizers

@router.get("/organizers/{organizer_id}")
def get_organizer_by_id(organizer_id: int):
    cursor.execute("""
        SELECT organizer_id, user_id, organization_name 
        FROM POrganizer 
        WHERE organizer_id = :1
    """, [organizer_id])
    row = cursor.fetchone()
    if row:
        return {
            "organizer_id": row[0],
            "user_id": row[1],
            "organization_name": row[2]
        }
    else:
        raise HTTPException(status_code=404, detail="Organizer not found")