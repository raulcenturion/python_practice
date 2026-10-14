# JSON del login y del usuario autenticado.
# Hasta la sección 8 los usuarios viven en FAKE_USERS (router.py), no en la base.
# La sección 11 suma los modelos de la tabla users. /login y /me siguen con
# Token y UserPublic. UserRecord y el resto quedan para cuando el login lea esa tabla.
#
# typing.Literal      → el rol solo puede ser user, editor o admin.
# pydantic.BaseModel  → la forma del JSON.
# ConfigDict          → from_attributes, para armar el JSON desde un ORM.
# EmailStr            → valida que el texto tenga forma de email.
#   pydantic lo apoya en el paquete email-validator.
# Field               → largo de la clave. 72 es el tope que miraba bcrypt.
#   pwdlib con Argon2 no tiene ese tope. Se deja el número de la clase.

from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field


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


# --- Sección 11. Modelos de la tabla users. /login y /me no los usan todavía. ---
#
# La clase reemplaza UserPublic por uno con id, role e is_active, y renombra
# Token a TokenResponse (el token más el usuario). Eso rompe GET /me, que sigue
# devolviendo email y username del token de FAKE_USERS.
# Por eso UserPublic y Token de arriba se quedan. Los de abajo son los de la clase,
# con el nombre UserRecord donde la clase dice UserPublic.

Role = Literal["user", "editor", "admin"]


class UserBase(BaseModel):
    email: EmailStr
    # La clase escribe Optional[str]. str | None es lo mismo.
    full_name: str | None = None
    model_config = ConfigDict(from_attributes=True)


# En la clase esta clase se llama UserPublic.
class UserRecord(UserBase):
    id: int
    role: Role
    is_active: bool


# Body para dar de alta un usuario. La sección 11 no trae la ruta que lo use.
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    full_name: str | None = None


# Body JSON de un login. El login actual no lo usa: lee OAuth2PasswordRequestForm
# (usuario y clave como formulario, no como este JSON).
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Lo que la clase quiere devolver en el login: el token y el usuario de la tabla.
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserRecord


# Body para cambiar el rol. La ruta que lo aplique llega con los roles (sección 12).
class RoleUpdate(BaseModel):
    role: Role
