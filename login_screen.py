from database import connect_to_db, db_login, return_reqest, db_login_email, disconnect
import streamlit as st
from st_paywall import add_auth  # type: ignore

def login():
    login_screen_g()
    login_screen()
    return st.session_state.usr_id

def login_screen():
    with st.sidebar: 
        st.markdown('### or please login by username')
        username = st.text_input('Username')
        password = st.text_input('Password', type='password')
        if st.button('Login'):
            connection = connect_to_db()
        
            if db_login(connection, username, password):
                st.success('Login successful')
                st.session_state.usr_id = return_reqest(connection, f"SELECT id FROM users WHERE username = '{username}' AND password = '{password}'")[0][0]
            else:
                st.error('Incorrect password or username')
            disconnect(connection)
        return st.session_state.usr_id

def login_screen_g():
     # Domyślnie rozwinięty sidebar
    st.sidebar.checkbox('Menu', value=True)
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
        connection=connect_to_db()
        if db_login_email(connection, st.session_state.email): 
            st.success("User exist!") 
            st.query_params.update(logged_in=True)
        disconnect(connection)
        return st.session_state.usr_id
    

    