import pickle
import pickle
from flask import Flask, request
import requests
import os
app = Flask(__name__)

@app.route("/",methods=["GET"])
def ping():
    return "<H1>Loan approval application</H1>"

# Get the absolute path for classifier.pkl
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'classifier.pkl')


with open('classifier.pkl', 'rb') as model_pickle:
    clf = pickle.load(model_pickle)

@app.route("/predict",methods=["POST"]) # expecting input in the form JSON
def predictions():
    loan_req = request.get_json()

    if loan_req['Gender'] == "Male":
        Gender = 0
    else:
        Gender = 1

    if loan_req['Married'] == "Unmarried":
        Married = 0
    else:
        Married = 1

    ApplicantIncome = loan_req['ApplicantIncome']
    LoanAmount = loan_req['LoanAmount']
    Credit_History = loan_req['Credit_History']

    result = clf.predict([[Gender,Married,ApplicantIncome,LoanAmount,Credit_History]])

    if result == 0:
        pred = 'Rejected'

    else:
        pred = 'Approved'

    return {'Loan_approval_status ': pred}

if __name__ == "__main__":
    app.run(debug=True)  # Add this to ensure the Flask app runs