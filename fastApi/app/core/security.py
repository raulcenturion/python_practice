# Sección 8 (auth). Firma y revisa el JWT, y dice quién está logueado.
#
# Un JWT es un texto con tres partes (header.payload.firma). Lo arma PyJWT.
# El cliente lo manda en el header: Authorization: Bearer <token>.
# La clave que firma vive en SECRET_KEY. Quien la tiene puede fabricar tokens.
#
# datetime                   → biblioteca estándar. La fecha de vencimiento (exp).
# jwt                        → paquete PyJWT (pip install PyJWT). encode firma, decode verifica.
#   ExpiredSignatureError    → el token venció.
#   InvalidTokenError        → firma mala, token cortado o algoritmo distinto.
#   PyJWTError               → la clase también lo atrapa. Cubre el resto de fallos de PyJWT.
# pwdlib.PasswordHash        → paquete pwdlib (pip install "pwdlib[argon2]").
#   recommended() hashea con Argon2. No es PyJWT ni FastAPI.
# fastapi.Depends            → engancha get_current_user en una ruta.
# fastapi.HTTPException      → 401 si no hay sesión válida, 403 si no alcanza el permiso.
# fastapi.security.OAuth2PasswordBearer
#   → saca el token del header. tokenUrl es la ruta que muestra Swagger
#     en el botón Authorize. Sección 12: /api/v1/auth/token (formulario).
#     Antes era /api/v1/auth/login. /login ahora recibe JSON, y Swagger
#     no manda JSON en ese botón: manda usuario y clave como formulario.
# fastapi.security.OAuth2PasswordRequestForm
#   → ese formulario. Lo lee auth2_token. El campo se llama username.
# sqlalchemy.orm.Session     → la sesión. La clase importa Session desde sqlmodel.
#   Este proyecto no usa SQLModel. La sesión es la de SQLAlchemy, la misma de get_db.
# app.core.db.get_db         → abre esa sesión por request.
# app.models.user.User       → la fila que devuelve get_current_user.
# app.core.config.settings   → sección 11. La clave, el algoritmo y los minutos.
# typing.Literal             → los tres roles de require_role.
#
# La clase importa además:
#   from click import pass_context   click es de terminales. pass_context no se usa.
# os.getenv se mudó a config.py. Acá ya no hace falta importar os.
#
# La clase también importa UserRepository al inicio de este archivo, para /token.
# Eso hace que core importe una capa de api. auth2_token llama al servicio
# adentro de la función, cuando el módulo ya terminó de cargarse, para no
# armar un círculo: service.py importa create_access_token desde acá.

from datetime import datetime, timedelta, timezone
from typing import Literal

import jwt
from app.core.config import settings
from app.core.db import get_db
from app.models.user import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError, PyJWTError
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from fastapi import Depends, HTTPException, status

# Antes estas tres líneas leían el entorno acá:
# SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-prod")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
# Sección 11 las centraliza en core/config.py. Estas tres líneas las usaba
# create_access_token de la sección 8. La sección 12 firma con settings.JWT_SECRET.
# SECRET_KEY = settings.JWT_SECRET
# ALGORITHM = settings.JWT_ALG
# ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

# Argon2. hash() devuelve el string que se guarda en users.hashed_password.
# verify() compara el texto que escribió la persona con ese string.
# El login de la sección 12 usa estas dos. FAKE_USERS comparaba la clave en texto plano.
password_hash = PasswordHash.recommended()

# tokenUrl es relativo al servidor. Swagger manda usuario y clave a esa ruta.
# Sección 8: tokenUrl="/api/v1/auth/login"
# Sección 12: el botón Authorize pega a /token, que sigue siendo un formulario.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

# 401: no está autenticado (no hay token, o el token no sirve).
# WWW-Authenticate le dice al cliente que el esquema es Bearer.
credentials_exc = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="No autenticado",
    headers={"WWW-Authenticate": "Bearer"},
)


# La clase la llama raise_expired_token, pero no lanza: devuelve la excepción.
# El raise está en get_current_user. El 401 de "venció" se distingue del de "no sirve".
def raise_expired_token():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )


# Todavía ninguna ruta la usa. La clase la deja lista para cuando haya roles.
# El nombre en la clase es raise_frobidden (le falta la "d" de forbidden).
# 403: el token es válido, pero ese usuario no puede hacer la acción.
def raise_frobidden():
    return HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="No tienes permisos suficientes",
    )


# Sección 11. Otro 401, con otro texto. La sección 12 lo usa cuando el token
# no se puede leer, cuando la clave no coincide, o cuando el usuario de la
# tabla no existe o está inactivo.
# get_current_user usa credentials_exc ("No autenticado") si falta sub,
# y este 401 si la fila no está o está inactiva.
def invalid_credentials():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales inválidas",
    )


# Sección 8. El login metía un dict (email en sub, más username) y un timedelta.
# La sección 12 lo comenta en la clase y lo reemplaza por create_access_token(sub, minutes).
# def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
#     to_encode = data.copy()
#     expire = datetime.now(tz=timezone.utc) + (
#         expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     )
#     to_encode.update({"exp": expire})
#     token = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
#     return token


