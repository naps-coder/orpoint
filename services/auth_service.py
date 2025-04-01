from models.user import User
from database import get_db_connection

def login(email, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, password_hash, is_admin FROM Users WHERE email = %s", (email,))
    user_data = cursor.fetchone()
    if user_data and user_data[1] == password:  # gotta change it to hash sometime
        return User(*user_data)
    return None