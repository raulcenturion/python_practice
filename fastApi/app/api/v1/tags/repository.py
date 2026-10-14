# SQL de las etiquetas. No hace commit y no arma el 404.
# Eso está en service.py. Este archivo deja filas listas.
#
# sqlalchemy.func     → lower, count, ilike. Funciones del motor, no de Python.
# sqlalchemy.select   → arma el SELECT.
# sqlalchemy.orm.Session → la sesión que abrió get_db.
# app.models.post     → PostORM y la tabla intermedia post_tags (post ↔ tag).
# app.models.tag      → TagORM, la tabla tags.
# app.services.pagination → corta el SELECT en páginas.
# TagPublic           → el JSON de cada ítem de la lista. Pydantic, no SQLAlchemy.

from app.models.post import PostORM, post_tags
from app.models.tag import TagORM
from app.services.pagination import paginate_query
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from .schemas import TagPublic


class TagRepository:
    def __init__(self, db: Session):
        self.db = db

    # Un tag por id, o None. scalar_one_or_none (SQLAlchemy) es la fila o None.
    def get(self, tag_id: int) -> TagORM | None:
        tag_find = select(TagORM).where(TagORM.id == tag_id)
        return self.db.execute(tag_find).scalar_one_or_none()

    def list_tags(
        self,
        search: str | None,
        order_by: str = "id",
        direction: str = "asc",
        page: int = 1,
        per_page: int = 10,
    ):
        query = select(TagORM)
        # ilike no distingue mayúsculas. %texto% es "contiene".
        # La clase escribe func.lower(TagORM.name).ilike(...). lower e ilike juntos
        # sobran: ilike ya ignora el caso. Se deja la forma de la clase.
        if search:
            query = query.where(func.lower(TagORM.name).ilike(f"%{search.lower()}%"))

        # Solo estas columnas se pueden usar para ordenar.
        # func.lower(name) ordena "API" junto a "api", no por el código del carácter.
        allowed_order = {
            "id": TagORM.id,
            "name": func.lower(TagORM.name),
        }

        result = paginate_query(
            db=self.db,
            model=TagORM,
            base_query=query,
            page=page,
            per_page=per_page,
            order_by=order_by,
            direction=direction,
            allowed_order=allowed_order,
        )

        # paginate_query devuelve TagORM. El listado responde TagPublic.
        result["items"] = [TagPublic.model_validate(item) for item in result["items"]]
        return result

    # Si ya hay un tag con ese nombre (sin mirar mayúsculas), devuelve ese.
    # Si no, inserta. No hace commit: lo hace el servicio.
    def create_tag(self, name: str):
        normalize = name.strip().lower()

        tag_obj = self.db.execute(
            select(TagORM).where(func.lower(TagORM.name) == normalize)
        ).scalar_one_or_none()

        if tag_obj:
            return tag_obj

        # La clase guarda TagORM(name=name), el texto tal cual llegó.
        # ensure_tag de los posts guarda el nombre ya en minúsculas.
        # En SQLite "Python" y "python" son dos filas distintas (unique distingue caso).
        # Se guarda normalize para que las dos vías hablen de la misma etiqueta.
        tag_obj = TagORM(name=normalize)
        self.db.add(tag_obj)
        # flush manda el INSERT y consigue el id, sin cerrar la transacción.
        self.db.flush()
        return tag_obj

    def update(self, tag_id: int, name: str) -> TagORM | None:
        tag = self.get(tag_id)
        if not tag:
            return None
        # La clase pregunta `if name is not None`. En TagUpdate name es obligatorio,
        # así que esa rama siempre entra. Se deja el mismo recorte a minúsculas.
        if name is not None:
            tag.name = name.strip().lower()

        self.db.add(tag)
        self.db.flush()
        self.db.refresh(tag)
        return tag

    # True si borró. False si el id no existe. El DELETE de SQL lo confirma el servicio.
    def delete(self, tag_id: int) -> bool:
        tag = self.get(tag_id)
        if not tag:
            return False
        self.db.delete(tag)
        return True

    # El tag que aparece en más posts. None si ninguno está usado.
    def most_popular(self) -> dict | None:
        # post_tags.c.tag_id es la columna de la tabla intermedia.
        # .c es "columns": post_tags no es un modelo, es un Table.
        row = (
            self.db.execute(
                select(
                    TagORM.id.label("id"),
                    TagORM.name.label("name"),
                    func.count(PostORM.id).label("uses"),
                )
                .join(post_tags, post_tags.c.tag_id == TagORM.id)
                .join(PostORM, PostORM.id == post_tags.c.post_id)
                .group_by(TagORM.id, TagORM.name)
                .order_by(func.count(PostORM.id).desc(), func.lower(TagORM.name).asc())
                .limit(1)
            )
            .mappings()
            .first()
        )
        # mappings() devuelve una fila tipo dict. dict(row) es un dict común.
        return dict(row) if row else None
