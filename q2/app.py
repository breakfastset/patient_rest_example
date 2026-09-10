from flask import Flask, jsonify, request
from patient_collection import *

app = Flask(__name__)

@app.route("/")
def main_page():
    """Index page."""
    return """
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Patient</title>
    </head>
    <body>
        <h1>Welcome to ABC Clinic</h1>
    </body>
    </html>
    """

@app.route("/patient/search", methods=["POST", "GET"])
def patient_search():
    """Search and return a valid Patient in json format."""
    patients = load_data("patients.json")

    # user request
    features = request.json
    search_phrase = features["search_phrase"]

    response = {}
    index = 0
    found = False
    target_patient = None

    while index < len(patients) and not found:
        if str(patients[index].patient_id) == search_phrase or patients[index].id_no == search_phrase:
            target_patient = patients[index]
            found = True
        index += 1

    if target_patient is not None:
        response = {"patient_id" : target_patient.patient_id, "surname" : target_patient.surname,
                    "given_name" : target_patient.given_name}

    return jsonify(response)



if __name__ == "__main__":
    app.run(port=5555)