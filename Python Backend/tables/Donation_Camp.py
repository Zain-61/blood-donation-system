from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class DonationCamp(BaseModel):
    camp_name: str
    camp_date: str  # Format: YYYY-MM-DD
    camp_location: str
    organizer_id: int

@router.post("/donation_camps")
def create_donation_camp(camp: DonationCamp):
    try:
        cursor.execute("""
            INSERT INTO PDonation_Camp (camp_name, camp_date, camp_location, organizer_id)
            VALUES (:1, TO_DATE(:2, 'YYYY-MM-DD'), :3, :4)
        """, (camp.camp_name, camp.camp_date, camp.camp_location, camp.organizer_id))
        connection.commit()
        return {"message": "Donation camp created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Organizer ID does not exist in POrganizer")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/donation_camps")
def get_all_donation_camps():
    cursor.execute("SELECT camp_id, camp_name, camp_date, camp_location, organizer_id FROM PDonation_Camp")
    rows = cursor.fetchall()
    camps = [
        {
            "camp_id": row[0],
            "camp_name": row[1],
            "camp_date": row[2].strftime('%Y-%m-%d') if row[2] else None,
            "camp_location": row[3],
            "organizer_id": row[4]
        } for row in rows
    ]
    return camps

@router.get("/donation_camps/{camp_id}")
def get_donation_camp_by_id(camp_id: int):
    cursor.execute("""
        SELECT camp_id, camp_name, camp_date, camp_location, organizer_id
        FROM PDonation_Camp
        WHERE camp_id = :1
    """, [camp_id])
    row = cursor.fetchone()
    if row:
        return {
            "camp_id": row[0],
            "camp_name": row[1],
            "camp_date": row[2].strftime('%Y-%m-%d') if row[2] else None,
            "camp_location": row[3],
            "organizer_id": row[4]
        }
    else:
        raise HTTPException(status_code=404, detail="Donation camp not found")