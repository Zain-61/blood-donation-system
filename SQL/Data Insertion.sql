INSERT INTO PUser_Account (username, password, email, phone) VALUES ('user1', 'password123', 'user1@example.com', '1234567890');
INSERT INTO PUser_Account (username, password, email, phone) VALUES ('user2', 'password456', 'user2@example.com', '1234567891');
INSERT INTO PUser_Account (username, password, email, phone) VALUES ('user3', 'password789', 'user3@example.com', '1234567892');
INSERT INTO PUser_Account (username, password, email, phone) VALUES ('user4', 'password000', 'user4@example.com', '1234567893');
INSERT INTO PUser_Account (username, password, email, phone) VALUES ('user5', 'password111', 'user5@example.com', '1234567894');
INSERT INTO PUser_Account (username, password, email, phone) VALUES ('user7', 'password111', 'user7@example.com', '1234567877');

INSERT INTO PPatient (user_id, blood_group, medical_history) VALUES (1, 'A+', 'None');
INSERT INTO PPatient (user_id, blood_group, medical_history) VALUES (2, 'O-', 'Asthma');
INSERT INTO PPatient (user_id, blood_group, medical_history) VALUES (3, 'B+', 'Diabetes');
INSERT INTO PPatient (user_id, blood_group, medical_history) VALUES (4, 'AB-', 'Hypertension');
INSERT INTO PPatient (user_id, blood_group, medical_history) VALUES (5, 'O+', 'None');

INSERT INTO PPatient_Contact (patient_id, contact_name, relationship, contact_phone) VALUES (1, 'John Doe', 'Father', '0987654321');
INSERT INTO PPatient_Contact (patient_id, contact_name, relationship, contact_phone) VALUES (2, 'Jane Doe', 'Mother', '0987654322');
INSERT INTO PPatient_Contact (patient_id, contact_name, relationship, contact_phone) VALUES (3, 'Mary Smith', 'Sister', '0987654323');
INSERT INTO PPatient_Contact (patient_id, contact_name, relationship, contact_phone) VALUES (4, 'Peter Brown', 'Brother', '0987654324');
INSERT INTO PPatient_Contact (patient_id, contact_name, relationship, contact_phone) VALUES (5, 'Lucas White', 'Uncle', '0987654325');


INSERT INTO PDonor (user_id, blood_group, last_donation_date)
VALUES (1, 'A+', DATE '2025-04-01');
INSERT INTO PDonor (user_id, blood_group, last_donation_date)
VALUES (2, 'O-', DATE '2025-03-01');
INSERT INTO PDonor (user_id, blood_group, last_donation_date)
VALUES (3, 'B+', DATE '2025-02-01');
INSERT INTO PDonor (user_id, blood_group, last_donation_date)
VALUES (4, 'AB-', DATE '2025-01-01');
INSERT INTO PDonor (user_id, blood_group, last_donation_date)
VALUES (5, 'O+', DATE '2025-02-01');

INSERT INTO PDonor_HealthCondition (donor_id, condition_name, condition_details) VALUES (1, 'None', 'No health conditions');
INSERT INTO PDonor_HealthCondition (donor_id, condition_name, condition_details) VALUES (2, 'Asthma', 'Mild asthma');
INSERT INTO PDonor_HealthCondition (donor_id, condition_name, condition_details) VALUES (3, 'Diabetes', 'Type 2');
INSERT INTO PDonor_HealthCondition (donor_id, condition_name, condition_details) VALUES (4, 'Hypertension', 'High blood pressure');
INSERT INTO PDonor_HealthCondition (donor_id, condition_name, condition_details) VALUES (5, 'None', 'No health conditions');

INSERT INTO PAdministrator (user_id, designation) VALUES (1, 'Manager');
INSERT INTO PAdministrator (user_id, designation) VALUES (2, 'Coordinator');
INSERT INTO PAdministrator (user_id, designation) VALUES (3, 'Supervisor');
INSERT INTO PAdministrator (user_id, designation) VALUES (4, 'Assistant');
INSERT INTO PAdministrator (user_id, designation) VALUES (5, 'Executive');


