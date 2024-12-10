import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
from typing import Any
import streamlit as st

#establish connection, if None is returned, connection failed
def connect_to_db():
    #env = dotenv_values(".env")
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

def add_meal(connection: Any, usr_id: int, meal_name: str, calories: int, protein: int, carbs: int, fats: int, fiber: int):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO food_intake (user_id, meal_name, calories, protein, carbs, fats, fiber,day) VALUES ({usr_id}, '{meal_name}', {calories}, {protein}, {carbs}, {fats}, {fiber}, CURDATE())")
    connection.commit()
    cursor.close()
    
    
#void disconnect 
def disconnect(connection:any):
    connection.close()
    
def create_user(connection: Any, username: str, password: str, daily_calories: int, daily_protein: int, daily_carbs: int, daily_fats: int, daily_fiber: int):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO users (username, password, daily_calories, daily_protein, daily_carbs, daily_fats, daily_fiber) VALUES ('{username}', '{password}', {daily_calories}, {daily_protein}, {daily_carbs}, {daily_fats}, {daily_fiber})")
    connection.commit()
    cursor.close()
    
def db_user_goal(connection: Any, usr_id: int):
    goal_string = return_reqest(connection, f"SELECT goal FROM users WHERE id = {usr_id}")
    return goal_string[0][0]