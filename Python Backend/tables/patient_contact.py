from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class PatientContact(BaseModel):
    patient_id: int
    contact_name: str
    relationship: str
    contact_phone: str

@router.post("/patient_contacts")
def create_patient_contact(contact: PatientContact):
    try:
        cursor.execute("""
            INSERT INTO PPatient_Contact (patient_id, contact_name, relationship, contact_phone)
            VALUES (:1, :2, :3, :4)
        """, (contact.patient_id, contact.contact_name, contact.relationship, contact.contact_phone))
        connection.commit()
        return {"message": "Patient contact created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Patient ID does not exist in PPatient")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/patient_contacts")
def get_all_patient_contacts():
    cursor.execute("SELECT contact_id, patient_id, contact_name, relationship, contact_phone FROM PPatient_Contact")
    rows = cursor.fetchall()
    contacts = [
        {
            "contact_id": row[0],
            "patient_id": row[1],
            "contact_name": row[2],
            "relationship": row[3],
            "contact_phone": row[4]
        } for row in rows
    ]
    return contacts

@router.get("/patient_contacts/{contact_id}")
def get_patient_contact_by_id(contact_id: int):
    cursor.execute("""
        SELECT contact_id, patient_id, contact_name, relationship, contact_phone 
        FROM PPatient_Contact 
        WHERE contact_id = :1
    """, [contact_id])
    row = cursor.fetchone()
    if row:
        return {
            "contact_id": row[0],
            "patient_id": row[1],
            "contact_name": row[2],
            "relationship": row[3],
            "contact_phone": row[4]
        }
    else:
        raise HTTPException(status_code=404, detail="Patient contact not found")