import os
import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie

# Lottie animation function for Animation in streamlit app
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Google-themed Lottie animation (verified URL)
lottie_google_fact_check = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_t9gkkhz4.json")

def show_home():
    st.markdown(
        """
        <div style="text-align: center;">
        <h2 style="color: #4285F4; font-size: 40px;">MedCare AI Health Companion! The Future of Personalized Care</h2>
        <p style="font-size: 20px;">Powered by Hack This Fall and Devfolio </p>
        </div>
        """, unsafe_allow_html=True
    )

    # Add some space with animation
    if lottie_google_fact_check:
        st_lottie(lottie_google_fact_check, height=250, key="google_fact_check")
    else:
        st.error("Failed to load animation. Please check the URL.")

    feature_1_desc = "Leverage the power of AI to analyze both medical images and textual data. Our AI Multimodal Diagnosis feature provides patients with detailed disease insights and clear next-step recommendations, helping you take control of your health journey"
    feature_2_desc = "Experience care that’s as unique as you are. Our Personalized Treatment plans combine AI-powered chatbots, health monitoring, and goal setting, delivering customized meal plans, workout routines, and treatment recommendations designed to match your individual health profile"
    feature_3_desc = "Research-driven insights made easy! Our Health Record Synthesis feature allows researchers to generate realistic synthetic health records from disease inputs or CSV uploads, enabling advanced research without the limitations of real-world data scarcity"
    feature_4_desc = "Need the latest research? Our Literature Recommender automatically fetches the top research papers from PUBMED, tailored to your specific disease queries. Say goodbye to manual searches and streamline your literature review process for faster innovation"
    feature_5_desc = "Transform how you interact with research papers! The Research Copilot feature allows researchers to engage with academic papers in real-time, using AI-powered chat to extract and analyze information from PDFs, making the research process faster and more efficient"
    feature_6_desc = "Quality matters in research! Our Synthetic Quality Check feature statistically compares synthetic health records with real Electronic Health Records (EHRs) to ensure the accuracy and reliability of generated data, paving the way for high-quality medical research"
    feature_7_desc = "Revolutionize drug discovery with AI. Our Drug Discovery feature enables the creation of new drugs from SMILES notation, automatically generating molecular images and properties. This empowers researchers to unlock new treatment possibilities and accelerate the development of life-saving medications"

    image1_path = "./Images/Image1_hack.jpg"
    image2_path = "./Images/Image2_hack.jpg"
    image3_path = "./Images/Image3_hack.jpg"
    image4_path = "./Images/Image4_hack.jpg"
    image5_path = "./Images/Image5_hack.jpg"
    image6_path = "./Images/Image6_hack.jpeg"
    image7_path = "./Images/Image7_hack.jpg"

    # Create two rows of features (2 in each row)
    col1, col2 = st.columns(2)
    with col1:
        st.image(image1_path, caption="AI Multimodal Diagnosis", use_column_width=True)
        st.write(feature_1_desc)

    with col2:
        st.image(image2_path, caption="Personalized Treatment", use_column_width=True)
        st.write(feature_2_desc)
    
    col3, col4 = st.columns(2)
    with col3:
        st.image(image3_path, caption="Health Record Synthesis", use_column_width=True)
        st.write(feature_3_desc)

    with col4:
        st.image(image4_path, caption="Literature Recommender", use_column_width=True)
        st.write(feature_4_desc)
    
    col5, col6 = st.columns(2)
    with col5:
        st.image(image5_path, caption="Research Copilot", use_column_width=True)
        st.write(feature_5_desc)

    with col6:
        st.image(image6_path, caption="Synthetic Quality Check", use_column_width=True)
        st.write(feature_6_desc)

    col7, col8 = st.columns(2)
    with col7:
        st.image(image7_path, caption="Drug Discovery", use_column_width=True)
        st.write(feature_7_desc)

    # Footer
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px;">
            <h4 style="color: #FBBC05;"> Built for Hack This Fall Virtual Hackathon 2024 🚀</h4>
            <p>By MedCare AI | Powered by Devfolio </p>
        </div>
        """, unsafe_allow_html=True
    )