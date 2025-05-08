from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from database import pool  # Assumes you're importing the Oracle connection pool from a `database.py` file
from datetime import date
# Initialize the router
router = APIRouter()

# Models for the views
class UserRoles(BaseModel):
    user_id: int
    username: str
    email: str
    phone: str
    role: str

class BloodInventoryDetails(BaseModel):
    inventory_id: int
    bank_name: str
    bank_location: str
    blood_group: str
    cost_per_unit: float
    rare_type: str
    units_available: int

class CampDonorDetails(BaseModel):
    camp_id: int
    camp_name: str
    camp_date:Optional[str]  # Assuming DATE is returned as a string
    camp_location: str
    organization_name: str
    donor_id: int
    blood_group: str
    last_donation_date:Optional[str]# Assuming DATE is returned as a string, nullable

class DonationRequestDetails(BaseModel):
    request_id: int
    patient_id: int
    user_id: int
    blood_group: str
    units_required: int
    request_date: str
    fulfilled: str
    donor_id: Optional[int]
    last_donation_date: Optional[str]

# Endpoint for VUserRoles
@router.get("/views/user_roles", response_model=List[UserRoles])
def get_user_roles():
    connection = pool.acquire()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM VUserRoles")
        rows = cursor.fetchall()
        return [
            UserRoles(
                user_id=row[0],
                username=row[1],
                email=row[2],
                phone=row[3],
                role=row[4]
            )
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        pool.release(connection)

# Endpoint for VBloodInventoryDetails
@router.get("/views/blood_inventory", response_model=List[BloodInventoryDetails])
def get_blood_inventory():
    connection = pool.acquire()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM VBloodInventoryDetails")
        rows = cursor.fetchall()
        return [
            BloodInventoryDetails(
                inventory_id=row[0],
                bank_name=row[1],
                bank_location=row[2],
                blood_group=row[3],
                cost_per_unit=row[4],
                rare_type=row[5],
                units_available=row[6]
            )
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        pool.release(connection)

# Endpoint for VCampDonorDetails
@router.get("/views/camp_donor_details", response_model=List[CampDonorDetails])
def get_camp_donor_details():
    connection = pool.acquire()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM VCampDonorDetails")
        rows = cursor.fetchall()
        return [
            CampDonorDetails(
                camp_id=row[0],
                camp_name=row[1],
                camp_date=row[2].strftime("%Y-%m-%d") if isinstance(row[2], date) else row[2],
                camp_location=row[3],
                organization_name=row[4],
                donor_id=row[5],
                blood_group=row[6],
                last_donation_date=row[7].strftime("%Y-%m-%d") if isinstance(row[7], date) else row[7],
            )
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        pool.release(connection)

# Endpoint for VDonationRequestDetails
@router.get("/views/donation_requests_details", response_model=List[DonationRequestDetails])
def get_donation_request_details():
    connection = pool.acquire()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM VDonationRequestDetails")
        rows = cursor.fetchall()
        return [
            DonationRequestDetails(
                request_id=row[0],
                patient_id=row[1],
                user_id=row[2],
                blood_group=row[3],
                units_required=row[4],
                request_date=row[5].strftime("%Y-%m-%d") if isinstance(row[5], date) else row[5],
                fulfilled=row[6],
                donor_id=row[7],
                last_donation_date=row[8].strftime("%Y-%m-%d") if isinstance(row[8], date) else row[8],
            )
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        pool.release(connection)