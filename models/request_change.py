from database import get_db_connection


class RequestChange:
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'

    def __init__(self, id=None, user_id=None, time_entry_id=None, reason=None, status=None):
        self.id = id
        self.user_id = user_id
        self.time_entry_id = time_entry_id
        self.reason = reason
        self.status = status

    @classmethod
    def create(cls, user_id, time_entry_id, reason):
        """asks for a change in the score entry"""
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """INSERT INTO ChangeRequests 
                (user_id, time_entry_id, reason, status) 
                VALUES (%s, %s, %s, %s)""",
                (user_id, time_entry_id, reason, cls.PENDING)
            )
            conn.commit()
            return cls(cursor.lastrowid, user_id, time_entry_id, reason, cls.PENDING)
        except Exception as e:
            print(f"error trying to create request: {e} T-T")
            return None
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def get_pending_requests(cls):
        """Get every pending requests"""
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT * FROM ChangeRequests WHERE status = %s",
                (cls.PENDING,)
            )
            return [cls(**request) for request in cursor.fetchall()]
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def update_status(cls, request_id, status, admin_id):
        """Atualiza o status de uma solicitação"""
        valid_statuses = [cls.APPROVED, cls.REJECTED]
        if status not in valid_statuses:
            raise ValueError(f"invalid format: {valid_statuses} use either APPROVED or REJECTED")

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """UPDATE ChangeRequests 
                SET status = %s 
                WHERE id = %s""",
                (status, request_id)
            )
            conn.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            conn.close()