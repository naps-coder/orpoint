from datetime import datetime
import hashlib
from database import get_db_connection


class User:
    def __init__(self, id=None, email=None, password_hash=None, is_admin=False):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin

    @classmethod
    def create(cls, email, password, is_admin=False):
        """method to create a user"""
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO users (email, password_hash, is_admin) VALUES (%s, %s, %s)",
                (email, password_hash, is_admin)
            )
            conn.commit()
            return cls(cursor.lastrowid, email, password_hash, is_admin)
        except mysql.connector.Error as err:
            print(f"error trying to create user {err} :(")
            return None
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_by_email(cls, email):
        """search for user by email"""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user_data = cursor.fetchone()
            if user_data:
                return cls(**user_data)
            return None
        finally:
            cursor.close()
            conn.close()

    def verify_password(self, password):
        """function to verify password"""
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    @classmethod
    def make_admin(cls, user_id):
        """this is a method to give admin privileges to a user!"""
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "UPDATE users SET is_admin = TRUE WHERE id = %s",
                (user_id,)
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()