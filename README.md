# Demand Forecasting App

A Streamlit web application for predicting product demand based on price, discount, inventory, promotion, competitor pricing, and product category.

## App Repository

- https://demand-forecast-kkt57qsc5tuw3sq3pckqst.streamlit.app/

## Overview

This project uses a trained machine learning model to estimate demand for a product. The app allows users to input business variables and receive a demand prediction instantly through the interface.

## Features

- Predict demand using a trained XGBoost model
- Input fields for:
  - Price
  - Discount
  - Inventory Level
  - Promotion
  - Competitor Pricing
  - Category
- Simple and interactive Streamlit dashboard

## Project Structure

- `app.py` – Streamlit app logic and prediction interface
- `demand_forecasting.csv` – dataset used for demand forecasting
- `demand_forecasting.ipynb` – notebook for model development and analysis
- `xgbboost_demand_forecasting_model.pkl` – trained prediction model
- `label_encoder.pkl` – category label encoder
- `requirements.txt` – Python dependencies


## Usage

1. Enter product information in the sidebar or form.
2. Click the Predict Demand button.
3. View the forecasted demand result.


