# Tabla users. Sección 11 define la fila. Sección 12: el login la lee.
# FAKE_USERS quedó comentado en api/v1/auth/router.py.
# hashed_password lo llena hash_password (pwdlib). El rol arranca en "user".
#
# datetime              → biblioteca estándar. La fecha de alta.
# typing.Literal        → limita role a tres textos. No es una tabla.
# app.core.db.Base      → la clase madre de SQLAlchemy. Sin esto no hay tabla.
# sqlalchemy.orm        → Mapped y mapped_column declaran columnas.
# sqlalchemy.Boolean    → verdadero o falso (is_active).
# sqlalchemy.DateTime   → fecha y hora.
# sqlalchemy.Enum       → la columna solo acepta user, editor o admin.
# sqlalchemy.String     → texto con largo máximo.

from datetime import datetime
from typing import Literal

from app.core.db import Base
from sqlalchemy import Boolean, DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column

# El mismo Literal está en api/v1/auth/schemas.py (el JSON).
# Acá describe la columna. Allá describe el body. No se importan entre sí.
Role = Literal["user", "editor", "admin"]


# Las otras tablas se llaman AuthorORM, PostORM, TagORM.
# La clase a esta la llama User, sin el sufijo ORM.
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    # unique: no puede haber dos filas con el mismo email.
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    # Nunca el texto de la clave. Lo llena hash_password (pwdlib) en security.py.
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    # La clase declara Mapped[str] sin nullable, así que el INSERT exigiría el nombre.
    # UserCreate (schemas) lo deja opcional. nullable=True acepta las dos cosas.
    full_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    # name="role_enum" es el nombre del tipo en Postgres. En SQLite queda como texto.
    role: Mapped[Role] = mapped_column(
        Enum("user", "editor", "admin", name="role_enum"),
        default="user",
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    # utcnow está deprecado. La clase lo usa igual que created_at de los posts.
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
