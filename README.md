# MedCare AI Health Companion! The Future of Personalized Care

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Diagram](#diagram)
- [Screenshot](#screenshot)
- [Contributing](#contributing)
- [License](#license)

## Overview
This repository contains an AI-powered healthcare application designed to enhance patient care and medical research. Built with Streamlit and advanced AI models, the application allows users to upload medical data, generate synthetic health records, perform multimodal diagnosis, and receive personalized treatment recommendations. It also offers tools for real-time research assistance, drug discovery, and synthetic data quality checks. The system leverages the Google Gemini model, along with various machine learning and data processing techniques, to bridge the gap between patient care and medical research while ensuring the accuracy and quality of synthetic health data.


## Features

- **AI Multimodal Diagnosis**: Users upload medical data (images and text), and the AI analyzes it to provide detailed disease insights and next-step recommendations.

- **Personalized Treatment**: Based on user health records, the AI offers customized care plans, including health monitoring, goal setting, and chatbot interactions.

- **Health Record Synthesis**: Researchers upload disease-related data or CSV files, and the AI generates synthetic health records to address data scarcity for research purposes.

- **Literature Recommender**: Users input disease queries, and the AI recommends relevant research papers from PUBMED to streamline literature reviews.

- **Research Copilot**: Researchers upload research papers (PDFs) and interact with them through AI-driven chat for enhanced information retrieval.

- **Synthetic Quality Check**: Users upload real and synthetic EHR datasets, and the AI statistically compares them to ensure the quality and reliability of synthetic data.

- **Drug Discovery**: Users provide SMILES notation, and the AI generates molecular images and properties, facilitating new drug development.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yash-0300/MedCareAI.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and go to `http://localhost:8501`.

## Diagram

![Architecture and User Flow](https://github.com/yash-0300/MedCareAI/blob/main/Images/MedCareAI_Tech.png)

## Screenshot

![Application Home Page](https://github.com/yash-0300/MedCareAI/blob/main/Images/medcareai_ss1.png)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.