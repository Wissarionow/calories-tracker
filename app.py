import streamlit as st
from database import return_reqest, connect_to_db, disconnect
from login_screen import login_screen
from ai_func import fill_meal, Meal

class CalorieAndMacroToday:
    calories: int
    protein: int
    carbs: int
    fats: int
    fiber: int
    
def empty_calories_today():
    temp=CalorieAndMacroToday()
    temp.calories=0
    temp.protein=0
    temp.carbs=0
    temp.fats=0
    temp.fiber=0
    return temp    

def fill_calories_today(connection, usr_id,class_calories):
    #for test purposes only
    #results = return_reqest(connection, f"SELECT * FROM food_intake WHERE user_id = {usr_id} and day = CURDATE()")
    
    results = return_reqest(connection, f"SELECT * FROM food_intake WHERE user_id = {usr_id}")
    
    for result in results:
        class_calories.calories+=result[2]
        class_calories.protein+=result[3]
        class_calories.carbs+=result[4]
        class_calories.fats+=result[5]
        class_calories.fiber+=result[6]
    return class_calories


def main():
    ###
    #general session state variables
    ###
    if 'usr_intake' not in st.session_state:
        st.session_state.usr_intake = empty_calories_today()
    
    if 'usr_id' not in st.session_state:
        st.session_state.usr_id = None

    if st.session_state.usr_id is None:
        st.session_state.usr_id = login_screen()

    if st.session_state.usr_id is not None:
        connection=connect_to_db()
        
    #calories progress bars
    if st.session_state.usr_id is not None:
        username = return_reqest(connection, f"SELECT username FROM users WHERE id = {st.session_state.usr_id}")
        st.title(f"Welcome, {username[0][0]}")
        st.text("Here is your calories and macro for today")
        
        results = return_reqest(connection, f"SELECT daily_calories, daily_protein, daily_carbs, daily_fats, daily_fiber FROM users WHERE id = {st.session_state.usr_id}")
        daily_goals = results[0]
        
        st.session_state.usr_intake = fill_calories_today(connection, st.session_state.usr_id, st.session_state.usr_intake)
            
        st.write("Calories Intake")
        st.progress(st.session_state.usr_intake.calories / daily_goals[0])
        st.write(f"{st.session_state.usr_intake.calories} / {daily_goals[0]} kcal")
        
        st.write("Protein Intake")
        st.progress(st.session_state.usr_intake.protein / daily_goals[1])
        st.write(f"{st.session_state.usr_intake.protein} / {daily_goals[1]} g")
        
        st.write("Carbs Intake")
        st.progress(st.session_state.usr_intake.carbs / daily_goals[2])
        st.write(f"{st.session_state.usr_intake.carbs} / {daily_goals[2]} g")
        
        st.write("Fats Intake")#???
        st.progress(st.session_state.usr_intake.fats / daily_goals[3])
        st.write(f"{st.session_state.usr_intake.fats} / {daily_goals[3]} g")
        
        st.write("Fiber Intake")
        st.progress(st.session_state.usr_intake.fiber / daily_goals[4])
        st.write(f"{st.session_state.usr_intake.fiber} / {daily_goals[4]} g")
    
    
    #adding meals
    option = st.selectbox("Choose an option", ("Upload a photo", "Take a picture from camera"))
    image = None
    if option == "Upload a photo":
        image = st.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"])
    elif option == "Take a picture from camera":
        image = st.camera_input("Take a picture")

    if image is not None:
        with open("captured_image.png", "wb") as f:
            f.write(image.getbuffer())
    

if __name__ == "__main__":
    main()