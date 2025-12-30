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

st.header(" ⬆️Upload Image")
st.write("Upload a food image to get calorie & nutrition insights")

uploaded_file = st.file_uploader(
    "📸 Upload food image",
    type=["jpg", "jpeg", "png"]
)

st.image(
    "static/food_bg.jpg",
    caption="🍽️ Make informed food choices with instant calorie and nutrition analysis",
    use_container_width=True
)

input_prompt = """
You are a certified clinical nutritionist and registered dietitian
with expertise in food composition analysis, Indian and global cuisines,
and evidence-based dietary guidelines.

Your task is to analyze the uploaded food image and deliver a precise,
structured, and user-friendly nutrition report.

STRICT ANALYSIS RULES:
- Identify ONLY food items clearly visible in the image.
- Do NOT assume hidden ingredients or cooking methods.
- If portion size is unclear, clearly state the assumption made.
- Use standard nutrition reference values (per 100g) from reliable databases.
- Avoid vague language such as "approximate" unless unavoidable.
- Be confident, factual, and concise.

FOR EACH IDENTIFIED FOOD ITEM, PROVIDE:

1. Food Identification:
- Name of food item
- Assumed portion weight (grams), if not provided by user

2. Nutrition Breakdown (EXACT VALUES):
- Calories (kcal per 100g)
- Carbohydrates (g per 100g)
- Protein (g per 100g)
- Fat (g per 100g)
- Fiber (g per 100g)

3. Daily Requirement Contribution (PERCENTAGE):
Calculate contribution based on an average adult daily requirement:
- Calories (%)
- Carbohydrates (%)
- Protein (%)
- Fat (%)

4. Total Nutrition for the Estimated Portion:
- Total calories
- Total carbohydrates
- Total protein
- Total fat

AFTER ANALYSIS, PROVIDE:

GOOD POINTS (Bullet format, short):
- Nutritional strengths of this food

LIMITATIONS / CONCERNS (Bullet format, short):
- Nutritional weaknesses or health concerns

OVERALL ASSESSMENT:
- Health Category: Healthy / Moderately Healthy / Unhealthy
- One practical improvement suggestion

CONFIDENCE SCORE:
- Reliability of analysis (0–100%)

OUTPUT FORMAT (STRICT — FOLLOW EXACTLY):

Food Item:
Assumed Portion Weight (g):

Nutrition per 100g:
- Calories:
- Carbohydrates:
- Protein:
- Fat:
- Fiber:

Daily Requirement Contribution (% per 100g):
- Calories:
- Carbohydrates:
- Protein:
- Fat:

Total Nutrition for Estimated Portion:
- Calories:
- Carbohydrates:
- Protein:
- Fat:

Good Points:
- 
- 

Concerns:
- 
- 

Health Category:
Improvement Suggestion:
Confidence Score:

Medical Disclaimer:
This AI-generated nutrition analysis is for informational purposes only.
It does not replace professional medical or dietary advice.
Consult a qualified healthcare professional for personalized guidance.
"""

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        return [{
            "mime_type": uploaded_file.type,
            "data": uploaded_file.getvalue()
        }]
    return None


if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_container_width=True)

    submit = st.button("🍛 Analyze Nutrition")

    if submit:
        image_data = input_image_setup(uploaded_file)

        with st.spinner("Analyzing food..."):
            response = get_gemini_response(input_prompt, image_data)

        st.subheader("🔎Nutrition Analysis")
        st.write(response)
