INSERT INTO PMedical_Staff (user_id, qualification) VALUES (1, 'MBBS');
INSERT INTO PMedical_Staff (user_id, qualification) VALUES (2, 'MD');
INSERT INTO PMedical_Staff (user_id, qualification) VALUES (3, 'PhD');
INSERT INTO PMedical_Staff (user_id, qualification) VALUES (4, 'BDS');
INSERT INTO PMedical_Staff (user_id, qualification) VALUES (5, 'MS');

INSERT INTO POrganizer (user_id, organization_name) VALUES (1, 'Red Cross');
INSERT INTO POrganizer (user_id, organization_name) VALUES (2, 'Green Crescent');
INSERT INTO POrganizer (user_id, organization_name) VALUES (3, 'Blood Donors Society');
INSERT INTO POrganizer (user_id, organization_name) VALUES (4, 'Health for All');
INSERT INTO POrganizer (user_id, organization_name) VALUES (5, 'Life Savers');

INSERT INTO PDonation_Camp (camp_name, camp_date, camp_location, organizer_id) VALUES ('Summer Blood Drive', DATE '2025-06-01', 'City Hall', 1);
INSERT INTO PDonation_Camp (camp_name, camp_date, camp_location, organizer_id) VALUES ('Winter Blood Drive', DATE '2025-12-01', 'Main Square', 2);
INSERT INTO PDonation_Camp (camp_name, camp_date, camp_location, organizer_id) VALUES ('Spring Blood Drive', DATE '2025-03-01', 'University Campus', 3);
INSERT INTO PDonation_Camp (camp_name, camp_date, camp_location, organizer_id) VALUES ('Autumn Blood Drive', DATE '2025-09-01', 'Community Center', 4);
INSERT INTO PDonation_Camp (camp_name, camp_date, camp_location, organizer_id) VALUES ('Holiday Blood Drive',DATE '2025-12-15', 'Shopping Mall', 5);

INSERT INTO PBlood_Bank (bank_name, bank_location) VALUES ('City Blood Bank', 'Downtown');
INSERT INTO PBlood_Bank (bank_name, bank_location) VALUES ('Westside Blood Bank', 'Westside District');
INSERT INTO PBlood_Bank (bank_name, bank_location) VALUES ('Eastside Blood Bank', 'Eastside District');
INSERT INTO PBlood_Bank (bank_name, bank_location) VALUES ('North Blood Bank', 'North City');
INSERT INTO PBlood_Bank (bank_name, bank_location) VALUES ('South Blood Bank', 'South District');

INSERT INTO PBlood_Type_Info (blood_group, cost_per_unit, rare_type) VALUES ('A+', 100.00, 'N');
INSERT INTO PBlood_Type_Info (blood_group, cost_per_unit, rare_type) VALUES ('O-', 150.00, 'Y');
INSERT INTO PBlood_Type_Info (blood_group, cost_per_unit, rare_type) VALUES ('B+', 120.00, 'N');
INSERT INTO PBlood_Type_Info (blood_group, cost_per_unit, rare_type) VALUES ('AB-', 200.00, 'Y');
INSERT INTO PBlood_Type_Info (blood_group, cost_per_unit, rare_type) VALUES ('O+', 110.00, 'N');

INSERT INTO PBlood_Inventory (bank_id, blood_group, units_available) VALUES (1, 'A+', 50);
INSERT INTO PBlood_Inventory (bank_id, blood_group, units_available) VALUES (2, 'O-', 30);
INSERT INTO PBlood_Inventory (bank_id, blood_group, units_available) VALUES (3, 'B+', 60);
INSERT INTO PBlood_Inventory (bank_id, blood_group, units_available) VALUES (4, 'AB-', 10);
INSERT INTO PBlood_Inventory (bank_id, blood_group, units_available) VALUES (5, 'O+', 80);

INSERT INTO PDonation (donor_id, camp_id, donation_date, units_donated) VALUES (1, 1, DATE '2025-04-01', 2);
INSERT INTO PDonation (donor_id, camp_id, donation_date, units_donated) VALUES (2, 2, DATE '2025-03-01', 1);
INSERT INTO PDonation (donor_id, camp_id, donation_date, units_donated) VALUES (3, 3, DATE '2025-02-01', 3);
INSERT INTO PDonation (donor_id, camp_id, donation_date, units_donated) VALUES (4, 4, DATE '2025-01-01', 2);
INSERT INTO PDonation (donor_id, camp_id, donation_date, units_donated) VALUES (5, 5, DATE '2025-05-01', 1);

