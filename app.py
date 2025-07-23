import streamlit as st
import joblib
import numpy as np

st.title("Salary Prediction APP")

st.divider()

st.write("With this app, You can get estimations for the salaries of the companies")

years = st.number_input("Enter the years at the company", value = 1, step = 1, min_value = 0)
jobRate = st.number_input("Enter the Job Rate", value = 3.5, step = 0.5, min_value = 0.0)

x = [years, jobRate]

model = joblib.load("linearmodel.pkl")


st.divider()

predict = st.button("Press the button for salary Prediction")

st.divider()

if predict:
    st.balloons()
    x1 = np.array([x])
    prediction = model.predict(x1)[0]

    st.write(f"salary prediction is {prediction:,.2f}")

else:
    "please press the button for app to make the predictions"
