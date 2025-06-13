import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("rf_model.pkl")

# List of features the model was trained on
expected_features = [
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount', 'Hour'
]

# Streamlit app UI
st.title("💳 Credit Card Fraud Detection")
st.write("Upload a CSV file with transaction data to predict potential frauds.")

uploaded_file = st.file_uploader("Upload CSV with transaction features", type=["csv"])

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)

        # If 'Hour' column is missing, try computing it from 'Time' (optional)
        if 'Hour' not in data.columns and 'Time' in data.columns:
            data['Hour'] = (data['Time'] // 3600) % 24

        # Select only the features used during training
        data = data[expected_features]

        # Run model predictions
        preds = model.predict(data)

        # Display results
        st.subheader("Prediction Results")
        result_df = data.copy()
        result_df['Prediction'] = preds
        st.dataframe(result_df)

        # Count breakdown
        st.subheader("Fraud Count")
        st.write(result_df['Prediction'].value_counts().rename({0: 'Not Fraud', 1: 'Fraud'}))

    except Exception as e:
        st.error(f"🚫 Error processing file: {e}")