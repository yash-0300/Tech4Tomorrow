import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Set up Google Gemini-Pro AI model
if GOOGLE_API_KEY:
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    model = gen_ai.GenerativeModel('gemini-1.5-flash-latest')
else:
    st.error("Google API key is not found. Please check your .env file.")

# Extract text from uploaded PDFs
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

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

# Main function for the Streamlit app
def show_copilot():
    st.markdown("""
        <div style="text-align: center;">
        <h2 style="color: #4285F4; font-size: 40px;">MedCare Research Copilot</h2>
        </div>
        """, unsafe_allow_html=True
    )

    # File uploader for PDF files
    pdf_docs = st.file_uploader("Upload your PDF Files and click on 'Submit & Process'", accept_multiple_files=True)

    # Button to process the uploaded files
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            raw_text = get_pdf_text(pdf_docs)
            st.success("Text extraction complete!")
            st.session_state["system_prompt"] = "From the text below, answer the user's question:\n\n" + raw_text

    # Collect user question outside of generate_response
    user_question = st.text_input("Ask a MedCare Research Copilot question:")

    # Display button only if text has been processed
    if "system_prompt" in st.session_state:
        if st.button("Generate Response"):
            response = generate_response(st.session_state["system_prompt"], user_question)
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
