from datetime import datetime
from time_entry import TimeEntry
from change_request import ChangeRequest
from auth_service import AuthService


class PointService:
    def __init__(self):
        self.auth_service = AuthService()

    def register_entry(self, email):
        """registers an entry"""
        user = self.auth_service.get_current_user()
        last_entry = TimeEntry.get_last_entry(user.id)

        if last_entry and last_entry.type == TimeEntry.ENTRY:
            raise ValueError("there is already an entry without exit")

        return TimeEntry.create(user.id, TimeEntry.ENTRY)

    def register_exit(self, email):
        """registers an exit"""
        user = self.auth_service.get_current_user()
        last_entry = TimeEntry.get_last_entry(user.id)

        if not last_entry or last_entry.type == TimeEntry.EXIT:
            raise ValueError("there is not an entry for you to register an exit!!")

        return TimeEntry.create(user.id, TimeEntry.EXIT)

    def list_entries(self, email, limit=20):
        """lists the last 20 user's entries"""
        user = self.auth_service.get_current_user()
        return TimeEntry.get_by_user(user.id, limit)

    def create_change_request(self, email, entry_id, reason):
        """ask for a change in the score entry"""
        user = self.auth_service.get_current_user()
        entry = TimeEntry.get_by_id(entry_id)

        if not entry or entry.user_id != user.id:
            raise ValueError("invalid format.")

        return ChangeRequest.create(user.id, entry_id, reason)