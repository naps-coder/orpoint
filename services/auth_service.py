from user import User
import getpass


class AuthService:
    def __init__(self):
        self.current_user = None

    def login(self, email, password):
        """Autentica um usuário"""
        user = User.get_by_email(email)
        if not user or not user.verify_password(password):
            raise ValueError("Credenciais inválidas")
        self.current_user = user
        return user

    def register(self, email, password, is_admin=False):
        """Registra um novo usuário"""
        if User.get_by_email(email):
            raise ValueError("Email já cadastrado")

        if len(password) < 6:
            raise ValueError("Senha deve ter pelo menos 6 caracteres")

        return User.create(email, password, is_admin)

    def get_current_user(self):
        """Retorna o usuário atualmente autenticado"""
        if not self.current_user:
            raise ValueError("Nenhum usuário autenticado")
        return self.current_user