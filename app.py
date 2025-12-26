import streamlit as st
from PIL import Image
from gemini_helper import get_gemini_response
import base64

st.set_page_config(
    page_title="AI NutriCare",
    layout="wide"
)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    



st.markdown("""
<div style="
background: linear-gradient(
    rgba(0,0,0,0.55),
    rgba(0,0,0,0.55)
),
url('https://images.unsplash.com/photo-1498837167922-ddd27525d352');
background-size: cover;
background-position: center;
padding: 25px;
border-radius: 16px;
color: white;
text-align: center;
margin-bottom: 25px;">
<h2 style="margin-bottom: 8px;">🥗 AI NutriCare</h2>
<p style="font-size: 14px; opacity: 0.9;">
Smart calorie & nutrition insights
</p>
</div>
""", unsafe_allow_html=True)

st.image(
    "static/food_bg.jpg",
    caption="🍽️ Balanced meal example",
    use_container_width=True
)


input_prompt = """
You are a friendly nutrition coach.

Look at the uploaded food image and help the user understand their meal in a simple, motivating way.

Do the following:
1. Identify the visible food items (only what you can clearly see).
2. Estimate the portion size of each item (small / medium / large).
3. Give an approximate calorie range for each item.
4. Calculate the total calorie range of the meal.
5. Briefly explain how this meal affects energy, fitness, or weight goals.
6. Give 1 small, practical tip the user can apply today.

Guidelines:
- Be friendly, positive, and non-judgmental.
- Keep explanations short and easy to understand.
- If the image is unclear, politely say so.
- Calories are estimates, not exact values.
- Avoid medical or clinical language.

Respond in this format:

🍽️ What’s on your plate:
- Item – Portion – Calories (approx)

🔥 Total Energy:
- ___ to ___ kcal

💡 What this means for you:
- Short, motivating explanation

✅ One small improvement (optional):
- Practical tip
"""

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        return [{
            "mime_type": uploaded_file.type,
            "data": uploaded_file.getvalue()
        }]
    return None

st.header(" ⬆️Upload Image")
st.write("Upload a food image to get calorie & nutrition insights")

uploaded_file = st.file_uploader(
    "📸 Upload food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image,
use_container_width=True)

    submit = st.button("🔍 Analyze Calories")

    if submit:
        image_data = input_image_setup(uploaded_file)

        with st.spinner("Analyzing food..."):
            response = get_gemini_response(input_prompt, image_data)

        st.subheader("🔎 Analysis")
        st.write(response)






















