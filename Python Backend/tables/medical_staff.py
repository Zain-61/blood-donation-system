from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class MedicalStaff(BaseModel):
    user_id: int
    qualification: str

@router.get("/medical_staff")
def get_all_medical_staff():
    cursor.execute("SELECT staff_id, user_id, qualification FROM PMedical_Staff")
    rows = cursor.fetchall()
    staff = [
        {
            "staff_id": row[0],
            "user_id": row[1],
            "qualification": row[2]
        } for row in rows
    ]
    return staff


@router.post("/medical_staff")
def create_medical_staff(staff: MedicalStaff):
    try:
        cursor.execute("""
            INSERT INTO PMedical_Staff (user_id, qualification)
            VALUES (:1, :2)
        """, (staff.user_id, staff.qualification))
        connection.commit()
        return {"message": "Medical staff created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="User ID does not exist in PUser_Account")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/medical_staff/{staff_id}")
def get_medical_staff_by_id(staff_id: int):
    cursor.execute("""
        SELECT staff_id, user_id, qualification
        FROM PMedical_Staff
        WHERE staff_id = :1
    """, [staff_id])
    row = cursor.fetchone()
    if row:
        return {
            "staff_id": row[0],
            "user_id": row[1],
            "qualification": row[2]
        }
    else:
        raise HTTPException(status_code=404, detail="Medical staff not found")