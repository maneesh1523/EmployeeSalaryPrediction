# EmployeeSalaryPrediction

# 💼 Employee Salary Prediction App

This is a simple **Machine Learning + Streamlit** web application that predicts an employee's salary based on their **years at the company** and **job rating**.

---

## 🚀 Features

- 📊 Takes input for:
  - Years at the company
  - Job rating
- 🤖 Predicts salary using a trained Linear Regression model
- 🎈 Shows predictions with clean formatting
- ✅ Easy-to-use Streamlit interface

---

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## 📁 Project Structure


---

## 🧠 How the Model Was Trained

1. Created a dummy dataset with:
   - `years_at_company`
   - `job_rate`
   - `salary`
2. Trained a `LinearRegression` model using Scikit-learn
3. Saved the trained model as `linearmodel.pkl` using `joblib`

> *(Training code is inside a separate notebook or script like `salary_training.ipynb`)*

---

## ⚙️ How to Run the App Locally

### 1. Clone or Download this Repository

```bash
git clone https://github.com/your-username/EmployeeSalaryPrediction.git
cd EmployeeSalaryPrediction

python -m venv .venv
source .venv/bin/activate       # On Mac/Linux
.venv\Scripts\activate          # On Windows

pip install -r requirements.txt


pip install streamlit scikit-learn pandas numpy joblib

streamlit run app.py

pip freeze > requirements.txt
