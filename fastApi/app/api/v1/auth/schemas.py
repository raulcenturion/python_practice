# JSON del login y del usuario autenticado. No son tablas: los usuarios de esta
# clase viven en un dict dentro de router.py (FAKE_USERS), no en la base.
#
# pydantic.BaseModel  → la forma del JSON.
# ConfigDict          → from_attributes, por si más adelante el usuario sale de un ORM.

from pydantic import BaseModel, ConfigDict


# Lo que devuelve POST /api/v1/auth/login.
# token_type "bearer" le dice al cliente que lo mande como: Bearer <access_token>.
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Lo que va dentro del token, después de decodificarlo.
# sub es el email. username es el nombre corto. Esta clase documenta esa forma;
# get_current_user hoy devuelve un dict con las mismas claves.
class TokenData(BaseModel):
    sub: str
    username: str


# Lo que devuelve GET /api/v1/auth/me. Sin la clave.
class UserPublic(BaseModel):
    email: str
    username: str
    model_config = ConfigDict(from_attributes=True)