INSERT INTO PDonation_Request (patient_id, blood_group, units_required, request_date, fulfilled) VALUES (1, 'A+', 2, DATE '2025-05-01', 'N');
INSERT INTO PDonation_Request (patient_id, blood_group, units_required, request_date, fulfilled) VALUES (2, 'O-', 1, DATE '2025-04-15', 'Y');
INSERT INTO PDonation_Request (patient_id, blood_group, units_required, request_date, fulfilled) VALUES (3, 'B+', 3, DATE '2025-03-01', 'N');
INSERT INTO PDonation_Request (patient_id, blood_group, units_required, request_date, fulfilled) VALUES (4, 'AB-', 2, DATE '2025-02-15', 'Y');
INSERT INTO PDonation_Request (patient_id, blood_group, units_required, request_date, fulfilled) VALUES (5, 'O+', 1, DATE '2025-05-01', 'N');

INSERT INTO PExchange_Request (request_id) VALUES (1);
INSERT INTO PExchange_Request (request_id) VALUES (2);
INSERT INTO PExchange_Request (request_id) VALUES (3);
INSERT INTO PExchange_Request (request_id) VALUES (4);
INSERT INTO PExchange_Request (request_id) VALUES (5);


INSERT INTO PExchange_Donor (exchange_id, donor_id, health_test_passed) VALUES (1, 1, 'Y');
INSERT INTO PExchange_Donor (exchange_id, donor_id, health_test_passed) VALUES (2, 2, 'N');
INSERT INTO PExchange_Donor (exchange_id, donor_id, health_test_passed) VALUES (3, 3, 'Y');
INSERT INTO PExchange_Donor (exchange_id, donor_id, health_test_passed) VALUES (4, 4, 'N');
INSERT INTO PExchange_Donor (exchange_id, donor_id, health_test_passed) VALUES (5, 5, 'Y');

INSERT INTO PPayment_Method (method_name) VALUES ('Credit Card');
INSERT INTO PPayment_Method (method_name) VALUES ('Debit Card');
INSERT INTO PPayment_Method (method_name) VALUES ('PayPal');
INSERT INTO PPayment_Method (method_name) VALUES ('Bank Transfer');
INSERT INTO PPayment_Method (method_name) VALUES ('Cash');

INSERT INTO PPayment (request_id, method_id, amount, payment_date) VALUES (1, 1, 200.00, DATE '2025-05-02');
INSERT INTO PPayment (request_id, method_id, amount, payment_date) VALUES (2, 2, 100.00, DATE '2025-04-16');
INSERT INTO PPayment (request_id, method_id, amount, payment_date) VALUES (3, 3, 300.00, DATE '2025-03-05');
INSERT INTO PPayment (request_id, method_id, amount, payment_date) VALUES (4, 4, 400.00, DATE '2025-02-20');
INSERT INTO PPayment (request_id, method_id, amount, payment_date) VALUES (5, 5, 150.00, DATE '2025-05-05');

-- O- can donate to everyone (universal donor)
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'O-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'O+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'A-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'A+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'B-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'B+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'AB-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O-', 'AB+');

-- O+ can donate to O+, A+, B+, AB+
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O+', 'O+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O+', 'A+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O+', 'B+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('O+', 'AB+');

-- A- can donate to A-, A+, AB-, AB+
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('A-', 'A-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('A-', 'A+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('A-', 'AB-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('A-', 'AB+');

-- A+ can donate to A+, AB+
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('A+', 'A+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('A+', 'AB+');

-- B- can donate to B-, B+, AB-, AB+
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('B-', 'B-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('B-', 'B+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('B-', 'AB-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('B-', 'AB+');

-- B+ can donate to B+, AB+
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('B+', 'B+');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('B+', 'AB+');

-- AB- can donate to AB-, AB+
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('AB-', 'AB-');
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('AB-', 'AB+');

-- AB+ can donate to AB+ only (universal recipient)
INSERT INTO PBlood_Compatibility (donor_group, recipient_group) VALUES ('AB+', 'AB+');
