from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class DonationRequest(BaseModel):
    patient_id: int
    blood_group: str
    units_required: int
    request_date: Optional[str] = None  # Format: YYYY-MM-DD
    status: Optional[str] = "Pending"  # Default status is "Pending"

@router.post("/donation_requests")
def create_donation_request(request: DonationRequest):
    try:
        cursor.execute("""
            INSERT INTO PDonation_Request (patient_id, blood_group, units_required, request_date, status)
            VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'), :5)
        """, (request.patient_id, request.blood_group, request.units_required, request.request_date, request.status))
        connection.commit()
        return {"message": "Donation request created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Patient ID does not exist in PPatient")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/donation_requests")
def get_all_donation_requests():
    cursor.execute("""
        SELECT request_id, patient_id, blood_group, units_required, request_date, status 
        FROM PDonation_Request
    """)
    rows = cursor.fetchall()
    requests = [
        {
            "request_id": row[0],
            "patient_id": row[1],
            "blood_group": row[2],
            "units_required": row[3],
            "request_date": row[4].strftime('%Y-%m-%d') if row[4] else None,
            "status": row[5]
        } for row in rows
    ]
    return requests

@router.get("/donation_requests/{request_id}")
def get_donation_request_by_id(request_id: int):
    cursor.execute("""
        SELECT request_id, patient_id, blood_group, units_required, request_date, status
        FROM PDonation_Request
        WHERE request_id = :1
    """, [request_id])
    row = cursor.fetchone()
    if row:
        return {
            "request_id": row[0],
            "patient_id": row[1],
            "blood_group": row[2],
            "units_required": row[3],
            "request_date": row[4].strftime('%Y-%m-%d') if row[4] else None,
            "status": row[5]
        }
    else:
        raise HTTPException(status_code=404, detail="Donation request not found")