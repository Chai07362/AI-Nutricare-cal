import streamlit as st
from PIL import Image
from gemini_helper import get_gemini_response

st.set_page_config(page_title=" AI Calories Calculator")
st.header("🍎AI Calories Calculator")

uploaded_file = st.file_uploader("Choose a food image...", type=["jpg","jpeg","png"])

def input_image_setup(uploaded_file):
    if uploaded_file:
        return [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]
    return None

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=250)

submit = st.button("Tell me about the total calories")

input_prompt = """
You are a nutritionist. Analyze the food items in the image and calculate:
1. Calories per food item
2. Total calories
3. Whether the food is healthy or not

Format:
1. Item 1 - calories
2. Item 2 - calories
...
Total: _ calories
Healthiness: _
"""

if submit and uploaded_file:
    image_data = input_image_setup(uploaded_file)
    with st.spinner("Analyzing food..."):
        response = get_gemini_response(input_prompt, image_data)
    st.subheader("🔎 Analysis")
    st.write(response)