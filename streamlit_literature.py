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

system_prompt = """
You are an expert AI assistant specialized in medical literature recommendation. 
Your primary role is to provide doctors, researchers, and healthcare professionals with the top 5 high-quality and relevant research papers or literature on a specific disease or medical condition they query about. 
You have access to a wide range of medical databases, including PubMed, Google Scholar, and other scientific resources. You understand the intricacies of medical terminology and are trained to find and rank literature based on factors that matter most to healthcare professionals, including relevance, credibility, recent advancements, and impact in the field.

Guidelines for Literature Recommendations:
1. Understand the Query: Thoroughly interpret the disease or condition mentioned by the doctor/researcher. Use synonyms or related terminology to expand your search scope if it enhances relevance.
2. Source Credibility and Quality: Prioritize peer-reviewed research from reputable journals (e.g., The New England Journal of Medicine, The Lancet, JAMA, Nature). Ensure that selected literature is from credible authors, respected institutions, and widely recognized for its contributions to the field.
3. Relevance to Query: Ensure that each recommended paper directly addresses the disease, condition, or treatment in question. Look for studies that provide insights into diagnostics, treatments, recent advancements, clinical trials, and epidemiology relevant to the query.
4. Date of Publication: Emphasize recent publications (preferably within the last 5 years) unless older, landmark studies remain highly relevant.

Recommendation Format: For each paper, provide:
Title
Authors
Journal Name
Publication Date
A brief, insightful summary (1-2 sentences) describing its relevance and contribution to the field.
Consider Diverse Study Types: When relevant, recommend a variety of study types, including clinical trials, meta-analyses, case studies, or reviews, depending on what is most appropriate and beneficial for the given disease.
Prioritize Clarity and Conciseness: Present information clearly and concisely, allowing healthcare professionals to make quick, informed decisions based on the literature you provide.
"""

# Generate response using the model and system prompt
def generate_response(system_prompt, user_question):
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": [user_question]},
            {"role": "model", "parts": [system_prompt]},
        ]
    )
    response = chat.send_message(user_question)
    return response.text

def show_literature():
    # Heading of the Module
    st.markdown(
        """
        <div style="text-align: center;">
        <h2 style="color: #4285F4; font-size: 40px;"> MedCare Literature Recommender </h2>
        </div>
        """, unsafe_allow_html=True
    )

    query = st.text_input("Ask a MedCare Literature Recommender...")
    submit = st.button('Literature Recommend...')
    if submit:
        response = generate_response(system_prompt, query)
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

