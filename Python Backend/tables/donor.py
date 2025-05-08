from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class Donor(BaseModel):
    user_id: int
    blood_group: str
    last_donation_date: Optional[str] = None  # Format: YYYY-MM-DD

@router.post("/donors")
def create_donor(donor: Donor):
    try:
        cursor.execute("""
            INSERT INTO PDonor (user_id, blood_group, last_donation_date)
            VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'))
        """, (donor.user_id, donor.blood_group, donor.last_donation_date))
        connection.commit()
        return {"message": "Donor created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="User ID does not exist in PUser_Account")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/donors")
def get_all_donors():
    cursor.execute("SELECT donor_id, user_id, blood_group, last_donation_date FROM PDonor")
    rows = cursor.fetchall()
    donors = [
        {
            "donor_id": row[0],
            "user_id": row[1],
            "blood_group": row[2],
            "last_donation_date": row[3].strftime('%Y-%m-%d') if row[3] else None
        } for row in rows
    ]
    return donors

@router.get("/donors/{donor_id}")
def get_donor_by_id(donor_id: int):
    cursor.execute("""
        SELECT donor_id, user_id, blood_group, last_donation_date
        FROM PDonor
        WHERE donor_id = :1
    """, [donor_id])
    row = cursor.fetchone()
    if row:
        return {
            "donor_id": row[0],
            "user_id": row[1],
            "blood_group": row[2],
            "last_donation_date": row[3].strftime('%Y-%m-%d') if row[3] else None
        }
    else:
        raise HTTPException(status_code=404, detail="Donor not found")