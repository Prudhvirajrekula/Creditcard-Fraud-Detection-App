# 💳 Credit Card Fraud Detection App

An interactive fraud detection tool built with **Streamlit** and **Random Forest**, using a real-world dataset of over 280,000 credit card transactions.

## 🔍 Project Overview

This app allows users to upload transaction data and receive fraud predictions instantly. It was developed as part of a data science portfolio to demonstrate end-to-end ML deployment and user interaction.

### ⚙️ Features
- Upload CSVs to detect fraudulent transactions
- Real-time prediction using a trained Random Forest model
- Summary counts of fraud vs non-fraud predictions
- Supports preprocessing with automatic feature alignment

## 📊 Dataset

- Source: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- Total rows: 284,807
- Fraud cases: ~0.17%
- All features are PCA-transformed except `Amount` and `Time`

## 🚀 Try the App (Live)
👉 [Click here to try it live](https://creditcard-fraud-detection-prudhviraj.streamlit.app/)

## 🛠 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/CreditCard-Fraud-Detection.git
cd CreditCard-Fraud-Detection
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Run Streamlit
```bash
streamlit run app.py
```

## 📁 Project Structure

```
📦 CreditCard-Fraud-Detection
├── app.py                 # Streamlit app
├── rf_model.pkl           # Trained RandomForest model
├── requirements.txt       # Python dependencies
├── creditcard.csv         # Original dataset (or use sample)
└── README.md              # You're here
```

## Screenshots
<img width="1917" height="1093" alt="CCFD" src="https://github.com/user-attachments/assets/65266837-0a4d-4052-98d5-271149b54689" />


## 🧠 Skills Demonstrated
- Data preprocessing & feature engineering
- Class imbalance handling (SMOTE)
- Model training & evaluation (Random Forest, AUC: 0.999)
- Interactive app development (Streamlit)
- Deployment & sharing
