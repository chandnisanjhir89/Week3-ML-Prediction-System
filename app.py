import streamlit as st
import joblib
import numpy as np

# Load Model
import os
model = joblib.load(os.path.join(os.path.dirname(__file__), "diabetes_model.pkl"))
# App Title
st.title("Diabetes Prediction System")

st.write("Enter patient details to predict diabetes risk.")

# User Inputs
gender = st.selectbox("Gender", [0, 1])

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100,
    value=30
)

hypertension = st.selectbox(
    "Hypertension",
    [0, 1]
)

heart_disease = st.selectbox(
    "Heart Disease",
    [0, 1]
)

smoking_history = st.selectbox(
    "Smoking History",
    [0, 1, 2, 3, 4, 5]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

hba1c = st.number_input(
    "HbA1c Level",
    min_value=3.0,
    max_value=15.0,
    value=5.5
)

blood_glucose = st.number_input(
    "Blood Glucose Level",
    min_value=50,
    max_value=300,
    value=100
)

# Prediction Button
if st.button("Predict"):

    input_data = np.array([
        [
            gender,
            age,
            hypertension,
            heart_disease,
            smoking_history,
            bmi,
            hba1c,
            blood_glucose
        ]
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("High Risk: Diabetes Detected")
    else:
        st.success("Low Risk: No Diabetes Detected")
        
