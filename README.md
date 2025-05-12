# Netflix Customer Churn Prediction 🎬📉

This project analyzes customer engagement data from Netflix to predict churn behavior using various classification models. The goal is to identify customers likely to leave the platform and support strategic retention efforts.

---

## 📌 Project Objective

To develop a machine learning model that predicts which Netflix users are likely to churn, based on their viewing behavior and engagement metrics. The model aims to assist in customer retention strategies by identifying high-risk users.

---

## 📊 Dataset

- **Source**: Netflix Engagement Dataset (Kaggle)
- **Size**: ~3,500+ user records
- **Features**: Account age, daily watch time, content preferences, payment history, and churn status

---

## 🧠 Models Used

- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Decision Tree  
- Random Forest  
- XGBoost  

---

## 📈 Results

- Best performing model: **Random Forest**  
- Accuracy: ~88%  
- ROC AUC Score: ~0.91  
- Feature Importance: Watch time, Payment consistency, Preferred content genre

---

## 🛠️ Tech Stack

- Python (Pandas, Scikit-learn, XGBoost)
- Jupyter Notebook
- Streamlit (for web app deployment)

---

## 🚀 Deployment

A simple **Streamlit web app** was created to make the model accessible for inference:
- Upload new customer data (CSV)
- View predicted churn outcomes

🔗 [Try the App](https://huggingface.co/spaces/rezaagassi11/Netflix_churn)

---


