from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class BloodInventory(BaseModel):
    bank_id: int
    blood_group: str
    units_available: int

@router.post("/blood_inventory")
def create_blood_inventory_entry(inventory: BloodInventory):
    try:
        cursor.execute("""
            INSERT INTO PBlood_Inventory (bank_id, blood_group, units_available)
            VALUES (:1, :2, :3)
        """, (inventory.bank_id, inventory.blood_group, inventory.units_available))
        connection.commit()
        return {"message": "Blood inventory entry created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Invalid bank ID or blood group")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/blood_inventory")
def get_all_blood_inventory():
    cursor.execute("SELECT inventory_id, bank_id, blood_group, units_available FROM PBlood_Inventory")
    rows = cursor.fetchall()
    inventory = [
        {
            "inventory_id": row[0],
            "bank_id": row[1],
            "blood_group": row[2],
            "units_available": row[3]
        } for row in rows
    ]
    return inventory

@router.get("/blood_inventory/{inventory_id}")
def get_blood_inventory_by_id(inventory_id: int):
    cursor.execute("""
        SELECT inventory_id, bank_id, blood_group, units_available
        FROM PBlood_Inventory
        WHERE inventory_id = :1
    """, [inventory_id])
    row = cursor.fetchone()
    if row:
        return {
            "inventory_id": row[0],
            "bank_id": row[1],
            "blood_group": row[2],
            "units_available": row[3]
        }
    else:
        raise HTTPException(status_code=404, detail="Blood inventory entry not found")