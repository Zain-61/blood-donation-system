from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import cursor, connection
import cx_Oracle

router = APIRouter()

class ExchangeRequest(BaseModel):
    request_id: int

@router.get("/exchange_requests")
def get_all_exchange_requests():
    cursor.execute("SELECT exchange_id, request_id FROM PExchange_Request")
    rows = cursor.fetchall()
    exchange_requests = [
        {
            "exchange_id": row[0],
            "request_id": row[1]
        } for row in rows
    ]
    return exchange_requests


@router.post("/exchange_requests")
def create_exchange_request(exchange_request: ExchangeRequest):
    try:
        cursor.execute("""
            INSERT INTO PExchange_Request (request_id)
            VALUES (:1)
        """, (exchange_request.request_id,))
        connection.commit()
        return {"message": "Exchange request created successfully"}
    except cx_Oracle.IntegrityError as e:
        if "ORA-02291" in str(e):  # Foreign key constraint violation
            raise HTTPException(status_code=400, detail="Request ID does not exist in PDonation_Request")
        elif "ORA-00001" in str(e):  # Unique constraint violation
            raise HTTPException(status_code=400, detail="Request ID is already associated with an exchange")
        else:
            raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/exchange_requests/{exchange_id}")
def get_exchange_request_by_id(exchange_id: int):
    cursor.execute("""
        SELECT exchange_id, request_id 
        FROM PExchange_Request 
        WHERE exchange_id = :1
    """, [exchange_id])
    row = cursor.fetchone()
    if row:
        return {
            "exchange_id": row[0],
            "request_id": row[1]
        }
    else:
        raise HTTPException(status_code=404, detail="Exchange request not found")