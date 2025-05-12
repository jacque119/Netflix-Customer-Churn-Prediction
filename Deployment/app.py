import streamlit as st
import eda
import pred

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Pilih Halaman:", ["EDA", "Predict A User"])

# Display the selected page
if page == "EDA":
    eda.run()  # Run EDA script
elif page == "Predict A User":
    pred.run()  # Run Prediction script
