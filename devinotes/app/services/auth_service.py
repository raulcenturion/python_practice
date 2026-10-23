# Registro y login. El router no toca el repositorio: lo hace este servicio.
#
# HTTPException → 400 si el mail existe, 401 si la clave no cierra.
# hash/verify/create_access_token → core/security.py.
# User / UserCreate → modelo de tabla y el body del registro.
# UserRepository    → get_by_email y create.

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User, UserCreate
from app.repositories.user_repository import UserRepository
from fastapi import HTTPException


class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, payload: UserCreate) -> User:
        if self.repo.get_by_email(payload.email):
            raise HTTPException(status_code=400, detail="Email ya registrado")

        # La clase corta la clave en 72 caracteres: el tope de bcrypt.
        # PasswordHash.recommended() usa Argon2, que no tiene ese tope.
        # Se deja el corte para que el login y el registro miren el mismo texto.
        user = User(
            email=payload.email,
            full_name=payload.full_name,
            hashed_password=hash_password(payload.password[:72]),
        )
        return self.repo.create(user)

    def login(self, email: str, password: str) -> str:
        user = self.repo.get_by_email(email)
        if not user or not verify_password(password[:72], user.hashed_password):
            raise HTTPException(status_code=401, detail="Credenciales inválidas")

        # sub es el id en texto. get_current_user lo vuelve a int.
        return create_access_token({"sub": str(user.id)})
