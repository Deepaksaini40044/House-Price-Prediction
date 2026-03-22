import streamlit as st
import requests

st.set_page_config(layout="wide")

# ===== CSS =====
st.markdown("""
<style>

/* BACKGROUND */
html, body, [data-testid="stAppViewContainer"] {
    background: url("https://images.unsplash.com/photo-1505761671935-60b3a7427bad") no-repeat center center fixed;
    background-size: cover;
}

/* BLUR OVERLAY */
[data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    backdrop-filter: blur(12px);
    background: rgba(0,0,0,0.35);
    z-index: 0;
}

/* REMOVE HEADER */
[data-testid="stHeader"] {
    background: transparent;
}

/* TITLE */
.title-box {
    width: 60%;
    margin: auto;
    margin-top: 30px;
    padding: 20px;
    border-radius: 25px;
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(20px);
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
}

/* CARD */
.container {
    width: 40%;
    margin: auto;
    margin-top: 25px;
    padding: 25px;
    border-radius: 25px;
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(25px);
}

/* REMOVE SPIN */
input[type=number]::-webkit-inner-spin-button, 
input[type=number]::-webkit-outer-spin-button { 
    -webkit-appearance: none; 
}

/* LABEL */
label {
    color: white !important;
    font-weight: bold;
}

/* INPUT */
div[data-baseweb="input"] > div {
    background: rgba(255,255,255,0.85) !important;
    border-radius: 10px !important;
}

/* BUTTON CENTER */
.stButton {
    display: flex;
    justify-content: center;
}

.stButton>button {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    border-radius: 30px;
    width: 200px;
    height: 50px;
    font-size: 16px;
}

/* RESULT */
.result {
    text-align: center;
    color: white;
    font-size: 22px;
    margin-top: 15px;
}

</style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.markdown('<div class="title-box">🏠 House Price Prediction</div>', unsafe_allow_html=True)

# ===== CENTER =====
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown('<div class="container">', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        Total_Bedrooms = st.number_input("Bedrooms", min_value=0)
        Total_Bathrooms = st.number_input("Bathrooms", min_value=0)
        Living_area = st.number_input("Living Area", min_value=0)
        Lot_area = st.number_input("Lot Area", min_value=0)
        Total_floors = st.number_input("Floors", min_value=0)
        House_condition = st.number_input("Condition", min_value=0)

    with c2:
        House_grade = st.number_input("Grade", min_value=0)
        Total_area = st.number_input("Total Area", min_value=0)
        Basement_area = st.number_input("Basement", min_value=0)
        Built_year = st.number_input("Built Year", min_value=1900)
        Renovation_year = st.number_input("Renovation Year", min_value=0)
        School_nearby = st.number_input("School Nearby", min_value=0)
        Airport_distance = st.number_input("Airport Distance", min_value=0)

    # BUTTON
    if st.button("🚀 Predict Price"):

        data = {
            "Total_Bedrooms": Total_Bedrooms,
            "Total_Bathrooms": Total_Bathrooms,
            "Living_area": Living_area,
            "Lot_area": Lot_area,
            "Total_floors": Total_floors,
            "House_condition": House_condition,
            "House_grade": House_grade,
            "Total_area": Total_area,
            "Basement_area": Basement_area,
            "Built_year": Built_year,
            "Renovation_year": Renovation_year,
            "School_nearby": School_nearby,
            "Airport_distance": Airport_distance
        }

        # ===== VALIDATION =====
        if any(v == 0 for v in data.values()):
            st.warning("⚠️ Please fill all fields with valid values!")
        
        else:
            url = "http://localhost:8000/predict"

            with st.spinner("Predicting..."):
                try:
                    res = requests.post(url, json=data)
                    result = res.json()

                    price = result["Predicted_price"] / 100000

                    st.markdown(f'<div class="result">💰 ₹ {price:.2f} Lakhs</div>', unsafe_allow_html=True)

                except:
                    st.error("API Error")

    st.markdown('</div>', unsafe_allow_html=True)