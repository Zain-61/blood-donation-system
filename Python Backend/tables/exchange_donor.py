from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class ExchangeDonor(BaseModel):
    exchange_id: int
    donor_id: int
    health_test_passed: str  # 'Y' or 'N'
@router.get("/exchange_donors")
def get_all_exchange_donors():
    cursor.execute("SELECT exchange_id, donor_id, health_test_passed FROM PExchange_Donor")
    rows = cursor.fetchall()
    exchange_donors = [
        {
            "exchange_id": row[0],
            "donor_id": row[1],
            "health_test_passed": row[2]
        } for row in rows
    ]
    return exchange_donors



@router.post("/exchange_donors")
def create_exchange_donor(exchange_donor: ExchangeDonor):
    try:
        cursor.execute("""
            INSERT INTO PExchange_Donor (exchange_id, donor_id, health_test_passed)
            VALUES (:1, :2, :3)
        """, (exchange_donor.exchange_id, exchange_donor.donor_id, exchange_donor.health_test_passed))
        connection.commit()
        return {"message": "Exchange donor added successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Invalid exchange ID or donor ID")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/exchange_donors/{exchange_id}/{donor_id}")
def get_exchange_donor_by_id(exchange_id: int, donor_id: int):
    cursor.execute("""
        SELECT exchange_id, donor_id, health_test_passed 
        FROM PExchange_Donor 
        WHERE exchange_id = :1 AND donor_id = :2
    """, [exchange_id, donor_id])
    row = cursor.fetchone()
    if row:
        return {
            "exchange_id": row[0],
            "donor_id": row[1],
            "health_test_passed": row[2]
        }
    else:
        raise HTTPException(status_code=404, detail="Exchange donor not found")