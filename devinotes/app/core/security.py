# Contraseñas y JWT. La sección 17 lo agrega.
#
# pwdlib.PasswordHash → ya está en el blog (sección 11). recommended() usa Argon2.
# jwt                  → el paquete instalado es PyJWT. encode y decode del token.
# settings             → secreto, algoritmo y minutos de vida, de core/config.py.

from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

pwd_context = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(data: dict, minutes: int | None = None) -> str:
    to_encode = data.copy()
    # La clase usa datetime.utcnow(), que Python marca como obsoleto.
    # now(timezone.utc) es el mismo instante, con zona.
    expire = datetime.now(timezone.utc) + timedelta(minutes=minutes or settings.JWT_EXPIRES_MIN)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.JWT_SECRET, algorithm=settings.JWT_ALG)


def decode_token(token: str) -> dict:
    return jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALG])
