# Loan Dataset Processing

## Project Overview

This project involves the processing and analysis of a loan dataset with the incorporation of machine learning models to predict loan approval outcomes. Through various data processing steps, exploratory data analysis (EDA), and machine learning models, this project aims to uncover insights from the data and predict loan approval status based on several factors.

## Getting Started

### Prerequisites

- Python
- Jupyter Notebook or JupyterLab
- Dependencies in requirements.txt

## Data

The dataset used in this project is "Loan_Dataset.xlsx", which contains various attributes related to loan applications, such as FICO score, employment status, lender information, and approval status throughout 100,000 entries.

## Project Structure

1. Data Loading: Load the loan dataset and display basic information.
2. Data Verification: Verify data integrity and constraints.
3. Data Sanitation: Clean and preprocess the dataset for analysis.
4. Exploratory Data Analysis (EDA): Perform EDA to uncover trends and relationships in the data.
5. Machine Learning Models: Train and evaluate several machine learning models to predict loan approval status.
6. View: Connect a frontend basic HTML/JS view to joblib packages of the models so that users can interact with them freely.

## Setup and Usage

1. **Install and Setup Virtual Environment:**

   - Ensure you have Python installed on your system.
   - Open a terminal and navigate to the project directory.
   - Run the following commands:

     ```bash
     # Install virtualenv using pip
     pip install virtualenv

     # Create a virtual environment named '.venv'
     python -m venv .venv
     ```

2. **Activate Virtual Environment:**

   - On Mac/Linux, activate the virtual environment:
     ```bash
     source .venv/bin/activate
     ```

3. **Install Dependencies:**

   - With the virtual environment activated, install project dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run Flask Application:**

   - Start the Flask backend server:
     ```bash
     python app.py
     ```
     Ensure the backend server is running at [http://127.0.0.1:5000](http://127.0.0.1:5000).

5. **Open the Web Interface:**

   - Open a new terminal window (while keeping the virtual environment active).
   - Run the following command to open the web interface in your default browser:
     ```bash
     open index.html
     ```
     If you prefer a different browser, copy and paste the provided link at the top of your default browser into the browser of your choosing.

6. **Interact with the Application:**

   - You can now interact with the data analysis application through the provided user interface. You will be able to fill out information about any applicant in order to see their approval odds with each lender based on the machine learning model. This will aid in promotional offers.

7. **Deactivate Virtual Environment:**
   - When finished, deactivate the virtual environment:
     ```bash
     deactivate
     ```

## Key Findings

- **Exploratory Data Analysis (EDA):** The analysis uncovered significant correlations between loan approval rates and several factors, including FICO scores, monthly gross income, and the debt-to-income ratio, highlighting their importance in the loan approval process.

- **Machine Learning Model Comparison:** We evaluated the performance of three models: Logistic Regression, Random Forest, and Gradient Boosting. The Random Forest model emerged as the superior choice for predicting loan approvals, offering insightful predictions that can guide which lender might be best for specific customer profiles.

- **Further Insights:** The "data_processor.ipynb" jupyter notebook contains detailed markdown comments and visual representations of our findings, providing a comprehensive view of our data analysis and modeling efforts.

## Future Improvements

- **Enhanced Analytics:**

  - Insights into outliers affecting data. Further research into contributing factors within loan approval and comparison to data provided. Overall improvement of ML model.

- **UI Experience:**
  - Transition from vanilla JavaScript to React for a more concise codebase and improved user interface with added functionality to handle missing variables or parameters and dynamic confidence rates.
