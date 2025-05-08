from fastapi import FastAPI
from tables.user_account import router as user_router
from tables.patient import router as patient_router
from tables.patient_contact import router as patient_contact_router
from tables.donor import router as donor_router
from tables.donation_request import router as donation_request_router
from tables.donor_health_condition import router as donor_health_condition_router
from tables.administrator import router as admin_router
from tables.medical_staff import router as medical_staff_router
from tables.organizer import router as organizer_router
from tables.Donation_Camp import router as camp_router
from tables.blood_bank import router as blood_bank_router
from tables.blood_type_info import router as blood_type_info_router
from tables.blood_inventory import router as blood_inventory_router
from tables.donation import router as donation_router

from tables.exchange_request import router as exchange_request_router
from tables.exchange_donor import router as exchange_donor_router
from tables.payment_method import router as payment_method_router
from tables.payment import router as payment_router
from tables.blood_compatibility import router as blood_compatibility_router
from views import router as views_router
app = FastAPI()

# Register routers

app.include_router(views_router, tags=["Views"])
app.include_router(user_router, tags=["User"])
app.include_router(patient_router, tags=["patient"])
app.include_router(patient_contact_router, tags=["patient_contact"])
app.include_router(donor_router, tags=["donor"])
app.include_router(donation_request_router, tags=["Donation Request"])

app.include_router(organizer_router, tags=["Organizer"])
app.include_router(donation_router, tags=["Donation"])
app.include_router(donor_health_condition_router, tags=["Donor Health Condition"])
app.include_router(admin_router, tags=["Administrator"])
app.include_router(medical_staff_router, tags=["Medical Staff"])
app.include_router(blood_bank_router, tags=["Blood Bank"])
app.include_router(blood_type_info_router, tags=["Blood Type Info"])
app.include_router(blood_inventory_router, tags=["Blood Inventory"])
app.include_router(camp_router, tags=["Camp.........."])
app.include_router(exchange_request_router, tags=["Exchange Request"])
app.include_router(exchange_donor_router, tags=["Exchange Donor"])
app.include_router(payment_method_router, tags=["Payment Method"])
app.include_router(payment_router, tags=["Payment"])
app.include_router(blood_compatibility_router, tags=["Blood Compatibility"])


@app.get("/")
def root():
    return {"message": "Welcome to the Blood Donation System API"}