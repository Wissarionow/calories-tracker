from database import connect_to_db, db_login, return_reqest,disconnect
import streamlit as st

def login_screen():

    st.title('Please login or Register(register in progress)')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    if st.button('Login'):
        connection = connect_to_db()
        
        if db_login(connection, username, password):
            st.success('Login successful')
            st.session_state.usr_id = return_reqest(connection, f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'")[0][0]
            disconnect(connection)
            st.rerun()
        else:
            st.error('Incorrect password or username')

    return st.session_state.usr_id
