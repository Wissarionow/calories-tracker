import streamlit as st
from database import return_reqest , connect_to_db, disconnect
from login_screen import login_screen
from ai_func import fill_meal, Meal

class CalorieAndMacroToday:
    calories: int
    protein: int
    carbs: int
    fats: int
    fiber: int


if 'usr_id' not in st.session_state:
        st.session_state.usr_id = login_screen()
        

if st.session_state.usr_id is not None:
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

        
        meal = fill_meal("captured_image.png")
        
        # Print out meal macros
        st.write(meal.name)
        st.write("Kalorie: " + str(meal.calories))
        st.write("Białko: " + str(meal.protein))
        st.write("Węglowodany: " + str(meal.carbs))
        st.write("Tłuszcze: " + str(meal.fats))
        st.write("Błonnik: " + str(meal.fiber))
    