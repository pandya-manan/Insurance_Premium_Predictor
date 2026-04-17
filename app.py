import streamlit as st
import numpy as np
import pickle

# Load model and feature order
model = pickle.load(open('model.pkl', 'rb'))
features = pickle.load(open('features.pkl', 'rb'))

st.set_page_config(page_title="Insurance Premium Predictor")

st.title("🏥 Insurance Premium Prediction App")
st.write("Enter details to predict insurance premium")

# ---------------- INPUTS ---------------- #

age = st.number_input("Age", 18, 100, 30)

gender = st.selectbox("Gender", ["Female", "Male"])

marital_status = st.selectbox("Marital Status", ["Unmarried", "Married"])

dependants = st.slider("Dependants", 0, 5, 0)

income = st.number_input("Income (Lakhs)", min_value=1.0, value=10.0)

bmi = st.selectbox("BMI Category", ["Underweight", "Normal", "Overweight", "Obesity"])

smoking = st.selectbox("Smoking Status", ["No Smoking", "Occasional", "Regular"])

plan = st.selectbox("Insurance Plan", ["Bronze", "Silver", "Gold"])

region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])

employment = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Freelancer"])

physical_activity = st.selectbox("Physical Activity", ["High", "Medium", "Low"])

stress_level = st.selectbox("Stress Level", ["Low", "Medium", "High"])

# Diseases
st.subheader("Medical Conditions")

diabetes = st.checkbox("Diabetes")
high_bp = st.checkbox("High Blood Pressure")
heart_disease = st.checkbox("Heart Disease")
thyroid = st.checkbox("Thyroid")

# ---------------- FEATURE ENGINEERING ---------------- #

# Binary encoding
gender = 0 if gender == "Female" else 1
marital_status = 0 if marital_status == "Unmarried" else 1

# Ordinal encoding
bmi_map = {"Underweight": 0, "Normal": 1, "Overweight": 2, "Obesity": 3}
smoking_map = {"No Smoking": 0, "Occasional": 1, "Regular": 2}
plan_map = {"Bronze": 0, "Silver": 1, "Gold": 2}

bmi = bmi_map[bmi]
smoking = smoking_map[smoking]
plan = plan_map[plan]

# Lifestyle score
activity_map = {"High": 0, "Medium": 1, "Low": 4}
stress_map = {"Low": 0, "Medium": 1, "High": 4}

life_style_risk_score = activity_map[physical_activity] + stress_map[stress_level]

# Disease features
diabetes = int(diabetes)
high_bp = int(high_bp)
heart_disease = int(heart_disease)
thyroid = int(thyroid)

disease_count = diabetes + high_bp + heart_disease + thyroid

# ---------------- ONE HOT ENCODING ---------------- #

# Region (Northeast is baseline)
region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0

# Employment (Freelancer is baseline)
employment_salaried = 1 if employment == "Salaried" else 0
employment_self = 1 if employment == "Self-Employed" else 0

# ---------------- CREATE INPUT DICT ---------------- #

input_dict = {
    'age': age,
    'gender': gender,
    'marital_status': marital_status,
    'dependants': dependants,
    'bmi_category': bmi,
    'smoking_status': smoking,
    'income_lakhs': income,
    'insurance_plan': plan,
    'region_Northwest': region_northwest,
    'region_Southeast': region_southeast,
    'region_Southwest': region_southwest,
    'life_style_risk_score': life_style_risk_score,
    'employment_status_Salaried': employment_salaried,
    'employment_status_Self-Employed': employment_self,
    'diabetes': diabetes,
    'high_bp': high_bp,
    'heart_disease': heart_disease,
    'thyroid': thyroid,
    'disease_count': disease_count
}

# Ensure correct feature order
input_data = np.array([input_dict[feature] for feature in features]).reshape(1, -1)

# ---------------- PREDICTION ---------------- #

if st.button("Predict Premium"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Annual Premium: ₹ {round(prediction, 2)}")