#connecting to DB
import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Toyatodo@24",  
        database="url_short"
    )