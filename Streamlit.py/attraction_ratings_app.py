import streamlit as st
import pandas as pd
from joblib import dump
from joblib import load
import pickle


# Title
st.title("🎡 Tourism Experience Analytics - Rating Prediction (LGBMRegressor)")

# Load encoders
encoders = load("models/encoder.joblib")

# Load LGBM model
lgbm = load("models/Regression_Task_Model/best_lgb_model.joblib")

# Set default values
default_country = "India"
default_city = "Kerala"
default_region = "South East Asia"
default_continent = "Asia"
default_attraction = "Sacred Monkey Forest Sanctuary"
default_attraction_type = "Nature & Wildlife Areas"
default_visit_mode = "Couples"

default_year = 2022
default_month = 10
default_userid = 70456
default_avg_rating_user = 1.0
default_avg_rating_attraction = 0.6

# Initialize session state for reset
if 'reset' not in st.session_state:
    st.session_state.reset = False

# Reset button function
def reset_form():
    st.session_state.Country = default_country
    st.session_state.CityName = default_city
    st.session_state.Region = default_region
    st.session_state.Continent = default_continent
    st.session_state.Attraction = default_attraction
    st.session_state.AttractionType = default_attraction_type
    st.session_state.VisitMode = default_visit_mode
    st.session_state.VisitYear = default_year
    st.session_state.VisitMonth = default_month
    st.session_state.UserId = default_userid
    st.session_state.AvgRatingUser = default_avg_rating_user
    st.session_state.AvgRatingAttraction = default_avg_rating_attraction

# MAIN TAB
tab1 = st.tabs(['LGBMRegressor Rating Prediction'])[0]

with tab1:
    try:
        # Form
        with st.form("prediction_form"):
            # Form fields
            Country = st.selectbox("Select Country", sorted(encoders['Country'].classes_), key="Country")
            CityName = st.selectbox("Select City", sorted(encoders['CityName'].classes_), key="CityName")
            Region = st.selectbox("Select Region", sorted(encoders['Region'].classes_), key="Region")
            Continent = st.selectbox("Select Continent", sorted(encoders['Continent'].classes_), key="Continent")
            Attraction = st.selectbox("Select Attraction", sorted(encoders['Attraction'].classes_), key="Attraction")
            AttractionType = st.selectbox("Select Attraction Type", sorted(encoders['AttractionType'].classes_), key="AttractionType")
            VisitMode = st.selectbox("Select Visit Mode", sorted(encoders['VisitMode'].classes_), key="VisitMode")
            VisitYear = st.selectbox("Select Visit Year", list(range(2013, 2030)), key="VisitYear")
            VisitMonth = st.selectbox("Select Visit Month", list(range(1, 13)), key="VisitMonth")
            UserId = st.number_input("User ID", min_value=0, step=1, key="UserId")
            AvgRatingUser = st.number_input("Average Rating per User", min_value=0.0, max_value=5.0, step=0.1, key="AvgRatingUser")
            AvgRatingAttraction = st.number_input("Average Rating per Attraction", min_value=0.0, max_value=5.0, step=0.1, key="AvgRatingAttraction")

            # Buttons
            predict_btn = st.form_submit_button("Predict Rating")
            reset_btn = st.form_submit_button("Reset Form", on_click=reset_form)

        # Display selected inputs in a table
        st.subheader("📋 Selected Input Data")
        input_data = {
            'UserId': [UserId],
            'VisitYear': [VisitYear],
            'VisitMonth': [VisitMonth],
            'VisitMode': [VisitMode],
            'Attraction': [Attraction],
            'AttractionType': [AttractionType],
            'CityName': [CityName],
            'Country': [Country],
            'Region': [Region],
            'Continent': [Continent],
            'Average rating per user': [AvgRatingUser],
            'Average rating per attraction': [AvgRatingAttraction]
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

            # Predict using LGBM model
            prediction = lgbm.predict(new_df)
            st.success(f"✅ Predicted Rating is: **{prediction[0]:.2f}** ⭐️ (using LGBMRegressor)")

    except Exception as e:
        st.error(f"Failed to fetch data: {e}")
