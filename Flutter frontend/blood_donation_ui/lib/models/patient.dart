class Patient {
  final int patientId;
  final String firstName;
  final String lastName;
  final String? bloodGroup;

  Patient({
    required this.patientId,
    required this.firstName,
    required this.lastName,
    this.bloodGroup,
  });

  factory Patient.fromJson(Map<String, dynamic> json) {
    return Patient(
      patientId: json['patient_id'],
      firstName: json['first_name'],
      lastName: json['last_name'],
      bloodGroup: json['blood_group'],
    );
  }
}