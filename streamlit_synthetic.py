import os
import requests
import json
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from sklearn.neighbors import KernelDensity
import google.generativeai as gen_ai

load_dotenv()
# Set up Google Gemini-Pro AI model
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Get the key from the environment

if GOOGLE_API_KEY:
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-1.5-flash-latest')
else:
    st.error("Google API key is not found. Please check your .env file.")


def show_synthetic_data():
    # Heading of the Module
    st.markdown(
        """
        <div style="text-align: center;">
        <h2 style="color: #4285F4; font-size: 40px;"> MedCare Electronic Health Record </h2>
        </div>
        """, unsafe_allow_html=True
    )

    # File uploader for CSV
    uploaded_file = st.file_uploader("Upload a Electronic Health Record in CSV Format", type=["csv"])
    if uploaded_file:
        # Load CSV data into a DataFrame
        original_data = pd.read_csv(uploaded_file)
        
        # Display the original CSV file in Streamlit
        st.write("Uploaded CSV Data (Original):")
        st.dataframe(original_data)
        # Number of synthetic data points to generate
        num_synthetic = 5
        
        # Separate numerical and categorical columns
        numerical_cols = original_data.select_dtypes(include=np.number).columns
        categorical_cols = original_data.select_dtypes(exclude=np.number).columns
        
        # DataFrame to store synthetic data
        synthetic_data = pd.DataFrame()
        
        # Generate synthetic data for numerical columns using KDE sampling
        for col in numerical_cols:
            kde = KernelDensity(kernel='gaussian', bandwidth=1.0).fit(original_data[[col]])
            synthetic_data[col] = kde.sample(num_synthetic).flatten()
        
        # For categorical columns, perform random sampling from existing data
        for col in categorical_cols:
            synthetic_data[col] = np.random.choice(original_data[col], num_synthetic)
        
        # Combine original and synthetic data
        combined_data = pd.concat([original_data, synthetic_data], ignore_index=True)
        
        # Display the synthetic data in Streamlit
        st.write("Generated Synthetic Data (5 additional points):")
        st.dataframe(synthetic_data)
        
        # Display the combined data (original + synthetic) in Streamlit
        st.write("Combined Data (Original + Synthetic):")
        st.dataframe(combined_data)

        # Optionally, allow the user to download the combined data as a CSV
        csv = combined_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Combined Data as CSV",
            data=csv,
            file_name="combined_data.csv",
            mime="text/csv"
        )