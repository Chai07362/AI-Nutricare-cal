import streamlit as st
from PIL import Image
from gemini_helper import get_gemini_response

st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
    }

    /* Title */
    h1 {
        color: #0f172a;
        text-align: center;
    }

    /* Upload box */
    section[data-testid="stFileUploader"] {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #cbd5e1;
    }

    /* Button */
    button {
        background-color: #22c55e !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="AI NutriCare",
    layout="wide"
)

input_prompt = """
You are a certified nutritionist and dietician with expertise in Indian and global cuisines.

Analyze the food items visible in the image carefully.

STRICT RULES:
- Identify only clearly visible food items.
- Assume the cuisine may be Indian unless clearly non-Indian.
- Estimate portion sizes using common Indian serving standards (katori, roti size, ladle, plate size).
- Use standard nutrition databases for estimation.
- If any assumption is made, state it clearly.
- Do NOT guess hidden ingredients or cooking methods.
- If the image quality is poor, say so.

For EACH food item provide:
- Name
- Estimated calories
- Macronutrients (carbs, protein, fat)

Then provide:
1. Total estimated calories of the meal
2. Health rating (Healthy / Moderately Healthy / Unhealthy)
3. Short reasoning (2–3 lines)
4. One realistic improvement suggestion
5. Confidence score (0–100%) indicating reliability of the estimation

Output format (STRICT):

Item 1:
- Name:
- Calories:
- Carbs:
- Protein:
- Fat:

Item 2:
- Name:
- Calories:
- Carbs:
- Protein:
- Fat:

Total Calories:
Health Rating:
Reason:
Suggestion:
Confidence Score:
Medical Disclaimer:
This analysis is AI-generated and intended for informational purposes only.
It should not be considered medical or dietary advice.
Please consult a qualified healthcare professional or registered dietician for personalized guidance.
"""

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        return [{
            "mime_type": uploaded_file.type,
            "data": uploaded_file.getvalue()
        }]
    return None

st.header("🥗 AI NutriCare")
st.write("Upload a food image to get calorie & nutrition insights")

uploaded_file = st.file_uploader(
    "📸 Upload food image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)

    submit = st.button("🔍 Analyze Calories")

    if submit:
        image_data = input_image_setup(uploaded_file)

        with st.spinner("Analyzing food..."):
            response = get_gemini_response(input_prompt, image_data)

        st.subheader("🔎 Analysis")
        st.write(response)






