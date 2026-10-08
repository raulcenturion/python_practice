# Sección 8 (auth). Firma y revisa el JWT, y dice quién está logueado.
#
# Un JWT es un texto con tres partes (header.payload.firma). Lo arma PyJWT.
# El cliente lo manda en el header: Authorization: Bearer <token>.
# La clave que firma vive en SECRET_KEY. Quien la tiene puede fabricar tokens.
#
# os                         → biblioteca estándar. Lee SECRET_KEY del entorno.
# datetime                   → biblioteca estándar. La fecha de vencimiento (exp).
# jwt                        → paquete PyJWT (pip install PyJWT). encode firma, decode verifica.
#   ExpiredSignatureError    → el token venció.
#   InvalidTokenError        → firma mala, token cortado o algoritmo distinto.
# fastapi.Depends            → engancha get_current_user en una ruta.
# fastapi.HTTPException      → 401 si no hay sesión válida, 403 si no alcanza el permiso.
# fastapi.security.OAuth2PasswordBearer
#   → saca el token del header. tokenUrl es la ruta de login que muestra Swagger
#     en el botón Authorize. Tiene que coincidir con la URL real: /api/v1/auth/login.

import os
from datetime import datetime, timedelta, timezone

import jwt
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from fastapi import Depends, HTTPException, status

# Si .env no trae la clave, se usa este texto. En un servidor real no se deja el default.
SECRET_KEY = os.getenv("SECRET_KEY", "change-me-in-prod")
# HS256: la misma clave firma y verifica. Es un algoritmo de PyJWT, no de FastAPI.
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

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
