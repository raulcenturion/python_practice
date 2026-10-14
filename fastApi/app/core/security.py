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
#   → saca el token del header. tokenUrl es la ruta de login que muestra Swagger
#     en el botón Authorize. Tiene que coincidir con la URL real: /api/v1/auth/login.
# app.core.config.settings   → sección 11. La clave, el algoritmo y los minutos.
# typing.Literal             → los tres roles de require_role.
#
# La clase importa además:
#   from click import pass_context   click es de terminales. pass_context no se usa.
#   from sqlmodel import Session     este proyecto usa SQLAlchemy, no SQLModel.
#   from app.models.user import User lo usaría el get_current_user nuevo, comentado abajo.
# os.getenv se mudó a config.py. Acá ya no hace falta importar os.

from datetime import datetime, timedelta, timezone
from typing import Literal

import jwt
from app.core.config import settings
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from pwdlib import PasswordHash

from fastapi import Depends, HTTPException, status

# Antes estas tres líneas leían el entorno acá:
# SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-prod")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
# Sección 11 las centraliza en core/config.py. Los nombres de acá siguen,
# para no tocar create_access_token ni el login de la sección 8.
SECRET_KEY = settings.JWT_SECRET
ALGORITHM = settings.JWT_ALG
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

# Argon2. hash() devuelve un string que se guardaría en users.hashed_password.
# verify() compara el texto que escribió la persona con ese string.
# El login de FAKE_USERS todavía compara la clave en texto plano. Estas dos
# funciones quedan listas para cuando el login lea la tabla users.
password_hash = PasswordHash.recommended()

# tokenUrl es relativo al servidor. Swagger manda usuario y clave a esa ruta.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

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


# Sección 11. Otro 401, con otro texto. La clase lo usa cuando el token
# no se puede leer o cuando el usuario de la tabla no existe o está inactivo.
# get_current_user de abajo sigue usando credentials_exc ("No autenticado").
def invalid_credentials():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales inválidas",
    )


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    # copy() para no modificar el dict que mandó el login.
    to_encode = data.copy()
    # exp es el claim estándar de vencimiento. PyJWT lo compara con la hora UTC.
    # La clase escribe Optional[timedelta]. timedelta | None es el equivalente.
    expire = datetime.now(tz=timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    # jwt.encode devuelve el string del token. key es SECRET_KEY.
    token = jwt.encode(payload=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return token


def decode_token(token: str) -> dict:
    # algorithms es una lista a propósito: si el token dice otro algoritmo, se rechaza.
    # La clase nombra la variable playload. Es un typo de payload; acá va el nombre correcto.
    payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
    return payload


# Depends(oauth2_scheme) exige el header Authorization. Si falta, FastAPI responde 401
# antes de entrar a esta función.
#
# La clase 8 la escribió async:
# async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
#
# Hoy es def porque adentro no hay nada que esperar: decode_token es un cálculo
# en memoria. async sin await no espera y el editor avisa.
#
# Cuando la revisión implique una espera (buscar el usuario en la base, llamar
# a otro servicio), vuelve a ser async y esa espera se escribe con await:
#     user = await buscar_usuario(sub)
# Mientras el await espera, el servidor puede atender otros requests.
# Eso es lo que evita el bloqueo. FastAPI acepta las dos formas en un Depends.
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = decode_token(token)
        # sub es el sujeto del token. En el login guardamos el email ahí.
        sub: str | None = payload.get("sub")
        username: str | None = payload.get("username")
        if not sub or not username:
            raise credentials_exc

        # Este dict es el "usuario actual". create_post lo usa como autor.
        return {"email": sub, "username": username}
    except ExpiredSignatureError:
        raise raise_expired_token()
    except InvalidTokenError:
        raise credentials_exc


# La clase 11 reemplaza get_current_user por esto. No está activo.
#
# async def get_current_user(
#     db: Session = Depends(get_db),
#     token: str = Depends(oauth2_scheme),
# ) -> User:
#     try:
#         playload = decode_token(token)
#         sub = playload.get("sub")
#         username = playload.get("username")
#         if not sub or not username:
#             raise credentials_exc
#         user_id = int(sub)
#     except ExpiredSignatureError:
#         raise raise_expired_token()
#     except InvalidTokenError:
#         raise credentials_exc
#     except PyJWTError:
#         raise invalid_credentials()
#     user = db.get(User, user_id)
#     if not user or not user.is_active:
#         raise invalid_credentials()
#     return user
#
# No reemplaza a la función de arriba por tres motivos:
# 1. El login sigue guardando el email en sub, no el id de la tabla users.
#    int(sub) con "ricardo@example.com" lanza ValueError, que esta función no atrapa.
# 2. Pide username dentro del token y, a la vez, la clase cambia create_access_token
#    para guardar solo sub y exp. Un token armado con esa firma nueva no trae
#    username, así que el if not username siempre rechazaría la sesión.
#    Esa firma nueva, comentada, sería:
#    def create_access_token(sub: str, minutes: int | None = None) -> str:
#        expire = datetime.now(timezone.utc) + timedelta(
#            minutes=minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
#        )
#        return jwt.encode(
#            {"sub": sub, "exp": expire},
#            settings.JWT_SECRET,
#            algorithm=settings.JWT_ALG,
#        )
#    El login llama create_access_token(data=..., expires_delta=...).
#    Cambiar la firma rompe ese llamado. Se deja la de la sección 8.
# 3. Es async y no tiene await. La lectura db.get es síncrona. El editor avisa,
#    igual que en la sección 8. Cuando el usuario salga de la base y esa espera
#    sea real, la función vuelve a ser async y la consulta va con await.
#
# decode_token de la clase usa settings.SECRET_KEY y settings.ALGORITHM,
# y nombra la variable playload. Esos dos nombres existen en config.py
# como alias de JWT_SECRET y JWT_ALG. La función activa usa SECRET_KEY y ALGORITHM.


def hash_password(plain: str) -> str:
    # plain es la clave que escribió la persona. El resultado no se puede revertir.
    return password_hash.hash(plain)


def verify_password(plain: str, hashed: str) -> bool:
    # True si plain coincide con el hash guardado. False si no.
    return password_hash.verify(plain, hashed)


# Devuelve una dependencia. require_role("editor") se usa como Depends(require_editor).
# order compara roles: user < editor < admin. Si el rol es menor, 403.
# Hoy ninguna ruta la usa. get_current_user devuelve un dict (email, username),
# y un dict no tiene .role. Cuando el usuario salga de la tabla users, esta
# función recibe ese User y user.role existe.
def require_role(min_role: Literal["user", "editor", "admin"]):
    order = {"user": 0, "editor": 1, "admin": 2}

    def evaluation(user=Depends(get_current_user)):
        if order[user.role] < order[min_role]:
            raise raise_frobidden()
        return user

    return evaluation


# Atajos. En una ruta: user: User = Depends(require_editor)
require_user = require_role("user")
require_editor = require_role("editor")
require_admin = require_role("admin")
