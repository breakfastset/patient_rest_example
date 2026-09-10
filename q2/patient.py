
class Patient:

    def __init__(self, patient_id, surname, given_name, dob, gender, id_no, address):
        """Initialize the Patient with initial values."""
        self.patient_id = patient_id
        self.surname = surname
        self.given_name = given_name
        self.dob = dob
        self.gender = gender
        self.id_no = id_no
        self.address = address

    def __str__(self):
        """Return a string representation of the Patient."""
        return (f"Patient {self.patient_id} Details: "
                f"\nName: {self.surname} {self.given_name} "
                f"\n Sex: {self.gender.title()}"
                f"\n DOB: {self.dob} "
                f"\n  ID: {self.id_no} "
                f"\nAddr: {self.address}")
