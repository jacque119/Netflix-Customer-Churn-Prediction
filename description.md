# Netflix Customer Churn Prediction

## Repository
`This is a project to create machine learning model to predict Netflix Customer Churn Behavior using 5 models (KNN, SVM, Decision Tree, Random Forest, Gradient Boost)`


```
1. README.md - Project Overview.
2. P1M2_reza_agassi.ipynb - Notebook for developing all the models.
3. inf_P1M2_reza_agassi.ipynb - Notebook for testing the best model with new inference data.
4. url.txt - Text file consist of dependencies required to deploy the model in hugging face open sources platform.
5. Netflix Engagement Dataset.csv - raw dataset in csv.
6. train_analysis.csv - data frame for analyzing strength and weakness of the model.
7. batch_inference_data.csv - data frame for inference data.
8. Deployment file - consist of the best model, dataset, data inference and 3 python script for a web app using streamlit.
```

## Problem Background
`With rises the popularity of subscription based platform like netflix it creates many new competitor that have their own strength this could make the churn behavior. Churn is when customer stop subscribing to netflix and move to other platform. From that problem we would like to develop a machine learning model to study this behavior so a company like Netflix could mitigate the churn of their customer by learning the pattern and providing a solution toward a customer problem`

## Project Output
`The output of this project is Web App contain EDA analysis and best model picked that can predict new data for predicting churn behavior of customer.`

## Data
`This project uses the Netflix Engagement Dataset, which contains customer interaction details, subscription history, and engagement metrics. The dataset includes 14 features such as subscription length, customer satisfaction score, daily watch time, engagement rate, and payment history:`

`Rows: 3,500+
Columns: 14
Missing Values: None
Outliers: None`

## Method
`This project aims to predict customer churn using Supervised Machine Learning techniques. The approach includes:

1. Exploratory Data Analysis (EDA) – Understanding customer behavior and key churn factors.
2. Preprocessing Pipeline – Handling categorical and numerical features using OneHotEncoding and Standard Scaling.
3. Model Selection & Training – Implementing multiple models such as:
    - Support Vector Machine (SVM) (Final Model Chosen)
    - Decision Tree
    - Random Forest
    - Gradient Boosting
4. Deployment – Creating a Streamlit web app hosted on Hugging Face Spaces for easy user interaction.`

## Stacks
`The following tools and technologies were used:

1. Programming Language: Python
2. Libraries Used:
    - pandas – Data manipulation
    - scikit-learn – Machine learning models
    - matplotlib & seaborn – Data visualization
    - joblib – Model saving/loading
    - streamlit – Web app deployment
3. Deployment: Hugging Face Spaces (for hosting the prediction app)`

## Reference
`Hugging Face.co`

---

