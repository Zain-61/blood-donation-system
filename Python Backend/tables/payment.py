from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class Payment(BaseModel):
    request_id: int
    method_id: int
    amount: float
    payment_date: str  # Format: YYYY-MM-DD

@router.post("/payments")
def create_payment(payment: Payment):
    try:
        cursor.execute("""
            INSERT INTO PPayment (request_id, method_id, amount, payment_date)
            VALUES (:1, :2, :3, TO_DATE(:4, 'YYYY-MM-DD'))
        """, (payment.request_id, payment.method_id, payment.amount, payment.payment_date))
        connection.commit()
        return {"message": "Payment created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Invalid request ID or method ID")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/payments")
def get_all_payments():
    cursor.execute("SELECT payment_id, request_id, method_id, amount, payment_date FROM PPayment")
    rows = cursor.fetchall()
    payments = [
        {
            "payment_id": row[0],
            "request_id": row[1],
            "method_id": row[2],
            "amount": row[3],
            "payment_date": row[4].strftime('%Y-%m-%d') if row[4] else None
        } for row in rows
    ]
    return payments

@router.get("/payments/{payment_id}")
def get_payment_by_id(payment_id: int):
    cursor.execute("""
        SELECT payment_id, request_id, method_id, amount, payment_date 
        FROM PPayment 
        WHERE payment_id = :1
    """, [payment_id])
    row = cursor.fetchone()
    if row:
        return {
            "payment_id": row[0],
            "request_id": row[1],
            "method_id": row[2],
            "amount": row[3],
            "payment_date": row[4].strftime('%Y-%m-%d') if row[4] else None
        }
    else:
        raise HTTPException(status_code=404, detail="Payment not found")