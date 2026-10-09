# Tabla posts y la tabla intermedia post_tags (posts ↔ tags).
#
# datetime        → biblioteca estándar. La hora de created_at.
# sqlalchemy      → columnas, claves foráneas y la tabla intermedia.
#   Table, Column → para post_tags, que no es una clase propia.
#   ForeignKey    → apunta a posts.id y tags.id.
# app.core.db.Base → la madre DeclarativeBase definida en core/db.py.

from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from app.core.db import Base
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

# PostORM nombra a AuthorORM y a TagORM solo como tipos.
# Esas clases, a su vez, nombran a PostORM. Importarlas de verdad acá
# cierra el círculo (post → author → post).
#
# Cómo se usa TYPE_CHECKING:
#   1. from __future__ import annotations deja las anotaciones sin evaluar.
#   2. if TYPE_CHECKING: el import de abajo NO corre cuando levantás la API.
#   3. Un type checker (Pyright, mypy) sí entra a ese if y entiende los nombres.
#   4. En tiempo de ejecución, "AuthorORM" entre comillas es solo texto.
# La clase importa List dos veces y también Optional. Con annotations alcanza
# con list[...] y AuthorORM | None. Optional[X] es lo mismo que X | None.
if TYPE_CHECKING:
    from .author import AuthorORM
    from .tag import TagORM


# Tabla puente. No es una clase ORM: no hay un TagDePost que consultar.
# ondelete="CASCADE": si se borra el post o el tag, se borra esta fila.
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)


class PostORM(Base):
    __tablename__ = "posts"
    # Dos posts no pueden tener el mismo título. Si pasa, la base lanza IntegrityError.
    __table_args__ = (UniqueConstraint("title", name="unique_post_title"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    # Sección 10. Ruta de la imagen, o NULL si el post no tiene.
    # La clase escribe image_url = mapped_column(...) sin el tipo Mapped.
    # Mapped[str | None] es el mismo estilo que el resto de columnas de este archivo.
    # create_all no agrega columnas a una tabla que ya existe. Si blog.db es viejo,
    # hay que borrar ese archivo para que esta columna se cree.
    image_url: Mapped[str | None] = mapped_column(String(300), nullable=True)
    # La clase usa datetime.utcnow (hora UTC sin zona). El equivalente actual
    # es datetime.now(timezone.utc). Se deja utcnow para coincidir con el módulo.
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # author_id es la columna real. author es el objeto AuthorORM, si hay uno.
    author_id: Mapped[int | None] = mapped_column(ForeignKey("authors.id"))
    author: Mapped[AuthorORM | None] = relationship(back_populates="posts")

    # secondary=post_tags usa el objeto Table de arriba (tag.py usa el nombre en texto).
    # passive_deletes=True: al borrar el post, la base limpia post_tags (ON DELETE CASCADE)
    # y SQLAlchemy no recorre la lista de tags para borrarla a mano.
    tags: Mapped[list[TagORM]] = relationship(
        secondary=post_tags,
        back_populates="posts",
        lazy="selectin",
        passive_deletes=True,
    )
