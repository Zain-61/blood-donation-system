from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class DonorHealthCondition(BaseModel):
    donor_id: int
    condition_name: str
    condition_details: Optional[str] = None


@router.get("/donor_health_conditions")
def get_all_donor_health_conditions():
    cursor.execute("SELECT condition_id, donor_id, condition_name, condition_details FROM PDonor_HealthCondition")
    rows = cursor.fetchall()
    conditions = [
        {
            "condition_id": row[0],
            "donor_id": row[1],
            "condition_name": row[2],
            "condition_details": row[3]
        } for row in rows
    ]
    return conditions

@router.post("/donor_health_conditions")
def create_donor_health_condition(condition: DonorHealthCondition):
    try:
        cursor.execute("""
            INSERT INTO PDonor_HealthCondition (donor_id, condition_name, condition_details)
            VALUES (:1, :2, :3)
        """, (condition.donor_id, condition.condition_name, condition.condition_details))
        connection.commit()
        return {"message": "Donor health condition created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Donor ID does not exist in PDonor")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/donor_health_conditions/{condition_id}")
def get_donor_health_condition_by_id(condition_id: int):
    cursor.execute("""
        SELECT condition_id, donor_id, condition_name, condition_details
        FROM PDonor_HealthCondition
        WHERE condition_id = :1
    """, [condition_id])
    row = cursor.fetchone()
    if row:
        return {
            "condition_id": row[0],
            "donor_id": row[1],
            "condition_name": row[2],
            "condition_details": row[3]
        }
    else:
        raise HTTPException(status_code=404, detail="Health condition not found")