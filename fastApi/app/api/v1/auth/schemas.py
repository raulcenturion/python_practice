# JSON del login y del usuario.
# Sección 8: Token (solo el access_token) y UserPublic con email y username.
#   Eso era el dict de FAKE_USERS. Quedó comentado abajo.
# Sección 11 y 12: UserPublic es la fila de users (id, email, nombre, rol, activo).
#   /login devuelve TokenResponse: el token más ese usuario.
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

# --- Sección 8. Respuesta del login contra FAKE_USERS. Ya no la devuelve ninguna ruta. ---
# class Token(BaseModel):
#     access_token: str
#     token_type: str = "bearer"
#
# class UserPublic(BaseModel):
#     email: str
#     username: str
#     model_config = ConfigDict(from_attributes=True)

Role = Literal["user", "editor", "admin"]


class UserBase(BaseModel):
    email: EmailStr
    # La clase escribe Optional[str]. str | None es lo mismo.
    full_name: str | None = None
    model_config = ConfigDict(from_attributes=True)


# Lo que devuelve /register, /me y el cambio de rol. Sin la clave.
# En la integración de la sección 11 se llamó UserRecord, para no pisar el
# UserPublic de email y username. La clase lo llama UserPublic. Ahora ese es el nombre activo.
class UserPublic(UserBase):
    id: int
    role: Role
    is_active: bool


# Body del POST /register. La ruta llega en la sección 12.
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)
    full_name: str | None = None


# Body JSON de POST /login. /token no usa esta clase: Swagger manda un formulario.
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Lo que devuelve POST /login: el token y la fila, sin la clave.
# token_type "bearer" le dice al cliente que lo mande como: Bearer <access_token>.
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserPublic


# Body del PUT /role/{id}. role solo puede ser user, editor o admin.
class RoleUpdate(BaseModel):
    role: Role


# Lo que la sección 8 guardaba dentro del token: el email en sub y el username.
# La sección 12 guarda solo sub, y ese sub es el id de users, no el email.
# username ya no viaja. Se deja en el modelo porque la clase no lo sacó de TokenData.
class TokenData(BaseModel):
    sub: str
    username: str
