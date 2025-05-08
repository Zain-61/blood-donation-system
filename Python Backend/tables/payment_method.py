from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class PaymentMethod(BaseModel):
    method_name: str
@router.get("/payment_methods")
def get_all_payment_methods():
    cursor.execute("SELECT method_id, method_name FROM PPayment_Method")
    rows = cursor.fetchall()
    payment_methods = [
        {
            "method_id": row[0],
            "method_name": row[1]
        } for row in rows
    ]
    return payment_methods


@router.post("/payment_methods")
def create_payment_method(payment_method: PaymentMethod):
    try:
        cursor.execute("""
            INSERT INTO PPayment_Method (method_name)
            VALUES (:1)
        """, (payment_method.method_name,))
        connection.commit()
        return {"message": "Payment method created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/payment_methods/{method_id}")
def get_payment_method_by_id(method_id: int):
    cursor.execute("""
        SELECT method_id, method_name 
        FROM PPayment_Method 
        WHERE method_id = :1
    """, [method_id])
    row = cursor.fetchone()
    if row:
        return {
            "method_id": row[0],
            "method_name": row[1]
        }
    else:
        raise HTTPException(status_code=404, detail="Payment method not found")