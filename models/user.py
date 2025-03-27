class User:
    def __init__(self, id, email, password_hash, is_admin):
        self.id = id
        self.email = email
        self.password_hash = password_hash
        self.is_admin = is_admin