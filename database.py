import mysql.connector
from mysql.connector import Error
from dotenv import dotenv_values
from typing import Any

env = dotenv_values(".env")

#establish connection, if None is returned, connection failed
def connect_to_db():
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

#void disconnect 
def disconnect(connection:any):
    connection.close()