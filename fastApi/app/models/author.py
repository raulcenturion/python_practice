# Tabla authors. Un autor tiene muchos posts.
#
# from __future__ import annotations  →  biblioteca estándar.
#   Guarda las anotaciones (List["PostORM"], etc.) como texto y no las evalúa ahora.
# typing.TYPE_CHECKING               →  biblioteca estándar.
#   Vale True solo para mypy / Pyright. Cuando corre la app, vale False.
# sqlalchemy                         →  columnas y el vínculo con PostORM.

from __future__ import annotations

from typing import TYPE_CHECKING

from app.core.db import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# AuthorORM menciona a PostORM, y PostORM menciona a AuthorORM.
# Si este archivo importara post.py de verdad, y post.py importara author.py,
# Python entra en un círculo y falla con ImportError.
#
# if TYPE_CHECKING es False al ejecutar la app, así que esa línea NO corre.
# El editor igual la ve y sabe qué es PostORM.
# Las comillas de List["PostORM"] hacen el resto: el nombre no se busca ahora,
# se busca más tarde, cuando las dos clases ya existen.
# from __future__ import annotations refuerza eso: todas las anotaciones quedan en texto.
if TYPE_CHECKING:
    from .post import PostORM


class AuthorORM(Base):
    __tablename__ = "authors"  # nombre de la tabla en la base

    # Mapped + mapped_column es el estilo de SQLAlchemy 2. Integer/String son tipos de columna.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    # unique=True: dos autores no pueden compartir el email. index=True acelera la búsqueda.
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)

    # relationship no es una columna. Es el acceso autor.posts → lista de PostORM.
    # back_populates="author" apunta al atributo del otro lado (PostORM.author).
    # En la clase el tipo es List["PostORM"]. list["PostORM"] es el equivalente actual.
    posts: Mapped[list[PostORM]] = relationship(back_populates="author")
