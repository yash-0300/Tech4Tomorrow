import os
import requests
import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_home import *
from streamlit_multimodal import *
from streamlit_personalized import *
from streamlit_copilot import *
from streamlit_literature import *
from streamlit_drug import *
from streamlit_synthetic import *
from streamlit_quality_check import *

# Set page configuration - Page title in browser tab bar
st.set_page_config(page_title="MedCare Assistant", layout="wide", page_icon="🧑‍⚕️")

# Sidebar for selecting the 7 features of our AI powered MedCare Application
with st.sidebar:
    selected = option_menu(
        'MedCare Solutions',
        ['Home', 'AI MultiModal Diagnosis', 'Personalized Treatment', 'Health Record Synthesis', 'Literature Recommender', 'Research Copilot', 'Synthetic Quality Check', 'Drug Discovery'],
        menu_icon='hospital-fill',
        icons=['house', 'activity', 'heart', 'database', 'book', 'robot', 'check-circle', 'gear'],
        default_index = 0
    )

if selected == 'Home':
    show_home()

if selected == 'AI MultiModal Diagnosis':
    show_multimodal()

if selected == 'Personalized Treatment':
    show_personalized()

if selected == 'Research Copilot':
    show_copilot()

if selected == 'Literature Recommender':
    show_literature()

if selected == 'Drug Discovery':
    show_drug()

if selected == 'Health Record Synthesis':
    show_synthetic_data()

if selected == 'Synthetic Quality Check':
    show_quality_check()