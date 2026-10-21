# Arma el slug de un post a partir del título. Sección 14.
#
# slugify → paquete python-slugify (pip install python-slugify).
#   El import es `from slugify import slugify`, no el nombre del paquete.
#   Pasa "Mi primer post" a "mi-primer-post": minúsculas, sin acentos, guiones.
# sqlalchemy.select → busca slugs que ya existen para no repetir el unique.
# sqlalchemy.orm.Session → la sesión que ya abrió el repository.
# PostORM.slug → la columna nueva. Es unique.

from app.models.post import PostORM
from slugify import slugify as _slugify
from sqlalchemy import select
from sqlalchemy.orm import Session


def slugify_base(text: str) -> str:
    # lowercase=True fuerza minúsculas. separator='-' pone guiones entre palabras.
    # Si el título no deja ningún carácter (por ejemplo "---"), se usa "post"
    # para no guardar un slug vacío en una columna unique.
    slug = _slugify(text, lowercase=True, separator="-")
    return slug or "post"


def ensure_unique_slug(db: Session, base_text: str) -> str:
    base = slugify_base(base_text)
    # like "fastapi%" trae "fastapi" y también "fastapi-2".
    # La clase no ancla el patrón al final, así que "fastapi" también
    # coincide con "fastapi-extra". Alcanza para no chocar el unique.
    existing = db.execute(select(PostORM.slug).where(PostORM.slug.like(f"{base}%"))).scalars().all()

    if base not in existing:
        return base

    # El primero se queda como "mi-post". El siguiente es "mi-post-2", luego -3, ...
    i = 2
    candidate = f"{base}-{i}"
    while candidate in existing:
        i += 1
        candidate = f"{base}-{i}"
    return candidate
