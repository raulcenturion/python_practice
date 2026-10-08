# Rutas de autenticación de la sección 8.
# POST /api/v1/auth/login  → entrega el JWT.
# GET  /api/v1/auth/me     → dice quién es el dueño del token.
#
# El prefix "/auth" se suma al "/api/v1" que pone main.py al incluir este router.
#
# datetime.timedelta              → biblioteca estándar. Cuánto vive el token.
# fastapi.APIRouter              → el grupo de rutas.
# fastapi.security.OAuth2PasswordRequestForm
#   → lee usuario y clave como formulario (no como JSON).
#     Swagger y el botón Authorize mandan application/x-www-form-urlencoded.
#     El campo se llama username. En esta clase el valor es el email.
# app.core.security               → crea el token y lee el usuario del header.

from datetime import timedelta

from app.core.security import create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

from fastapi import APIRouter, Depends, HTTPException, status

from .schemas import Token, UserPublic

# Usuarios de práctica. La clave está en texto plano a propósito: la clase
# todavía no hashea. No es una tabla y no sirve fuera de este ejercicio.
# La clave del dict es el email, porque el formulario manda ese email en "username".
FAKE_USERS = {
    "ricardo@example.com": {
        "email": "ricardo@example.com",
        "username": "ricardo",
        "password": "secret123",
    },
    "alumno@example.com": {
        "email": "alumno@example.com",
        "username": "alumno",
        "password": "123456",
    },
}

router = APIRouter(prefix="/auth", tags=["auth"])


# Depends() sin argumento arma el formulario. FastAPI lo documenta en /docs.
# La clase 8 lo escribió async def login. Hoy es def: FAKE_USERS está en memoria
# y no hay await. Si el usuario se buscara en la base, sería async y esa consulta
# iría con await, para no frenar el resto de los requests. Misma idea que
# get_current_user en core/security.py.
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = FAKE_USERS.get(form_data.username)
    # Misma respuesta si el email no existe o si la clave no coincide.
    # Así no se cuenta cuál de las dos falló.
    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
        )

    # sub queda con el email. username viaja aparte, para /me y para el autor del post.
    token = create_access_token(
        data={"sub": user["email"], "username": user["username"]},
        expires_delta=timedelta(minutes=30),
    )

    return {"access_token": token, "token_type": "bearer"}


# get_current_user rechaza la petición si el token falta, venció o no firma con SECRET_KEY.
# La clase 8 lo escribió async def read_me. Hoy es def porque solo arma el JSON.
# Pasaría a async con await si /me tuviera que esperar otra lectura.
@router.get("/me", response_model=UserPublic)
def read_me(current=Depends(get_current_user)):
    return {"email": current["email"], "username": current["username"]}
