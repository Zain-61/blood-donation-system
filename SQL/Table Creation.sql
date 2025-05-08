-- PUSER_ACCOUNT
CREATE TABLE PUser_Account (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);

-- PPATIENT
CREATE TABLE PPatient (
    patient_id INT PRIMARY KEY,
    user_id INT UNIQUE,
    blood_group VARCHAR(5) NOT NULL,
    medical_history VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES PUser_Account(user_id)
);

-- PPATIENT_CONTACT
CREATE TABLE PPatient_Contact (
    contact_id INT PRIMARY KEY,
    patient_id INT,
    contact_name VARCHAR(100) NOT NULL,
    relationship VARCHAR(50) NOT NULL,
    contact_phone VARCHAR(15) NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES PPatient(patient_id)
);

-- PDONOR
CREATE TABLE PDonor (
    donor_id INT PRIMARY KEY,
    user_id INT UNIQUE ,
    blood_group VARCHAR(5),
    last_donation_date DATE,
    FOREIGN KEY (user_id) REFERENCES PUser_Account(user_id)
);

-- PDONOR_HEALTHCONDITION
CREATE TABLE PDonor_HealthCondition (
    condition_id INT PRIMARY KEY,
    donor_id INT,
    condition_name VARCHAR(100),
    condition_details VARCHAR(255),
    FOREIGN KEY (donor_id) REFERENCES PDonor(donor_id)
);

-- PADMINISTRATOR
CREATE TABLE PAdministrator (
    admin_id INT PRIMARY KEY,
    user_id INT,
    designation VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES PUser_Account(user_id)
);

-- PMEDICAL_STAFF
CREATE TABLE PMedical_Staff (
    staff_id INT PRIMARY KEY,
    user_id INT,
    qualification VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES PUser_Account(user_id)
);

-- PORGANIZER
CREATE TABLE POrganizer (
    organizer_id INT PRIMARY KEY,
    user_id INT,
    organization_name VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES PUser_Account(user_id)
);

-- PDonation_Camp
CREATE TABLE PDonation_Camp (
    camp_id INT PRIMARY KEY,
    camp_name VARCHAR(100),
    camp_date DATE,
    camp_location VARCHAR(100),
    organizer_id INT,
    FOREIGN KEY (organizer_id) REFERENCES POrganizer(organizer_id)
);

-- PBLOOD_BANK
CREATE TABLE PBlood_Bank (
    bank_id INT PRIMARY KEY ,
    bank_name VARCHAR(100) NOT NULL UNIQUE,
    bank_location VARCHAR(100) NOT NULL
);

-- PBLOOD_TYPE_INFO
CREATE TABLE PBlood_Type_Info (
    blood_group VARCHAR(5) PRIMARY KEY,
    cost_per_unit DECIMAL(10,2) CHECK (cost_per_unit >= 0),
    rare_type CHAR(1) CHECK (rare_type IN ('Y', 'N'))
);

-- PBLOOD_INVENTORY
CREATE TABLE PBlood_Inventory (
    inventory_id INT PRIMARY KEY,
    bank_id INT,
    blood_group VARCHAR(5),
    units_available INT CHECK (units_available >= 0),
    FOREIGN KEY (bank_id) REFERENCES PBlood_Bank(bank_id) ON DELETE CASCADE,
    FOREIGN KEY (blood_group) REFERENCES PBlood_Type_Info(blood_group)
);

-- PDONATION
CREATE TABLE PDonation (
    donation_id INT PRIMARY KEY,
    donor_id INT,
    camp_id INT,
    donation_date DATE,
    units_donated INT CHECK (units_donated > 0) NOT NULL,
    FOREIGN KEY (donor_id) REFERENCES PDonor(donor_id),
    FOREIGN KEY (camp_id) REFERENCES PDonation_Camp(camp_id)
);



-- PDONATION_REQUEST
CREATE TABLE PDonation_Request (
    request_id INT PRIMARY KEY,
    patient_id INT,
    blood_group VARCHAR(5),
    units_required INT CHECK (units_required > 0),
    request_date DATE,
    fulfilled CHAR(1) DEFAULT 'N' CHECK (fulfilled IN ('Y', 'N')),
    FOREIGN KEY (patient_id) REFERENCES PPatient(patient_id)
);

-- PEXCHANGE_REQUEST
CREATE TABLE PExchange_Request (
    exchange_id INT PRIMARY KEY,
    request_id INT UNIQUE,
    FOREIGN KEY (request_id) REFERENCES PDonation_Request(request_id)
);

-- PEXCHANGE_DONOR
CREATE TABLE PExchange_Donor (
    exchange_id INT,
    donor_id INT,
    health_test_passed CHAR(1) CHECK (health_test_passed IN ('Y', 'N')),
    PRIMARY KEY (exchange_id, donor_id),
    FOREIGN KEY (exchange_id) REFERENCES PExchange_Request(exchange_id),
    FOREIGN KEY (donor_id) REFERENCES PDonor(donor_id)
);

-- PPAYMENT_METHOD
CREATE TABLE PPayment_Method (
    method_id INT PRIMARY KEY,
    method_name VARCHAR(50)
);

-- PPAYMENT
CREATE TABLE PPayment (
    payment_id INT PRIMARY KEY,
    request_id INT,
    method_id INT,
    amount DECIMAL(10,2) ,
    payment_date DATE,
    FOREIGN KEY (request_id) REFERENCES PDonation_Request(request_id),
    FOREIGN KEY (method_id) REFERENCES PPayment_Method(method_id)
);

-- PBLOOD_COMPATIBILITY
CREATE TABLE PBlood_Compatibility (
    donor_group VARCHAR(5),
    recipient_group VARCHAR(5),
    PRIMARY KEY (donor_group, recipient_group)
);