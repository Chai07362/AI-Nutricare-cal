import streamlit as st
from PIL import Image
from gemini_helper import get_gemini_response

st.set_page_config(
    page_title="AI NutriCare",
    layout="wide"
)

st.header("🥗 AI NutriCare")
st.write("Upload food image to get calorie & nutrition insights")

uploaded_file = st.file_uploader(
    "📸 Upload food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)

submit = st.button("🔍 Analyze Calories")

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
   
    st.subheader("📊 Nutrition Analysis")
    st.write(response)

