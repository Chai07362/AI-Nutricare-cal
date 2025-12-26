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
You are a caring nutrition coach.

Analyze the uploaded food image and help the user understand their meal in a supportive and honest way.

Your goals:
- Appreciate what is good about the meal
- Point out nutritional gaps gently
- Help the user make better choices without guilt

Steps:
1. Identify only the visible food items.
2. Estimate portion size for each item (small / medium / large).
3. Provide approximate calories per item.
4. Calculate the total calorie range of the meal.
5. Estimate key nutrients (protein, carbohydrates, fats, fiber).
6. Mention at least one positive nutritional aspect.
7. Mention at least one area of concern or improvement.
8. Suggest 1 small, realistic improvement the user can apply next time.

Guidelines:
- Be respectful, encouraging, and non-judgmental.
- Use simple language; avoid medical terms.
- If the image is unclear, say so politely.
- Calories and nutrients are estimates, not exact values.
- Do NOT give medical advice.

Respond strictly in this format:

🍽️ What’s on your plate:
- Item – Portion – Calories (approx)

🔥 Total Calories:
- ___ to ___ kcal

🥗 Nutrition Breakdown (Approx):
- Protein: ___ g
- Carbohydrates: ___ g
- Fats: ___ g
- Fiber: ___ g

✅ What’s good about this meal:
- ___

⚠️ What could be better:
- ___

💡 Gentle nutrition tip:
- One simple, caring suggestion

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























