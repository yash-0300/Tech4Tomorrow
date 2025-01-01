import os
import requests
import json
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()
# Set up Google Gemini-Pro AI model
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Get the key from the environment

if GOOGLE_API_KEY:
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-1.5-flash-latest')
else:
    st.error("Google API key is not found. Please check your .env file.")

def get_personalized_plan(weight, height, medical_history, activity_level, query):
    # Define the system prompt
    system_prompt = """
    You are a personalized healthcare assistant. Your role is to generate customized meal and workout plans based on the user's physical details and medical history. 
    Provide well-structured, actionable advice, considering the user's current health status and lifestyle. Be concise and informative.
    """
    
    # Define the user prompt with the user's inputs
    user_prompt = f"""
    User details:
    - Weight: {weight} kg
    - Height: {height} cm
    - Medical history: {medical_history}
    - Activity level: {activity_level}
    
    Generate a personalized meal plan and workout plan suitable for the user. Include daily meal recommendations and suggested exercises. Also, consider any medical conditions or health concerns provided in the medical history.
    Always generate a response like a professional Doctor. Do not say user/patient that you are an AI.
    """

    chat = model.start_chat(
        history = [
                {"role": "user", "parts": user_prompt},
                {"role": "model", "parts": system_prompt},
            ]
    )

    # Assuming there's a function to send prompts to the Gemini model and retrieve the output
    response = chat.send_message(query)
    return response.text

def show_personalized():
    # Heading of the Module
    st.markdown(
        """
        <div style="text-align: center;">
        <h2 style="color: #4285F4; font-size: 40px;"> MedCare Personalized Care </h2>
        </div>
        """, unsafe_allow_html=True
    )

    # Collect user inputs
    weight = st.number_input('Enter your weight (kg)')
    height = st.number_input('Enter your height (cm)')
    medical_history = st.text_area("Enter your medical history and any existing conditions")
    activity_level = st.selectbox("Select your activity level", 
                                  ["Sedentary", "Lightly active", "Moderately active", "Very active", "Super active"])
    
    query = st.text_input("Ask the MedCare Personalized HealthCare Chatbot...")

    # Submit button to get a response
    if st.button("Get Personalized Plan"):
        response = get_personalized_plan(weight, height, medical_history, activity_level, query)
        # Custom box styling using markdown
        if response:
            st.markdown(
                f"""
                <div style="
                    background-color: #black;
                    padding: 15px;
                    border-radius: 10px;
                    border: 1px solid #ddd;
                    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                    margin-top: 20px;
                    ">
                    {response}
                </div>
                """, unsafe_allow_html=True
            )