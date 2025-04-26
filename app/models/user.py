# app/models/user_model.py
from app import mysql

def get_user_by_id(user_id):
    cursor = mysql.connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user
