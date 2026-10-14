# Operación completa de tags. El router pide. Este archivo confirma o revierte.
# El SQL está en repository.py.
#
# La clase no tiene este archivo: el router crea TagRepository, hace commit
# y lanza el 404 y el 500. Eso mezcla la ruta HTTP con la transacción.
# En posts esa mezcla se mudó a service.py. Acá se hace lo mismo.
# El código de la clase quedó comentado en router.py, al lado de cada ruta.
#
# sqlalchemy.exc.SQLAlchemyError → cualquier fallo del motor (conexión, SQL, restricción).
# sqlalchemy.orm.Session         → la sesión que abrió get_db. Este archivo no la cierra.
# fastapi.HTTPException          → 404 si no hay fila, 500 si la base falla.

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from fastapi import HTTPException

from .repository import TagRepository
from .schemas import TagCreate, TagPublic, TagUpdate


class TagService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = TagRepository(db)

    def list_tags(
        self,
        search: str | None,
        order_by: str,
        direction: str,
        page: int,
        per_page: int,
    ):
        # Listar no escribe. No hay commit.
        return self.repository.list_tags(
            search=search,
            order_by=order_by,
            direction=direction,
            page=page,
            per_page=per_page,
        )

    def create_tag(self, tag: TagCreate) -> TagPublic:
        try:
            created = self.repository.create_tag(name=tag.name)
            # Si el nombre ya existía, create_tag devuelve esa fila y el commit
            # no inserta otra. La ruta igual responde 201, como la clase.
            self.db.commit()
            self.db.refresh(created)
            return TagPublic.model_validate(created)
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al crear el tag")

    def update_tag(self, tag_id: int, payload: TagUpdate) -> TagPublic:
        tag = self.repository.update(tag_id, name=payload.name)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag no encontrado")
        self.db.commit()
        return TagPublic.model_validate(tag)

    def delete_tag(self, tag_id: int) -> None:
        deleted = self.repository.delete(tag_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Tag no encontrado")
        self.db.commit()

    def most_popular(self) -> dict:
        row = self.repository.most_popular()
        if not row:
            raise HTTPException(status_code=404, detail="No hay tags en uso")
        return row
