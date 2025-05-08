from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class Patient(BaseModel):
    user_id: int
    blood_group: str
    medical_history: Optional[str] = None

@router.post("/patients")
def create_patient(patient: Patient):
    try:
        cursor.execute("""
            INSERT INTO PPatient (user_id, blood_group, medical_history)
            VALUES (:1, :2, :3)
        """, (patient.user_id, patient.blood_group, patient.medical_history))
        connection.commit()
        return {"message": "Patient created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="User ID does not exist in PUser_Account")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/patients")
def get_all_patients():
    cursor.execute("SELECT patient_id, user_id, blood_group, medical_history FROM PPatient")
    rows = cursor.fetchall()
    patients = [
        {
            "patient_id": row[0],
            "user_id": row[1],
            "blood_group": row[2],
            "medical_history": row[3]
        } for row in rows
    ]
    return patients

@router.get("/patients/{patient_id}")
def get_patient_by_id(patient_id: int):
    cursor.execute("""
        SELECT patient_id, user_id, blood_group, medical_history 
        FROM PPatient 
        WHERE patient_id = :1
    """, [patient_id])
    row = cursor.fetchone()
    if row:
        return {
            "patient_id": row[0],
            "user_id": row[1],
            "blood_group": row[2],
            "medical_history": row[3]
        }
    else:
        raise HTTPException(status_code=404, detail="Patient not found")