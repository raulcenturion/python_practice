# Tabla tags. Un tag está en muchos posts y un post tiene muchos tags.
#
# El archivo de la clase a veces se nombra tags.py, pero models/__init__.py
# importa `from .tag import TagORM`. El nombre que funciona es tag.py.

from __future__ import annotations

from typing import TYPE_CHECKING

from app.core.db import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Misma idea que en author.py: no importamos post.py al correr la app.
# TYPE_CHECKING (typing) es True solo para el chequeo de tipos.
# Así se corta el círculo tag → post → tag.
if TYPE_CHECKING:
    from .post import PostORM


class TagORM(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, index=True)

    # secondary="post_tags" es el NOMBRE de la tabla intermedia, en texto.
    # En post.py la misma tabla es el objeto post_tags.
    # El texto evita importar post.py acá (otro círculo). SQLAlchemy resuelve
    # el nombre cuando las tablas ya están creadas.
    # lazy="selectin": al leer los posts de un tag, hace un SELECT ... IN (...).
    posts: Mapped[list[PostORM]] = relationship(
        secondary="post_tags",
        back_populates="tags",
        lazy="selectin",
    )
