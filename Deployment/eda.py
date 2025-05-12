import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run():
    st.title("Exploratory Data Analysis")
    
    # Load dataset
    df = pd.read_csv("Netflix Engagement Dataset.csv")
    st.write("### Netflix Engagement Data")
    st.dataframe(df.head(11))

 
    # Churn distribution visualization
    if "Churn Status (Yes/No)" in df.columns:
        st.write("### Churn Distribution")
        
        # Create the plot
        fig, ax = plt.subplots()
        sns.countplot(x="Churn Status (Yes/No)", data=df, palette="coolwarm", ax=ax)
        ax.set_title("Churn Distribution")

        # Display the plot in Streamlit
        st.pyplot(fig)
    else:
        st.error("Column 'Churn Status (Yes/No)' not found in dataset.")

    # Subscription Length vs Churn
    st.write("### Subscription Length vs. Churn")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="Churn Status (Yes/No)", y="Subscription Length (Months)", data=df, ax=ax)
    ax.set_title("Subscription Length vs. Churn")
    st.pyplot(fig)

    # Monthly Income vs Churn
    st.write("### Monthly Income vs. Churn")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="Churn Status (Yes/No)", y="Monthly Income ($)", data=df, ax=ax)
    ax.set_title("Monthly Income vs. Churn")
    st.pyplot(fig)

    # Subscription Plan vs Churn
    st.write("### Subscription Plan vs. Churn")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.countplot(x="Subscription Plan", hue="Churn Status (Yes/No)", data=df, ax=ax)
    ax.set_title("Subscription Plan vs. Churn")
    st.pyplot(fig)

    # Customer Satisfaction Score vs Churn
    st.write("### Customer Satisfaction Score vs. Churn")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x="Churn Status (Yes/No)", y="Customer Satisfaction Score (1-10)", data=df, ax=ax)
    ax.set_title("Customer Satisfaction Score vs. Churn")
    st.pyplot(fig)




if __name__ == '__main__':
    run()