from pathlib import Path
import pickle

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "xgbboost_demand_forecasting_model.pkl"
ENCODER_PATH = BASE_DIR / "label_encoder.pkl"

@st.cache_resource
def load_artifact():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}. Upload the trained model to the app repo before deployment.")
    if not ENCODER_PATH.exists():
        raise FileNotFoundError(f"Encoder file not found: {ENCODER_PATH}. Upload the label encoder file to the app repo before deployment.")

    with MODEL_PATH.open("rb") as file:
        model = pickle.load(file)

    with ENCODER_PATH.open("rb") as file:
        encoders = pickle.load(file)

    return model, encoders

model, label_encoders = load_artifact()

st.title("Demand Forecasting Application App")
st.divider()
st.header("Input Features")

price = st.number_input("Price", min_value=0.0, value = 50.0)
discount = st.number_input("Discount", min_value=0.0, max_value=100.0, value = 5.0)
inventory = st.number_input("Inventory Level", min_value=0, value = 100)
promotion = st.selectbox("Promotion", [0,1])
competitor_price = st.number_input("Competitor Pricing", min_value=0.0, value = 45.0)

category = st.selectbox("Category", ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"])

input_data = pd.DataFrame({
    "Price": [price],
    "Discount": [discount],
    "Inventory Level": [inventory],
    "Promotion": [promotion],
    "Competitor Pricing": [competitor_price],
    "Category": [category]
})

for col, encoder in label_encoders.items():
    if col in input_data.columns:
        input_data[col] = encoder.transform(input_data[col])

feature_order = list(model.feature_names_in_)
input_data = input_data[feature_order]

st.divider()

if st.button("Predict Demand"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Demand: {prediction[0]:.2f}")