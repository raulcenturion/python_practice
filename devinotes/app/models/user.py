# Tabla users de Devinote y los modelos de JSON que no se guardan.
#
# sqlmodel.SQLModel → paquete sqlmodel. Heredar de SQLModel da validación
#   de Pydantic. table=True además crea la tabla.
# sqlmodel.Field    → paquete sqlmodel (envuelve al Field de Pydantic y
#   suma primary_key, foreign_key, index, unique).

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    # Sin __tablename__, SQLModel usa el nombre de la clase en minúscula: "user".
    # Las otras tablas apuntan a user.id con foreign_key="user.id".
    # int | None: al insertar, el id lo genera la base y todavía no existe.
    # La clase anota id: int con default=None. El valor es el mismo.
    # Optional[int] es lo mismo que int | None.
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    full_name: str = Field(default="")
    # El texto de la clave no va acá. Lo que se guarda es el hash.
    hashed_password: str


# Sin table=True no hay tabla. Son el body y la respuesta, como los schemas
# de fastapi/. UserCreate trae password. UserRead no: el hash no sale en el JSON.
class UserCreate(SQLModel):
    email: str
    full_name: str = ""
    password: str


class UserRead(SQLModel):
    id: int
    email: str
    full_name: str
    # from_attributes deja armar UserRead desde una fila User.
    # La clase lo escribe igual. En Pydantic 2 es el reemplazo de orm_mode.
    model_config = {"from_attributes": True}
