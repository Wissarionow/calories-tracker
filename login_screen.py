from database import connect_to_db, db_login, return_reqest,disconnect, db_login_email
import streamlit as st
from st_paywall import add_auth  # type: ignore

def login():
    login_screen_g()
    login_screen()
    return st.session_state.usr_id

def login_screen():
    with st.sidebar: 
        st.markdown('### Please login by username')
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

def login_screen_g():
     
    with st.sidebar: 
        st.markdown('### Login by Google')
    
        try:
            add_auth(
            required=False,
            login_sidebar=True,
            login_button_text="Log by Google",

            )
        
        except KeyError:
            pass
        
        if st.session_state.get('email'):
            st.markdown(f"You logged by: {st.session_state['email']}")
            
        if db_login_email(connect_to_db(), st.session_state.email): 
            st.success("User exist!") 
        # else: 
        #     st.error("Użytkownik nie istnieje! Zarejestruj się, aby kontynuować.")
        return st.session_state.usr_id
    

    # if 'usr_id' not in st.session_state:
    #     st.session_state.usr_id = None

    # if st.session_state.usr_id is None:
    #     st.session_state.usr_id = login_screen()

# def register_screen():
#
#     st.title('Please register')
#     username = st.text_input('Username')
#     password = st.text_input('Password', type='password')
#     weight = st.number_input('How much do you weight?', min_value=0)
#     height = st.number_input('How tall are you?', min_value=0)
    