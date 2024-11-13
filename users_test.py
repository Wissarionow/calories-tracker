import streamlit as st
from database import return_reqest , connect_to_db, disconnect

def login_screen():
    st.empty()
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    if login_button:
        connection = connect_to_db()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        result = return_reqest(connection, query)
        if result:
            st.success("Logged in successfully")
        else:
            st.error("Invalid credentials")
        disconnect(connection)
        
def load_user_data():
    connection = connect_to_db()
   
    disconnect(connection)
    
login_screen()