# sub es el id del usuario, en texto. El token solo lleva sub y exp.
# No lleva username: la sección 12 lo saca. minutes=None usa el valor del .env.
def create_access_token(sub: str, minutes: int | None = None) -> str:
    expire = datetime.now(tz=timezone.utc) + timedelta(
        minutes=minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    # La clase firma con settings.JWT_SECRET y settings.JWT_ALG.
    # SECRET_KEY y ALGORITHM de este archivo son los mismos valores.
    return jwt.encode(
        {"sub": sub, "exp": expire},
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALG,
    )


def decode_token(token: str) -> dict:
    # algorithms es una lista a propósito: si el token dice otro algoritmo, se rechaza.
    # La clase nombra la variable playload. Es un typo de payload; acá va el nombre correcto.
    # Sección 11 este decode usaba settings.SECRET_KEY y settings.ALGORITHM,
    # nombres que config.py no tenía (solo JWT_SECRET y JWT_ALG). Esos alias se
    # agregaron para que no reviente. La sección 12 pasa a JWT_SECRET y JWT_ALG.
    payload = jwt.decode(
        jwt=token,
        key=settings.JWT_SECRET,
        algorithms=[settings.JWT_ALG],
    )
    return payload


# Depends(oauth2_scheme) exige el header Authorization. Si falta, FastAPI responde 401
# antes de entrar a esta función.
#
# Sección 8. Devolvía el dict del token, sin mirar la tabla:
# def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
#     payload = decode_token(token)
#     sub = payload.get("sub")          # el email
#     username = payload.get("username")
#     if not sub or not username:
#         raise credentials_exc
#     return {"email": sub, "username": username}
#
# Sección 11. Buscaba la fila, pero además exigía username. El token nuevo no lo trae,
# así que esa versión rechazaba toda sesión. La sección 12 saca el chequeo de username.
# async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
#     playload = decode_token(token)
#     sub = playload.get("sub")
#     username = playload.get("username")
#     if not sub or not username:
#         raise credentials_exc
#     user_id = int(sub)
#
# La clase 12 la escribe async. Acá es def: db.get es una lectura síncrona, no hay await.
# async sin await no espera y el editor avisa. Si la sesión fuera async, la línea
# sería `user = await db.get(User, user_id)` y la función volvería a ser async.
# Mientras ese await espera, el servidor puede atender otros requests.
def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
) -> User:
    try:
        payload = decode_token(token)
        # sub es el id de users, en texto. Lo puso create_access_token.
        sub: str | None = payload.get("sub")
        # Sección 11 también leía username y rechazaba el token si faltaba.
        # La sección 12 lo quita: el token ya no guarda ese dato.
        if not sub:
            raise credentials_exc

        user_id = int(sub)
    except ExpiredSignatureError:
        raise raise_expired_token()
    except InvalidTokenError:
        raise credentials_exc
    except PyJWTError:
        # Cubre lo que no entró en las dos de arriba. La clase lo agrega en la 11.
        raise invalid_credentials()
    except ValueError:
        # La clase no atrapa esto. int("ricardo@example.com") lanza ValueError
        # y FastAPI lo vería como 500. Un token de la sección 8 trae el email en sub.
        raise credentials_exc

    # db.get busca por id. None si esa fila no está.
    user = db.get(User, user_id)

    if not user or not user.is_active:
        raise invalid_credentials()

    return user


def hash_password(plain: str) -> str:
    # plain es la clave que escribió la persona. El resultado no se puede revertir.
    return password_hash.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    # True si plain coincide con el hash guardado. False si no.
    return password_hash.verify(plain, hashed)


# Formulario de Swagger (POST /api/v1/auth/token).
# La clase lo escribe async y arma el usuario con UserRepository acá mismo:
# async def auth2_token(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     repository = UserRepository(db)
#     user = repository.get_by_email(form.username)
#     if not user or not verify_password(form.password, user.hashed_password):
#         raise invalid_credentials()
#     token = create_access_token(sub=str(user.id))
#     return {"access_token": token, "token_type": "bearer"}
# El nombre auth2_token le falta la "o" de oauth2. Se deja el de la clase.
# Es def porque no hay await. El chequeo de la clave vive en AuthService,
# el mismo que usa POST /login, para no repetirlo.
def auth2_token(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    from app.api.v1.auth.service import AuthService

    return AuthService(db).token_for(form.username, form.password)


# Devuelve una dependencia. En una ruta: Depends(require_editor).
# order compara roles: user < editor < admin. Si el rol es menor, 403.
# La sección 12 la engancha en tags (crear y editar: editor, borrar: admin,
# el más usado: user) y en PUT /auth/role (admin).
def require_role(min_role: Literal["user", "editor", "admin"]):
    order = {"user": 0, "editor": 1, "admin": 2}

    def evaluation(user: User = Depends(get_current_user)) -> User:
        if order[user.role] < order[min_role]:
            raise raise_frobidden()
        return user

    return evaluation


# Atajos. En una ruta: user: User = Depends(require_editor)
require_user = require_role("user")
require_editor = require_role("editor")
require_admin = require_role("admin")
