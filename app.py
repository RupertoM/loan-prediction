from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Get the path to the ml_models folder
ml_models_path = os.path.join(os.path.dirname(__file__), 'ml_models')

# Load models from file
random_forest_a = joblib.load(os.path.join(ml_models_path, 'random_forest_a.joblib'))
random_forest_b = joblib.load(os.path.join(ml_models_path, 'random_forest_b.joblib'))
random_forest_c = joblib.load(os.path.join(ml_models_path, 'random_forest_c.joblib'))

# Accuracies from jupyter notebook
model_accuracies = {
    'Lender A': 0.89,
    'Lender B': 0.92,
    'Lender C': 0.83,
}

model_columns = ['Loan_Amount', 'FICO_score', 'Employment_Status', 'Monthly_Gross_Income', 'Monthly_Housing_Payment', 'Debt_to_Income_Ratio']

@app.route('/predict', methods=['POST'])
def predict_loan_approval():
    data = request.get_json()
    applicant_info = np.array([
        data['loan_amount'], data['fico_score'], data['employment_status'],
        data['income'], data['monthly_payments'], data['dti']
    ]).reshape(1, -1)
    applicant_df = pd.DataFrame(applicant_info, columns=model_columns)
    
    results = {}
    for lender, model in [('Lender A', random_forest_a), ('Lender B', random_forest_b), ('Lender C', random_forest_c)]:
        loan_status = model.predict(applicant_df)[0]
        loan_probability = model.predict_proba(applicant_df)[0][1]
        results[lender] = {
            'loan_status': int(loan_status),
            'loan_probability': float(loan_probability),
            'model_accuracy': float(model_accuracies[lender])
        }
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
