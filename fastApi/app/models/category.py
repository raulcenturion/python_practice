# Tabla categories. Sección 13. Un post puede estar en una categoría.
#
# sqlalchemy.Integer / String → el tipo de la columna.
# sqlalchemy.orm.Mapped       → el tipo Python de esa columna.
# mapped_column               → la declara en la tabla.
# relationship                → el vínculo con PostORM (un category, muchos posts).
# app.core.db.Base            → la clase madre. Sin esto no hay tabla.

from __future__ import annotations

from typing import TYPE_CHECKING

from app.core.db import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# La clase no importa PostORM: nombra la relación con el texto "PostORM".
# TYPE_CHECKING es para el chequeo de tipos. Al correr la app este import no se ejecuta
# y no se arma el círculo category → post → category.
if TYPE_CHECKING:
    from .post import PostORM


class CategoryORM(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    # unique: no hay dos categorías con el mismo nombre ni el mismo slug.
    name: Mapped[str] = mapped_column(String(60), unique=True, index=True)
    # slug es el texto corto de la URL, por ejemplo "backend". Lo manda el cliente.
    # La clase no lo genera a partir del nombre.
    slug: Mapped[str] = mapped_column(String(60), unique=True, index=True)

    # cascade="all, delete": si se borra la categoría desde la sesión, SQLAlchemy
    # también borra sus posts.
    # En post.py la clave dice ondelete="SET NULL": la base dejaría el post
    # y pondría category_id en NULL. Son dos reglas distintas. Se dejan las de la clase.
    # passive_deletes=True: no recorre los posts en Python; deja que la base aplique la clave.
    posts: Mapped[list[PostORM]] = relationship(
        "PostORM",
        back_populates="category",
        cascade="all, delete",
        passive_deletes=True,
    )
