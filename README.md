# AI NutriCare

AI NutriCare is a simple web application that helps users understand the nutritional value of their meals by analyzing food images.

The focus of this project is not just calorie counting, but **nutrition awareness** — highlighting what is good in a meal, pointing out what could be improved, and offering gentle, practical suggestions.

---

## What the app does

- Allows users to upload a food image
- Identifies visible food items
- Estimates calories and basic nutrition
- Highlights positive aspects of the meal
- Mentions nutritional gaps in a supportive way
- Suggests small improvements without judgement

All results are **approximate** and meant to help users make more informed food choices.

---

## How it works

1. A user uploads a food image  
2. The image is processed using a vision-based language model  
3. Food items and portion sizes are estimated  
4. Calories and nutrition values are calculated approximately  
5. The user receives balanced and easy-to-understand feedback  

---

## Technology used

- Python
- Streamlit
- Google Gemini API
- Pillow (for image handling)

---

## Project structure

AI-NutriCare/
│── app.py
│── gemini_helper.py
│── requirements.txt
│── README.md
│── .streamlit/
│ └── secrets.toml (local only)


---

## Running the project locally

1. Clone the repository  
``bash
git clone https://github.com/YOUR_USERNAME/AI-NutriCare.git
cd AI-NutriCare
Install dependencies
''bash

2.Install dependencies

pip install -r requirements.txt

3.Add your API key
Create the file .streamlit/secrets.toml and add:
GEMINI_API_KEY = "your_api_key_here"

4.Run the app
streamlit run app.py

Live version

The application is deployed on Streamlit Cloud:
https://ai-nutricare-cal.streamlit.app/

Notes on accuracy

The calorie and nutrition values shown by the app are estimates.
Actual values may vary depending on portion size, cooking method, and ingredients.

This project is intended for learning and awareness, not medical or dietary diagnosis.

* Possible improvements

~ User input for portion size

~ Better handling of regional food variations

~ Meal history tracking
 
~ Personalised suggestions based on goals

Final thoughts

This project was built as a learning exercise in combining computer vision, user-friendly design, and practical nutrition guidance.

Small, consistent improvements in food choices matter more than perfection.






