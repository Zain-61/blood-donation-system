from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class Donation(BaseModel):
    donor_id: int
    camp_id: int
    donation_date: str  # Format: YYYY-MM-DD
    units_donated: int

@router.post("/donations")
def create_donation(donation: Donation):
    try:
        cursor.execute("""
            INSERT INTO PDonation (donor_id, camp_id, donation_date, units_donated)
            VALUES (:1, :2, TO_DATE(:3, 'YYYY-MM-DD'), :4)
        """, (donation.donor_id, donation.camp_id, donation.donation_date, donation.units_donated))
        connection.commit()
        return {"message": "Donation created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Invalid donor ID or camp ID")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/donations")
def get_all_donations():
    cursor.execute("SELECT donation_id, donor_id, camp_id, donation_date, units_donated FROM PDonation")
    rows = cursor.fetchall()
    donations = [
        {
            "donation_id": row[0],
            "donor_id": row[1],
            "camp_id": row[2],
            "donation_date": row[3].strftime('%Y-%m-%d') if row[3] else None,
            "units_donated": row[4]
        } for row in rows
    ]
    return donations

@router.get("/donations/{donation_id}")
def get_donation_by_id(donation_id: int):
    cursor.execute("""
        SELECT donation_id, donor_id, camp_id, donation_date, units_donated
        FROM PDonation
        WHERE donation_id = :1
    """, [donation_id])
    row = cursor.fetchone()
    if row:
        return {
            "donation_id": row[0],
            "donor_id": row[1],
            "camp_id": row[2],
            "donation_date": row[3].strftime('%Y-%m-%d') if row[3] else None,
            "units_donated": row[4]
        }
    else:
        raise HTTPException(status_code=404, detail="Donation not found")