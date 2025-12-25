import streamlit as st
import google.generativeai as genai

# Configure Gemini API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Create Gemini model once
model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_response(input_prompt, image_parts):
    response = model.generate_content([input_prompt, image_parts[0]])
    return response.text