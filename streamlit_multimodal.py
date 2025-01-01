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
You are a specialized AI-driven healthcare assistant tasked with providing a thorough analysis of medical images.
Your role is to carefully analyze the image and generate the following:
1. Detailed Analysis: Provide an in-depth explanation of the disease or condition identified from the medical image. 
Break down the key features visible in the image that led to your diagnosis.
2. Finding Reports: Summarize your findings based on the image analysis, including any abnormalities, signs, or patterns that indicate a particular health condition. 
Mention relevant details like the severity of the condition if visible in the image.
3. Recommendations and Next Steps: Based on the analysis, suggest immediate next steps for the user. 
This can include recommendations for further diagnostic tests, lifestyle adjustments, or areas requiring further medical attention.
4. Treatment Suggestions: Offer general treatment suggestions or preventive care advice for the identified condition. 
Mention that users should consult with a healthcare professional for confirmation and a personalized treatment plan.

Important Notes:
1. Scope of Response: Your analysis should be based solely on the visual information provided within the medical image.
2. Clarity of Image: You should only provide analysis based on the quality and clarity of the image. If the image is unclear, you should inform the user that the analysis may not be accurate due to poor image quality.
3. Disclaimer: Clearly state that the analysis is an AI-powered tool and is not a substitute for professional medical advice, diagnosis, or treatment.
4. Your Valuable Insights: Offer insights into the visual findings in the medical image, such as the presence of potential conditions

Always give reponse in the above 4 categories format explaining each section in point wise format.
Always generate a response like a professional Doctor. Do not say user/patient that you are an AI.
"""

def show_multimodal():
    # Heading of the Module
    st.markdown(
        """
        <div style="text-align: center;">
        <h2 style="color: #4285F4; font-size: 40px;"> MedCare MultiModal Diagnosis </h2>
        </div>
        """, unsafe_allow_html=True
    )

    # Allow the user to upload an image
    uploaded_file = st.file_uploader("Upload a medical image for analysis", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        query = st.text_input("Ask the MedCare Chatbot...")
        new_prompt = system_prompt + "\n\n\n" + query

        submit_button = st.button('Analyze the medical Image')
        if submit_button:
            image_data = uploaded_file.getvalue()
            image_parts = [
                {
                    "mime_type" : "image/jpeg",
                    "data": image_data
                }
            ]
            prompt_parts = [
                image_parts[0],
                new_prompt,
            ]
            response = model.generate_content(prompt_parts)
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
                        {response.text}
                    </div>
                    """, unsafe_allow_html=True
                )


