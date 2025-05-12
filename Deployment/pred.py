import streamlit as st
import joblib
import pandas as pd

# Load model
@st.cache_resource
def load_model():
    return joblib.load("svm_churn_model.pkl")

model = load_model()

# Feature names expected by the model
expected_columns = [
    "Subscription Length (Months)", "Customer Satisfaction Score (1-10)", 
    "Daily Watch Time (Hours)", "Engagement Rate (1-10)", 
    "Device Used Most Often", "Genre Preference", "Region", 
    "Payment History (On-Time/Delayed)", "Subscription Plan", 
    "Support Queries Logged", "Age", "Monthly Income ($)", 
    "Promotional Offers Used", "Number of Profiles Created"
]

# Categorical & numerical columns
categorical_cols = ["Device Used Most Often", "Genre Preference", "Region", 
                    "Payment History (On-Time/Delayed)", "Subscription Plan", 
                    "Promotional Offers Used"]
numerical_cols = ["Subscription Length (Months)", "Customer Satisfaction Score (1-10)", 
                  "Daily Watch Time (Hours)", "Engagement Rate (1-10)", 
                  "Support Queries Logged", "Age", "Monthly Income ($)", 
                  "Number of Profiles Created"]

def run():
    st.title("Netflix Churn Prediction")

    # User inputs
    device = st.selectbox("Device Used Most Often", ["Tablet", "Mobile", "Laptop", "Smart TV"])
    genre = st.selectbox("Genre Preference", ["Action", "Drama", "Comedy", "Sci-Fi"])
    region = st.selectbox("Region", ["North America", "Europe", "Asia", "South America"])
    payment = st.selectbox("Payment History", ["On-Time", "Delayed"])
    plan = st.selectbox("Subscription Plan", ["Basic", "Standard", "Premium"])
    
    promo = st.number_input("Promotional Offers Used", min_value=0, max_value=10, value=2)
    sub_length = st.number_input("Subscription Length (Months)", min_value=1, max_value=60, value=12)
    satisfaction = st.slider("Customer Satisfaction Score (1-10)", 1, 10, 8)
    watch_time = st.number_input("Daily Watch Time (Hours)", min_value=0.0, max_value=24.0, value=3.5)
    engagement = st.slider("Engagement Rate (1-10)", 1, 10, 7)
    support_queries = st.number_input("Support Queries Logged", min_value=0, max_value=50, value=1)
    age = st.number_input("Age", min_value=1, max_value=100, value=35)
    income = st.number_input("Monthly Income ($)", min_value=0, max_value=10000, value=5000)
    profiles = st.number_input("Number of Profiles Created", min_value=1, max_value=10, value=3)

    # Create DataFrame with correct order
    input_data = pd.DataFrame([[sub_length, satisfaction, watch_time, engagement, 
                                 device, genre, region, payment, plan, 
                                 support_queries, age, income, promo, profiles]], 
                               columns=expected_columns)

    # Convert categorical columns to string (object) for OneHotEncoder
    input_data[categorical_cols] = input_data[categorical_cols].astype(str)

    # Convert numerical columns to correct type
    input_data[numerical_cols] = input_data[numerical_cols].astype(float)

    # Display input data before prediction
    st.write("### Input Data Before Prediction")
    st.dataframe(input_data)

    # Make prediction
    prediction = model.predict(input_data)
    churn_result = "Yes" if prediction[0] == 1 else "No"
    
    st.write(f"### Predicted Churn: {churn_result}")

if __name__ == "__main__":
    run()
