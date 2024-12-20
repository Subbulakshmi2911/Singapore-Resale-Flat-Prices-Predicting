import streamlit as st
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #F4F4F4;
    }
    .main-header {
        text-align: center;
        color: #009999;
        margin-bottom: 20px;
    }
    .section-header {
        color: #333;
        font-size: 20px;
        margin-top: 30px;
    }
    .stButton>button {
        background-color: #009999;
        color: white;
        border-radius: 5px;
    }
    .stButton>button:hover {
        background-color: #006666;
    }
    .info-box {
        background-color: #E6FFFA;
        padding: 15px;
        border: 1px solid #00CCCC;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Main title
st.markdown("<h1 class='main-header'>Singapore Resale Flat Price Predicting</h1>", unsafe_allow_html=True)


with open(r"D:\ResaleFlatPrices\trained_Regression_df_model.pkl", 'rb') as df_file:
     df = pickle.load(df_file)



unique_Storey_Range=df['storey_range'].unique()
unique_flat_model=df['flat_model'].unique()

town_mapping = {
'LIM CHU KANG': 0,
 'ANG MO KIO': 1,
 'YISHUN': 2,
 'BEDOK': 3,
 'GEYLANG': 4,
 'JURONG EAST': 5,
 'BUKIT BATOK': 6,
 'CLEMENTI': 7,
 'JURONG WEST': 8,
 'QUEENSTOWN': 9,
 'TOA PAYOH': 10,
 'WOODLANDS': 11,
 'HOUGANG': 12,
 'SERANGOON': 13,
 'KALLANG/WHAMPOA': 14,
 'BUKIT PANJANG': 15,
 'TAMPINES': 16,
 'MARINE PARADE': 17,
 'CENTRAL AREA': 18,
 'CHOA CHU KANG': 19,
 'BUKIT MERAH': 20,
 'SEMBAWANG': 21,
 'PASIR RIS': 22,
 'BISHAN': 23,
 'SENGKANG': 24,
 'BUKIT TIMAH': 25,
 'PUNGGOL': 26}

flat_type_mapping={
'1 ROOM': 0,
'2 ROOM': 1,
'3 ROOM': 2,
'4 ROOM': 3,
'5 ROOM': 4,
'EXECUTIVE': 5,
'MULTI-GENERATION': 6}

flat_model_mapping={
'2-room': 0,
'3Gen': 1,
'Adjoined flat': 2,
'Apartment': 3,
'DBSS': 4,
'Improved': 5,
'Improved-Maisonette': 6,
'Maisonette': 7,
'Model A': 8,
'Model A-Maisonette': 9,
'Model A2': 10,
'Multi Generation': 11,
'New Generation': 12,
'Premium Apartment': 13,
'Premium Apartment Loft': 14,
'Premium Maisonette': 15,
'Simplified': 16,
'Standard': 17,
'Terrace': 18,
'Type S1': 19,
'Type S2': 20}

storey_range_mapping = {
    '01 TO 03': 2.0,
    '01 TO 05': 3.0,
    '04 TO 06': 5.0,
    '06 TO 10': 8.0,
    '07 TO 09': 11.0,
    '10 TO 12': 13.0,
    '11 TO 15': 14.0,
    '13 TO 15': 17.0,
    '16 TO 18': 18.0,
    '16 TO 20': 20.0,
    '19 TO 21': 23.0,
    '21 TO 25': 26.0,
    '22 TO 24': 28.0,
    '25 TO 27': 29.0,
    '26 TO 30': 32.0,
    '28 TO 30': 33.0,
    '31 TO 33': 35.0,
    '31 TO 35': 38.0,
    '34 TO 36': 41.0,
    '36 TO 40': 44.0,
    '37 TO 39': 47.0,
    '40 TO 42': 50.0
}


# Sidebar menu
with st.sidebar:
    select = option_menu("Main Menu", ["About", "Prediction Models"], 
                         icons=["house", "gear", "info-circle"], default_index=0,
                         styles={
                             "container": {"padding": "5px", "background-color": "#EFFBFF"},
                             "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px", "--hover-color": "#CCE5FF"},
                             "nav-link-selected": {"background-color": "#009999"},
                         })
if select == "About":

    # Header and Introduction
    st.header("🛠️ Skills Takeaway From This Project")
    st.markdown(
        """
        <ul>
            <li><strong>Python Scripting</strong></li>
            <li><strong>Data Preprocessing</strong></li>
            <li><strong>Exploratory Data Analysis (EDA)</strong></li>
            <li><strong>Streamlit Application Development</strong></li>
        </ul>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h3 class='section-header'>📖 Introduction</h3>", unsafe_allow_html=True)

    st.markdown(
        """
        ### :red[Overview:] 
        This project aims to construct a machine learning model and implement it as a user-friendly online application 
        to provide accurate predictions for **Resale Flat Prices in Singapore**. The prediction model is built using 
        past transactional data to ensure reliability and precision.
        """
    )

    # Project Summary or Visual
    with st.expander("🔍 Learn More About This Project"):
        st.write(
            """
            - **Technologies Used:** Python, Streamlit, Pandas, Scikit-learn
            - **Key Features:** User-friendly interface, accurate price prediction, interactive visualization
            - **Objective:** Empower users to estimate resale prices and make informed decisions.
            """
        )


    # Footer or Call-to-Action
    st.markdown(
        """
        ---
        ### ✨ Ready to explore? Navigate to the **Prediction Models** section in the sidebar!
        """,
        unsafe_allow_html=True
    )

    
    
    
# Load models only once at the start of the script
with open(r"D:\ResaleFlatPrices\trained_Regression_model.pkl", 'rb') as file_1:
    regression_model = pickle.load(file_1)

# Streamlit application
if select == "Prediction Models":
    st.markdown("# :red[Predicting Results based on Trained Model]")
    col1, col2 = st.columns(2)
    
    with col1:
        town = st.selectbox("Town", options=list(town_mapping.keys()))
        flat_type = st.selectbox("Flat Type", options=list(flat_type_mapping.keys()))
        storey_range = st.selectbox("Storey Range", list(storey_range_mapping.keys()))
        floor_sqm = st.number_input("Floor Area (sqm)", min_value=28.0, max_value=173.0, step=1.0)
        flat_model = st.selectbox("Flat Model", options=list(flat_model_mapping.keys()))
    
    with col2:
        year = st.number_input("Year Built", min_value=1990, max_value=2024, step=1)
        month = st.selectbox("Month", options=list(range(1, 13)))
        remaining_lease_months = st.number_input("Remaining Lease (Months)", min_value=48, max_value=1173, step=1)
        lease_commence_year = st.number_input("Lease Commencement Year", min_value=1966, max_value=2024, step=1)
   
    predict_button_1 = st.button("Predict Resale Price", type="primary")

    if predict_button_1:
        try:
            # Encode categorical inputs
            town_encoded = town_mapping[town]
            flat_type_encoded = flat_type_mapping[flat_type]
            flat_model_encoded = flat_model_mapping[flat_model]
            storey_avg = storey_range_mapping[storey_range]

            # Prepare input array
            new_sample_1 = np.array([
                [
                    month,
                    town_encoded,
                    flat_type_encoded,
                    floor_sqm,
                    flat_model_encoded,
                    lease_commence_year,
                    storey_avg,
                    remaining_lease_months,
                    year
                ]
            ])

            # Make prediction
            predicted_price = regression_model.predict(new_sample_1)[0]
            st.success(f"The predicted Resale Price is: **${predicted_price:,.2f}**")
        except KeyError as ke:
            st.error(f"Mapping error: {ke}. Ensure all inputs are correctly selected.")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
