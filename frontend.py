import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🏥",
    layout="centered"
)

st.title("Insurance Premium Category Predictor")
st.markdown("Enter your details below to predict your insurance premium category.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.70, format="%.2f")
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are you a smoker?",[False, True])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox("Occupation",
[
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job"
    ]
)

if st.button("Predict Premium Category", use_container_width=True):

    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }

    try:
        with st.spinner("Predicting..."):
            response = requests.post(
                API_URL,
                json=input_data,
                timeout=10
            )

        if response.status_code == 200:
            result = response.json()
            prediction = result.get("predicted_category")
            st.success(
                f"Predicted Insurance Premium Category: **{prediction}**"
            )

        else:
            st.error(f"API Error: {response.status_code}")
            st.json(response.json())

    except requests.exceptions.ConnectionError:
        st.error(
            "Could not connect to the FastAPI server.\n\n"
            "Make sure FastAPI is running:\n"
            "uvicorn app:app --reload"
        )

    except Exception as e:
        st.error(f"Unexpected Error: {e}")