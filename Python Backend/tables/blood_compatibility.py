from fastapi import APIRouter, HTTPException
from database import cursor, connection

router = APIRouter()

@router.get("/blood_compatibility")
def get_all_blood_compatibility():
    cursor.execute("SELECT donor_group, recipient_group FROM PBlood_Compatibility")
    rows = cursor.fetchall()
    compatibility = [
        {
            "donor_group": row[0],
            "recipient_group": row[1]
        } for row in rows
    ]
    return compatibility

@router.get("/blood_compatibility/{donor_group}/{recipient_group}")
def get_blood_compatibility(donor_group: str, recipient_group: str):
    cursor.execute("""
        SELECT donor_group, recipient_group 
        FROM PBlood_Compatibility 
        WHERE donor_group = :1 AND recipient_group = :2
    """, [donor_group, recipient_group])
    row = cursor.fetchone()
    if row:
        return {
            "donor_group": row[0],
            "recipient_group": row[1]
        }
    else:
        raise HTTPException(status_code=404, detail="Compatibility not found")