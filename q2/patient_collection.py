from patient import Patient
import json

def load_data(filename="patients.json"):
    """Load data from json file to list of Patient objects and return."""
    patients = []

    # start of reading from json
    patient_db = open(filename, "r")
    json_data = json.load(patient_db)
    patient_dict_list = json_data["patients"]  # list of dictionaries loaded from json

    for patient_data in patient_dict_list:
        patient_id = patient_data["patient_id"]
        surname = patient_data["surname"]
        given_name = patient_data["given_name"]
        dob = patient_data["dob"]
        gender = patient_data["gender"]
        id_no = patient_data["id_no"]
        address = patient_data["address"]
        new_patient = Patient(patient_id, surname, given_name, dob, gender, id_no, address)   # create a Patient obj
        patients.append(new_patient)

    patient_db.close()
    # end of file reading

    return patients

def display_patients(patients):
    """Display Patient objects in a nicely formatted list."""
    for index in range(len(patients)):
        text = patients[index].__str__()
        print(f"{index + 1})\n{text}\n")

def search_patient(patients, target):
    """Search patient by patient id or id number."""
    for patient in patients:
        if patient.patient_id == target or patient.id_no == target:
            return patient
    return None


def main():
    """Test load_data()"""
    patients = load_data("patients.json")
    display_patients(patients)

    patient_1 = search_patient(patients, 128)
    patient_2 = search_patient(patients, "T0699333C")
    patient_3 = search_patient(patients, 999)

    if patient_1 is not None:
        print("1st search found: ")
        print(patient_1)
    else:
        print("Cannot find patient with id 128")
    print()

    if patient_2 is not None:
        print("2nd search found: ")
        print(patient_2)
    else:
        print("Cannot find patient with id T0699333C")
    print()

    if patient_3 is not None:
        print("3rd search found: ")
        print(patient_3)
    else:
        print("Cannot find patient with id 999")
    print()




if __name__ == '__main__':
    main()
