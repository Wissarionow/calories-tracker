import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
from typing import Any
import streamlit as st

#establish connection, if None is returned, connection failed
@st.cache_resource
def connect_to_db():
    env = dotenv_values(".env")
    try:
        connection = mysql.connector.connect(
        host=st.secrets['DB_HOST'],        
        user=st.secrets['DB_USER'],        
        password=st.secrets['DB_PASS'],        
        database=st.secrets['DB_NAME'],      
        auth_plugin=st.secrets['DB_AUTH_PLUGIN']
    )
        
        if connection.is_connected():
            return connection
        
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def return_reqest(connection: Any,query: str):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


def db_login(connection: Any, username: str, password: str):
    results=return_reqest(connection, f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    if results:
        return True
    else:
        return False

def db_login_email(connection: Any, email: str):
    results=return_reqest(connection, f"SELECT * FROM users WHERE email = '{email}'")
    if results:
        usr_id=return_reqest(connection, f"SELECT id FROM users WHERE email = '{st.session_state.email}'")[0][0]
        st.session_state.usr_id = usr_id
        return st.session_state.usr_id
    else:

        return 
    #db_login_email(connection, email)
    
def registration_email(): 

            st.write("Add some info ")
            email = st.session_state.email
            goal = st.number_input("Gain/Lose Weight", value=st.session_state.reg.goal, min_value=0)
            weight = st.number_input("Weight", value=st.session_state.reg.weight, min_value=0)
            bodyfat = st.number_input("Bodyfat", value=st.session_state.reg.bodyfat, min_value=0)
            daily_calories = st.number_input("Daily calories", value=st.session_state.reg.daily_calories, min_value=0)
            daily_protein = st.number_input("Daily protein", value=st.session_state.reg.daily_protein, min_value=0)
            daily_carbs = st.number_input("Daily Carbs", value=st.session_state.reg.daily_carbs, min_value=0)
            
            
            if st.button("Add"):
                connection=connect_to_db()
                add_usr(connection, email, goal, weight, bodyfat, daily_calories, daily_protein, daily_carbs)
                # st.session_state.usr_intake = empty_calories_today()
                # st.session_state.usr_intake = fill_calories_today(connection, st.session_state.usr_id, 
                #                                                   st.session_state.usr_intake)
                st.success("User add succesfully")

def add_meal(connection: Any, usr_id: int, meal_name: str, calories: int, protein: int, carbs: int, fats: int, fiber: int):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO food_intake (user_id, meal_name, calories, protein, carbs, fats, fiber,day) VALUES ({usr_id}, '{meal_name}', {calories}, {protein}, {carbs}, {fats}, {fiber}, CURDATE())")
    connection.commit()
    cursor.close()

def add_usr(connection: Any, email: int, goal: str, weight: int, body_fat: int, daily_calories: int, daily_protein: int, daily_carbs: int,):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users (email, goal, body_fat, weight, daily_calories, daily_protein, daily_carbs) VALUES ({email}, '{goal}', '{body_fat}', '{weight}', '{daily_calories}', '{daily_protein}', '{daily_carbs}')")
    connection.commit()
    cursor.close()
    
    
#void disconnect 
def disconnect(connection:any):
    connection.close()
    
def create_user(connection: Any, username: str, password: str, daily_calories: int, daily_protein: int, daily_carbs: int, daily_fats: int, daily_fiber: int):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users (username, password, daily_calories, daily_protein, daily_carbs, daily_fats, daily_fiber) VALUES ('{username}', '{password}', {daily_calories}, {daily_weight}, {daily_carbs}, {daily_fats}, {daily_fiber})")
    connection.commit()
    cursor.close()
    
def db_user_goal(connection: Any, usr_id: int):
    goal_string = return_reqest(connection, f"SELECT goal FROM users WHERE id = {usr_id}")
    return goal_string[0][0]

def user_exists_check_by_email(email):
    db_login_email()

