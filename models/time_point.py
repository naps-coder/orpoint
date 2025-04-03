from datetime import datetime
from database import get_db_connection


class TimePoint:
    ENTRY = 'entry'
    EXIT = 'exit'

    def __init__(self, id=None, user_id=None, timestamp=None, type=None):
        self.id = id
        self.user_id = user_id
        self.timestamp = timestamp
        self.type = type

    @classmethod
    def create(cls, user_id, entry_type):
        """Registering a score entry"""
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "INSERT INTO TimeEntries (user_id, timestamp, type) VALUES (%s, %s, %s)",
                (user_id, datetime.now(), entry_type)
            )
            conn.commit()
            return cls(cursor.lastrowid, user_id, datetime.now(), entry_type)
        except Exception as e:
            print(f"something went wrong trying to register the score: {e} ;-;")
            return None
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_by_user(cls, user_id, limit=None):
        """consulting score entries by user"""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            query = "SELECT * FROM TimeEntries WHERE user_id = %s ORDER BY timestamp DESC"
            params = (user_id,)

            if limit:
                query += " LIMIT %s"
                params = (user_id, limit)

            cursor.execute(query, params)
            return [cls(**entry) for entry in cursor.fetchall()]
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_last_entry(cls, user_id):
        """get last entry by  user"""
        entries = cls.get_by_user(user_id, limit=1)
        return entries[0] if entries else None