import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
from typing import Any

env = dotenv_values(".env")

#establish connection, if None is returned, connection failed
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",  
            database=env["DATABASE_NAME"],  
            user=env["DATABASE_USER"],  
            password=env["DATABASE_PASSWORD"],
            auth_plugin='mysql_native_password'  
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

#void disconnect 
def disconnect(connection:any):
    connection.close()