import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
from typing import Any


#establish connection, if None is returned, connection failed
def connect_to_db():
    env = dotenv_values(".env")
    try:
        connection = mysql.connector.connect(
        host=env['DB_HOST'],        
        user=env['DB_USER'],        
        password=env['DB_PASS'],        
        database=env['DB_NAME'],      
        auth_plugin=env['DB_AUTH_PLUGIN']
    )
        
        if connection.is_connected():
            return connection
        
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

#return request
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
    
    
#void disconnect 
def disconnect(connection:any):
    connection.close()