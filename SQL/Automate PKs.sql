CREATE SEQUENCE user_id_seq
START WITH 1 -- Set this to MAX(user_id) + 1
INCREMENT BY 1;

CREATE OR REPLACE TRIGGER trg_user_id
BEFORE INSERT ON PUser_Account
FOR EACH ROW
BEGIN
  IF :NEW.user_id IS NULL THEN
    SELECT user_id_seq.NEXTVAL INTO :NEW.user_id FROM dual;
  END IF;
END;
/




CREATE SEQUENCE patient_id_seq
START WITH 1 
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_patient_id
BEFORE INSERT ON PPatient
FOR EACH ROW
BEGIN
  IF :NEW.patient_id IS NULL THEN
    SELECT patient_id_seq.NEXTVAL INTO :NEW.patient_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE contact_id_seq
START WITH 1 -- Start with 1 or the next available ID
INCREMENT BY 1
NOCACHE; -- Ensure that the sequence is generated one at a time

CREATE OR REPLACE TRIGGER trg_contact_id
BEFORE INSERT ON PPatient_Contact
FOR EACH ROW
BEGIN
  IF :NEW.contact_id IS NULL THEN
    SELECT contact_id_seq.NEXTVAL INTO :NEW.contact_id FROM dual;
  END IF;
END;
/





CREATE SEQUENCE donor_id_seq
START WITH 1 -- Start with 1 or the next available ID
INCREMENT BY 1
NOCACHE; -- Ensure that the sequence is generated one at a time

CREATE OR REPLACE TRIGGER trg_donor_id
BEFORE INSERT ON PDonor 
FOR EACH ROW
BEGIN
  IF :NEW.donor_id IS NULL THEN
    SELECT donor_id_seq.NEXTVAL INTO :NEW.donor_id FROM dual;
  END IF;
END;
/




CREATE SEQUENCE request_id_seq
START WITH 1 -- Start with 1 or the next available ID
INCREMENT BY 1
NOCACHE; -- Ensure that the sequence is generated one at a time

CREATE OR REPLACE TRIGGER trg_request_id
BEFORE INSERT ON PDonation_Request
FOR EACH ROW
BEGIN
  IF :NEW.request_id IS NULL THEN
    SELECT request_id_seq.NEXTVAL INTO :NEW.request_id FROM dual;
  END IF;
END;
/




CREATE SEQUENCE inventory_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_inventory_id
BEFORE INSERT ON PBlood_Inventory
FOR EACH ROW
BEGIN
  IF :NEW.inventory_id IS NULL THEN
    SELECT inventory_id_seq.NEXTVAL INTO :NEW.inventory_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE camp_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;



CREATE OR REPLACE TRIGGER trg_camp_id
BEFORE INSERT ON PDonation_Camp
FOR EACH ROW
BEGIN
  IF :NEW.camp_id IS NULL THEN
    SELECT camp_id_seq.NEXTVAL INTO :NEW.camp_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE organizer_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_organizer_id
BEFORE INSERT ON POrganizer
FOR EACH ROW
BEGIN
  IF :NEW.organizer_id IS NULL THEN
    SELECT organizer_id_seq.NEXTVAL INTO :NEW.organizer_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE condition_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_condition_id
BEFORE INSERT ON PDonor_HealthCondition
FOR EACH ROW
BEGIN
  IF :NEW.condition_id IS NULL THEN
    SELECT condition_id_seq.NEXTVAL INTO :NEW.condition_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE admin_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_admin_id
BEFORE INSERT ON PAdministrator
FOR EACH ROW
BEGIN
  IF :NEW.admin_id IS NULL THEN
    SELECT admin_id_seq.NEXTVAL INTO :NEW.admin_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE staff_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_staff_id
BEFORE INSERT ON PMedical_Staff
FOR EACH ROW
BEGIN
  IF :NEW.staff_id IS NULL THEN
    SELECT staff_id_seq.NEXTVAL INTO :NEW.staff_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE bank_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_bank_id
BEFORE INSERT ON PBlood_Bank
FOR EACH ROW
BEGIN
  IF :NEW.bank_id IS NULL THEN
    SELECT bank_id_seq.NEXTVAL INTO :NEW.bank_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE exchange_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;

CREATE OR REPLACE TRIGGER trg_exchange_id
BEFORE INSERT ON PExchange_Request
FOR EACH ROW
BEGIN
  IF :NEW.exchange_id IS NULL THEN
    SELECT exchange_id_seq.NEXTVAL INTO :NEW.exchange_id FROM dual;
  END IF;
END;
/

CREATE SEQUENCE method_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;
CREATE OR REPLACE TRIGGER trg_method_id
BEFORE INSERT ON PPayment_Method
FOR EACH ROW
BEGIN
  IF :NEW.method_id IS NULL THEN
    SELECT method_id_seq.NEXTVAL INTO :NEW.method_id FROM dual;
  END IF;
END;
/

CREATE SEQUENCE payment_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;
CREATE OR REPLACE TRIGGER trg_payment_id
BEFORE INSERT ON PPayment
FOR EACH ROW
BEGIN
  IF :NEW.payment_id IS NULL THEN
    SELECT payment_id_seq.NEXTVAL INTO :NEW.payment_id FROM dual;
  END IF;
END;
/


CREATE SEQUENCE donation_id_seq
START WITH 1
INCREMENT BY 1
NOCACHE;
CREATE OR REPLACE TRIGGER trg_donation_id
BEFORE INSERT ON PDonation
FOR EACH ROW
BEGIN
  IF :NEW.donation_id IS NULL THEN
    SELECT donation_id_seq.NEXTVAL INTO :NEW.donation_id FROM dual;
  END IF;
END;
/


CREATE OR REPLACE TRIGGER trg_hash_password
BEFORE INSERT OR UPDATE ON PUser_Account
FOR EACH ROW
DECLARE
    hashed_password VARCHAR2(64);
BEGIN
    SELECT STANDARD_HASH(:NEW.password, 'SHA256')
    INTO hashed_password
    FROM dual;

    :NEW.password := hashed_password;
END;
/
