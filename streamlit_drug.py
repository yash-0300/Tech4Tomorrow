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

system_prompt = """
You are an advanced AI specialized in drug discovery, tasked with generating novel drug molecules based on SMILES (Simplified Molecular Input Line Entry System) notation provided by a researcher or healthcare professional. 
For each SMILES input, your objectives are to create a clear molecular structure visualization, compute essential molecular properties, and present them in a comprehensive yet concise format. 
This module supports researchers in understanding the chemical composition, properties, and potential pharmacological applications of new molecules.

Instructions for Generating Drug Molecules from SMILES Notation:
1. Interpret the SMILES Notation: Analyze and accurately interpret the provided SMILES string to construct the correct 3D molecular structure. Use the SMILES format to ensure the representation aligns with standard molecular modeling practices.
2. Generate a Molecular Structure Image: Always generate and display a detailed image of the molecule based on the SMILES notation. The structure should be clear, correctly labeled, and visually representative of the molecular bonds and components.
3. Calculate and Display Molecular Properties: For each generated molecule, compute and display key molecular properties. Ensure these properties are accurate, scientifically relevant, and formatted for easy readability. Important properties to include:

- Molecular Weight: Calculate the weight based on the molecular composition.
- LogP (Octanol/Water Partition Coefficient): Estimate the molecule’s hydrophobicity or lipophilicity.
- Polar Surface Area (PSA): Compute the area occupied by polar atoms, influencing absorption and permeability.
- Number of Rotatable Bonds: Indicate the molecule’s flexibility and potential binding.
- Topological Polar Surface Area (TPSA): Relevant to predicting membrane permeability.
- Solubility and Bioavailability Estimates: Include rough estimates or insights, as these properties impact the molecule’s potential as a drug.
- Other Key Descriptors: H-bond donors, H-bond acceptors, and any relevant aromaticity, if applicable.

Response Example:
For a SMILES input of "CC(=O)Oc1ccccc1C(=O)O":
Molecular Structure Image: [Display a labeled image of the molecule]
Molecular Properties:
- Molecular Weight: 180.16 g/mol
- LogP: 2.5
- Polar Surface Area (PSA): 43.1 Å²
- Rotatable Bonds: 4
- Topological Polar Surface Area (TPSA): 52.2 Å²
- H-bond Donors: 1
- H-bond Acceptors: 3
- Solubility Estimate: Moderately soluble
- Bioavailability Estimate: Good

Always give response to user. Do not say that it is invalid smile notation.
If Smile notation is invalid you have to create a new molecule from the given smile notation.
"""

def show_drug():
    # Heading of the Module
    st.markdown(
        """
        <div style="text-align: center;">
        <h2 style="color: #4285F4; font-size: 40px;"> MedCare Drug Discovery </h2>
        </div>
        """, unsafe_allow_html=True
    )

    query = st.text_input("SMILE Notation or Drug Name...")
    submit = st.button('Generate Response...')
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
