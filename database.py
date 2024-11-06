import psycopg2
from dotenv import dotenv_values

env = dotenv_values(".env")

#establish connection
def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",  
            database=env["DATABASE_NAME"],  
            user=env["DATABASE_USER"],  
            password=env["DATABASE_PASSWORD"]  
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

#return request
def return_reqest(connection,query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None

#void disconnect 
def disconnect(connection):
    connection.close()