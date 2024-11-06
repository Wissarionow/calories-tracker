import streamlit as st
from openai import OpenAI
import base64
import instructor
from pydantic import BaseModel
from dotenv import dotenv_values

class CalorieAndMacroToday:
    calories: int
    protein: int
    carbs: int
    fats: int
    fiber: int

class Meal(BaseModel):
    name: str
    calories: int
    protein: int
    carbs: int
    fats: int
    fiber: int

def fill_meal(image):
    meal = instructor_openai_client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=Meal,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Wypełnij makroskładniki i kalorie posiłku oraz podaj jego nazwę.", 
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image,
                            "detail": "high"
                        },
                    },
                ],
            },
        ],
    )
    return meal

def prepare_image_for_open_ai(image_path):
    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    return f"data:image/png;base64,{image_data}"

today = CalorieAndMacroToday()
meals = []

# Connecting to OpenAI
env = dotenv_values(".env")
openai_client = OpenAI(api_key=env["OPENAI_API_KEY"])
instructor_openai_client = instructor.from_openai(openai_client)

st.title("Camera or File Upload Example")

# Option to either upload a photo or take a picture from the camera
option = st.selectbox("Choose an option", ("Upload a photo", "Take a picture from camera"))

image = None
if option == "Upload a photo":
    image = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])
elif option == "Take a picture from camera":
    image = st.camera_input("Take a picture")


# If an image is provided, display it and prepare it for OpenAI
if image is not None:
    with open("captured_image.png", "wb") as f:
        f.write(image.getbuffer())

    prepared_image = prepare_image_for_open_ai("captured_image.png")

    st.image(image, caption="Captured Image", use_column_width=True)

    st.text(prepared_image)
    
    meal = fill_meal(prepared_image)
    
    # Print out meal macros
    st.write(meal.name)
    st.write("Kalorie: " + str(meal.calories))
    st.write("Białko: " + str(meal.protein))
    st.write("Węglowodany: " + str(meal.carbs))
    st.write("Tłuszcze: " + str(meal.fats))
    st.write("Błonnik: " + str(meal.fiber))
    