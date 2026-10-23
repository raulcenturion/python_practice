# Dependencias de las rutas. La sección 17 las arma acá, no en cada router.
#
# Annotated              → biblioteca estándar. Junta el tipo con Depends.
# fastapi.Depends        → FastAPI llama a la función y pasa el resultado al endpoint.
# HTTPException/status   → 401 cuando el token no sirve.
# OAuth2PasswordBearer   → Swagger manda el token a tokenUrl.
# sqlmodel.Session       → la sesión que reciben los servicios.
# get_session            → el generador de core/db.py, el with Session.
# decode_token           → core/security.py.
# UserRepository         → busca al dueño del token.

from collections.abc import Iterator
from typing import Annotated

import jwt
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from app.core.db import get_session
from app.core.security import decode_token
from app.models.user import User
from app.repositories.user_repository import UserRepository
from fastapi import Depends, HTTPException, status

# Swagger Authorize pega el form en esta ruta.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")


def get_db() -> Iterator[Session]:
    # La clase hace `return next(get_session())`.
    # next() avanza el generador hasta el yield y después lo suelta.
    # El with de get_session se cierra cuando el recolector tira ese generador,
    # a veces antes de que el endpoint use la sesión.
    # yield from deja el with abierto durante el request y lo cierra al salir.
    yield from get_session()


# Atajo: db: DBSession en vez de db: Session = Depends(get_db).
DBSession = Annotated[Session, Depends(get_db)]


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: DBSession) -> User:
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No autorizado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_token(token)
        sub = payload.get("sub")
        if sub is None:
            raise ValueError("el token no trae sub")
        user_id = int(sub)
    except (jwt.PyJWTError, ValueError, TypeError):
        # La clase atrapa Exception. Acá solo lo que realmente falla:
        # token inválido (PyJWT) o un sub que no es un entero.
        raise credentials_exc from None

    user = UserRepository(db).get_by_id(user_id)
    if not user:
        raise credentials_exc

    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
