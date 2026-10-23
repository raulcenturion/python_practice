# Rutas de auth. Prefijo /auth. main.py le suma /api/v1.
#
# APIRouter          → grupo de rutas de FastAPI.
# status             → 201 en el registro.
# OAuth2PasswordRequestForm → el form que manda Swagger (username y password).
# DBSession          → la sesión, de api/deps.py.
# UserCreate/UserRead → body y respuesta. UserRead no trae la clave.
# AuthService        → register y login.

from typing import Annotated

from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import DBSession
from app.models.user import UserCreate, UserRead
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: DBSession):
    return AuthService(UserRepository(db)).register(payload)


@router.post("/login")
def login(email: str, password: str, db: DBSession):
    # email y password no son un modelo: FastAPI los lee como query params.
    token = AuthService(UserRepository(db)).login(email, password)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/token")
def login_token(
    db: DBSession,
    form: Annotated[OAuth2PasswordRequestForm, Depends()],
):
    # La clase nombra esta función igual que login. El segundo def pisa el nombre
    # en el módulo. La ruta igual se registra, pero el nombre queda duplicado.
    # form.username es el email: el form de OAuth2 no tiene campo email.
    # Depends() va en Annotated. La clase lo pone como valor por defecto:
    #     form: OAuth2PasswordRequestForm = Depends()
    token = AuthService(UserRepository(db)).login(form.username, form.password)
    return {"access_token": token, "token_type": "bearer"}
