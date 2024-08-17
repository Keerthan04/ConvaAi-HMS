from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/patient/details', methods=['POST'])
def get_patient_details():
    data = request.json
    patient_name = data.get('name')
    
    # Replace this with actual retrieval logic using Convo AI or a database
    patient_data = {
        "details": f"Name: {patient_name}, Age: 30, Blood Group: O+",
        "medical_history": "Hypertension, Diabetes",
        "upcoming_appointments": "12th Aug 2024 - Dr. Smith, 14th Aug 2024 - Dr. Brown",
        "done_appointments": "10th Aug 2024 - Dr. Green",
        "recommended_tests": "Blood Test, MRI",
        "test_results": "Blood Test: Normal, MRI: Pending"
    }
    return jsonify(patient_data)

@app.route('/doctor/details', methods=['POST'])
def get_doctor_details():
    data = request.json
    doctor_name = data.get('name')
    
    # Replace this with actual retrieval logic using Convo AI or a database
    doctor_data = {
        "details": f"Name: Dr. {doctor_name}, Cardiologist, 10 years of experience",
        "upcoming_appointments": "12th Aug 2024 - John Doe, 14th Aug 2024 - Jane Doe"
    }
    return jsonify(doctor_data)

if __name__ == "__main__":
    app.run(debug=True)
