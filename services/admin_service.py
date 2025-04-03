from user import User
from change_request import ChangeRequest
from auth_service import AuthService

class AdminService:
    def __init__(self):
        self.auth_service = AuthService()

    def _check_admin(self):
        """check if the user is an admin"""
        user = self.auth_service.get_current_user()
        if not user.is_admin:
            raise PermissionError("access denied: you don't have admin privileges >:(")
        return user

    def approve_request(self, request_id):
        """aproves a request"""
        self._check_admin()
        return ChangeRequest.update_status(request_id, ChangeRequest.APPROVED)

    def reject_request(self, request_id):
        """reject user request"""
        self._check_admin()
        return ChangeRequest.update_status(request_id, ChangeRequest.REJECTED)

    def list_users(self):
        """lists every user"""
        self._check_admin()
        return User.get_all()

    def make_admin(self, user_id):
        """I GRANT YOU: ADMIN PRIVILEGES!!!!"""
        self._check_admin()
        return User.make_admin(user_id)

    def get_pending_requests(self):
        """Show pending requests"""
        self._check_admin()
        return ChangeRequest.get_pending_requests()