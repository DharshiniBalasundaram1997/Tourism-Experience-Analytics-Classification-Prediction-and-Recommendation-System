import streamlit as st
import pandas as pd
from joblib import load
import pickle

# Title
st.title("🎡 Tourism Experience Analytics - User Visit Mode Prediction (LGBMClassifier)")

# Load encoders
encoders = load("models/encoder_visit_mode.joblib")

# Load LGBM model
lgbm = load("models/Classification_Task_Model/best_lgbm_model.joblib")

# Set default values
default_country = "United States"
default_city = "Pleasanton"
default_region = "South America"
default_continent = "America"
default_attraction_type = "Nature & Wildlife Areas"
default_year = 2022
default_month = 7
default_userid = 33716

# Initialize session state for reset
if 'reset' not in st.session_state:
    st.session_state.reset = False

# Reset button function
def reset_form():
    st.session_state.Country = default_country
    st.session_state.CityName = default_city
    st.session_state.Region = default_region
    st.session_state.Continent = default_continent
    st.session_state.AttractionType = default_attraction_type
    st.session_state.VisitYear = default_year
    st.session_state.VisitMonth = default_month
    st.session_state.UserId = default_userid

# MAIN TAB
tab1 = st.tabs(['LGBMClassifier Visit Mode Prediction'])[0]

with tab1:
    try:
        # Form
        with st.form("prediction_form"):
            # Form fields
            Country = st.selectbox("Select Country", sorted(encoders['Country'].classes_), key="Country")
            CityName = st.selectbox("Select City", sorted(encoders['CityName'].classes_), key="CityName")
            Region = st.selectbox("Select Region", sorted(encoders['Region'].classes_), key="Region")
            Continent = st.selectbox("Select Continent", sorted(encoders['Continent'].classes_), key="Continent")
            AttractionType = st.selectbox("Select Attraction Type", sorted(encoders['AttractionType'].classes_), key="AttractionType")
            VisitYear = st.selectbox("Select Visit Year", list(range(2013, 2030)), key="VisitYear")
            VisitMonth = st.selectbox("Select Visit Month", list(range(1, 13)), key="VisitMonth")
            UserId = st.number_input("User ID", min_value=0, step=1, key="UserId")

            # Buttons
            predict_btn = st.form_submit_button("Predict Visit Mode")
            reset_btn = st.form_submit_button("Reset Form", on_click=reset_form)

        # Display selected inputs in a table
        st.subheader("📋 Selected Input Data")
        input_data = {
            'UserId': [UserId],
            'VisitYear': [VisitYear],
            'VisitMonth': [VisitMonth],
            'AttractionType': [AttractionType],
            'CityName': [CityName],
            'Country': [Country],
            'Region': [Region],
            'Continent': [Continent]
        }
        input_df = pd.DataFrame(input_data)
        st.table(input_df)

        # After form submit
        if predict_btn:
            new_df = input_df.copy()

            # Apply encoders to categorical columns
            for col in new_df.columns:
                if col in encoders:
                    new_df[col] = encoders[col].transform(new_df[col].astype(str))

            # Predict using LGBMClassifier
            pred_encoded = lgbm.predict(new_df)[0]
            visit_mode_label = encoders['VisitMode'].inverse_transform([pred_encoded])[0]

            st.success(f"✅ Predicted Visit Mode is: **{visit_mode_label}** 🎯 (using LGBMClassifier)")

    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
