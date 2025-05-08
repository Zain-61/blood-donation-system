from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class BloodTypeInfo(BaseModel):
    blood_group: str
    cost_per_unit: float
    rare_type: str  # 'Y' or 'N'

@router.get("/blood_type_info")
def get_all_blood_type_info():
    cursor.execute("SELECT blood_group, cost_per_unit, rare_type FROM PBlood_Type_Info")
    rows = cursor.fetchall()
    blood_types = [
        {
            "blood_group": row[0],
            "cost_per_unit": float(row[1]),
            "rare_type": row[2]
        } for row in rows
    ]
    return blood_types

@router.post("/blood_type_info")
def create_blood_type_info(info: BloodTypeInfo):
    try:
        cursor.execute("""
            INSERT INTO PBlood_Type_Info (blood_group, cost_per_unit, rare_type)
            VALUES (:1, :2, :3)
        """, (info.blood_group, info.cost_per_unit, info.rare_type))
        connection.commit()
        return {"message": "Blood type info created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-00001" in str(e):  # Unique constraint violation
            raise HTTPException(status_code=400, detail="Blood group already exists")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/blood_type_info")
def get_all_blood_type_info():
    cursor.execute("SELECT blood_group, cost_per_unit, rare_type FROM PBlood_Type_Info")
    rows = cursor.fetchall()
    blood_types = [
        {
            "blood_group": row[0],
            "cost_per_unit": float(row[1]),
            "rare_type": row[2]
        } for row in rows
    ]
    return blood_types

@router.get("/blood_type_info/{blood_group}")
def get_blood_type_info_by_group(blood_group: str):
    cursor.execute("""
        SELECT blood_group, cost_per_unit, rare_type
        FROM PBlood_Type_Info
        WHERE blood_group = :1
    """, [blood_group])
    row = cursor.fetchone()
    if row:
        return {
            "blood_group": row[0],
            "cost_per_unit": float(row[1]),
            "rare_type": row[2]
        }
    else:
        raise HTTPException(status_code=404, detail="Blood type info not found")