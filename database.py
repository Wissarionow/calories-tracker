import psycopg2
from dotenv import dotenv_values

env = dotenv_values(".env")

def return_reqest(request):
    try:
        connection = psycopg2.connect(
            host="localhost",  
            database=env["DATABASE_NAME"],  
            user=env["DATABASE_USER"],  
            password=env["DATABASE_PASSWORD"]  
        )
        with connection.cursor() as cursor:
            cursor.execute(request)
            result = cursor.fetchall()
            return result
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return None
