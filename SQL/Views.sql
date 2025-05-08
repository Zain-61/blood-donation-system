-- View for fetching all users with their roles
CREATE OR REPLACE VIEW VUserRoles AS
SELECT u.user_id, u.username, u.email, u.phone,
       CASE
           WHEN p.patient_id IS NOT NULL THEN 'Patient'
           WHEN d.donor_id IS NOT NULL THEN 'Donor'
           WHEN a.admin_id IS NOT NULL THEN 'Administrator'
           WHEN m.staff_id IS NOT NULL THEN 'Medical Staff'
           WHEN o.organizer_id IS NOT NULL THEN 'Organizer'
           ELSE 'Unknown'
       END AS role
FROM PUser_Account u
LEFT JOIN PPatient p ON u.user_id = p.user_id
LEFT JOIN PDonor d ON u.user_id = d.user_id
LEFT JOIN PAdministrator a ON u.user_id = a.user_id
LEFT JOIN PMedical_Staff m ON u.user_id = m.user_id
LEFT JOIN POrganizer o ON u.user_id = o.user_id;

-- View for fetching blood inventory details
CREATE OR REPLACE VIEW VBloodInventoryDetails AS
SELECT i.inventory_id, b.bank_name , b.bank_location, i.blood_group,
       t.cost_per_unit, t.rare_type, i.units_available
FROM PBlood_Inventory i
JOIN PBlood_Bank b ON i.bank_id = b.bank_id
JOIN PBlood_Type_Info t ON i.blood_group = t.blood_group;

-- View for fetching camp and donor details
CREATE OR REPLACE VIEW VCampDonorDetails AS
SELECT dc.camp_id, dc.camp_name, dc.camp_date, dc.camp_location,
       o.organization_name, d.donor_id, d.blood_group, d.last_donation_date
FROM PDonation_Camp dc
JOIN POrganizer o ON dc.organizer_id = o.organizer_id
JOIN PDonation dn ON dc.camp_id = dn.camp_id
JOIN PDonor d ON dn.donor_id = d.donor_id;

-- View for fetching donation details with patient requests
CREATE OR REPLACE VIEW VDonationRequestDetails AS
SELECT dr.request_id, p.patient_id, p.user_id, dr.blood_group, dr.units_required,
       dr.request_date, dr.fulfilled, d.donor_id, d.last_donation_date
FROM PDonation_Request dr
LEFT JOIN PPatient p ON dr.patient_id = p.patient_id
LEFT JOIN PExchange_Donor ed ON dr.request_id = ed.exchange_id
LEFT JOIN PDonor d ON ed.donor_id = d.donor_id;