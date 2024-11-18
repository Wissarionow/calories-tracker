from database import connect_to_db, db_login, return_reqest
import streamlit as st

def login_screen():
    if 'usr_id' not in st.session_state:
        st.session_state.usr_id = None

    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    if st.button('Login'):
        connection = connect_to_db()
        if db_login(connection, username, password):
            st.success('Login successful')
            st.session_state.usr_id = return_reqest(connection, f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'")
            st.rerun()
        else:
            st.error('Incorrect password or username')

    return st.session_state.usr_id