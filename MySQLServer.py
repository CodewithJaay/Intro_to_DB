import mysql.connector
from mysql.connector import Error

def create_database():
    try:
    
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='R!d@n*t-a#9887'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
     print("Error: Could not connect to MySQL server.")
     print(f"Details: {err}")


    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
