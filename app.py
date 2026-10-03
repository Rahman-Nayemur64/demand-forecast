import streamlit as st
import pandas as pd
import numpy as np
import pickle 

@st.cache_resource
def load_artifact():
    with open('xgbboost_demand_forecasting_model.pkl', 'rb') as file:
        model = pickle.load(file)
        
    with open("label_encoder.pkl", "rb") as file:
        encoders = pickle.load(file)

    return model, encoders

model, label_encoders = load_artifact()

st.title("Demand Forecasting Application App")
st.divider()
st.header("Input Features")

price = st.number_input("Price", min_value=0.0, value = 50.0)
discount = st.number_input("Discount", min_value=0.0, max_value=100.0, value = 5.0)
inventory = st.number_input("Inventory", min_value=0, value = 100)
promotion = st.selectbox("Promotion", [0,1])
competitor_price = st.number_input("Competitor Price", min_value=0.0, value = 45.0)

category = st.selectbox("Category", ["Electronics", "Clothing", "Home & Kitchen", "Sports", "Books"])

input_data = pd.DataFrame({
    "Price": [price],
    "Discount": [discount],
    "Inventory": [inventory],   
    "Promotion": [promotion],
    "Competitor_Price": [competitor_price],
    "Category": [category]
})

for col, encoder in label_encoders.items():
    if col in input_data.columns:
        input_data[col] = encoder.transform(input_data[col])
        
st.divider()

if st.button("Predict Demand"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Demand: {prediction[0]:.2f}")