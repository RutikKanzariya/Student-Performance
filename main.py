import streamlit as st
import pandas as pd
import joblib

# Load model files
model = joblib.load("student_model.pkl")
scaler = joblib.load("scaler.pkl")
feature_names = joblib.load("Featurename.pkl")

# Page Config
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Performance Predictor")
st.write("Predict whether a student will PASS or FAIL.")

# ==========================
# User Inputs
# ==========================

gender = st.selectbox(
    "Gender",
    ["female", "male"]
)

race = st.selectbox(
    "Race/Ethnicity",
    [
        "group A",
        "group B",
        "group C",
        "group D",
        "group E"
    ]
)

parent_education = st.selectbox(
    "Parental Level of Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    [
        "free/reduced",
        "standard"
    ]
)

test_prep = st.selectbox(
    "Test Preparation Course",
    [
        "completed",
        "none"
    ]
)

# ==========================
# Prediction Button
# ==========================

if st.button("Predict"):

    # Create empty dataframe with training columns
    input_encoded = pd.DataFrame(
        0,
        index=[0],
        columns=feature_names
    )

    # Gender
    if gender == "male":
        input_encoded["gender_male"] = 1

    # Race
    if race == "group B":
        input_encoded["race/ethnicity_group B"] = 1

    elif race == "group C":
        input_encoded["race/ethnicity_group C"] = 1

    elif race == "group D":
        input_encoded["race/ethnicity_group D"] = 1

    elif race == "group E":
        input_encoded["race/ethnicity_group E"] = 1

    # Parent Education
    if parent_education == "bachelor's degree":
        input_encoded["parental level of education_bachelor's degree"] = 1

    elif parent_education == "high school":
        input_encoded["parental level of education_high school"] = 1

    elif parent_education == "master's degree":
        input_encoded["parental level of education_master's degree"] = 1

    elif parent_education == "some college":
        input_encoded["parental level of education_some college"] = 1

    elif parent_education == "some high school":
        input_encoded["parental level of education_some high school"] = 1

    # Lunch
    if lunch == "standard":
        input_encoded["lunch_standard"] = 1

    # Test Preparation
    if test_prep == "none":
        input_encoded["test preparation course_none"] = 1

    # Scale Data
    input_scaled = scaler.transform(input_encoded)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    # Probability
    probability = model.predict_proba(input_scaled)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ PASS")
        st.write(
            f"Confidence Score: {probability[1] * 100:.2f}%"
        )
    else:
        st.error("❌ FAIL")
        st.write(
            f"Confidence Score: {probability[0] * 100:.2f}%"
        )

    # Debug Section
    with st.expander("Show Encoded Features"):
        st.dataframe(input_encoded)