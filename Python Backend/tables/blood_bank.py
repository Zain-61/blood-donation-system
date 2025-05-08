from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class BloodBank(BaseModel):
    name: str
    location: str


@router.get("/blood_banks")
def get_all_blood_banks():
    cursor.execute("SELECT bank_id, bank_name, bank_location FROM PBlood_Bank")
    rows = cursor.fetchall()
    banks = [
        {
            "bank_id": row[0],
            "bank_name": row[1],
            "bank_location": row[2]
        } for row in rows
    ]
    return banks

@router.post("/blood_banks")
def create_blood_bank(bank: BloodBank):
    try:
        cursor.execute("""
            INSERT INTO PBlood_Bank (name, location)
            VALUES (:1, :2)
        """, (bank.bank_name, bank.bank_location))
        connection.commit()
        return {"message": "Blood bank created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/blood_banks/{bank_id}")
def get_blood_bank_by_id(bank_id: int):
    cursor.execute("""
        SELECT bank_id, bank_name, bank_location
        FROM PBlood_Bank
        WHERE bank_id = :1
    """, [bank_id])
    row = cursor.fetchone()
    if row:
        return {
            "bank_id": row[0],
            "bank_name": row[1],
            "bank_location": row[2]
        }
    else:
        raise HTTPException(status_code=404, detail="Blood bank not found")