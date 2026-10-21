# Operación completa de categorías. El router pide. Este archivo confirma o revierte.
#
# La clase no tiene este archivo: el router crea CategoryRepository, hace commit
# y lanza el 400 y el 404. En posts, tags y auth eso vive en el servicio.
# El código de la clase quedó comentado en router.py.
#
# sqlalchemy.exc.IntegrityError → nombre o slug repetidos (las columnas son unique).
# sqlalchemy.orm.Session        → la sesión que abrió get_db. Este archivo no la cierra.
# fastapi.HTTPException         → 400 si el slug ya está, 404 si el id no existe.

from app.models.category import CategoryORM
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from fastapi import HTTPException

from .repository import CategoryRepository
from .schemas import CategoryCreate, CategoryPublic, CategoryUpdate


class CategoryService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = CategoryRepository(db)

    def list_categories(self, skip: int, limit: int) -> list[CategoryORM]:
        return list(self.repository.list_many(skip=skip, limit=limit))

    def create_category(self, data: CategoryCreate) -> CategoryPublic:
        # La clase mira el slug antes de insertar. El nombre unique no lo mira:
        # si el nombre ya existe, la base lanza IntegrityError y la clase no lo atrapa.
        if self.repository.get_by_slug(data.slug):
            raise HTTPException(status_code=400, detail="Slug en uso")

        try:
            category = self.repository.create(name=data.name, slug=data.slug)
            self.db.commit()
            self.db.refresh(category)
            return CategoryPublic.model_validate(category)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Nombre o slug ya en uso")

    def get_category(self, category_id: int) -> CategoryORM:
        category = self.repository.get(category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Categoría no encontrada")
        return category

    def update_category(self, category_id: int, data: CategoryUpdate) -> CategoryPublic:
        category = self.get_category(category_id)
        try:
            # exclude_unset=True: solo cambian los campos que vinieron en el JSON.
            updated = self.repository.update(category, data.model_dump(exclude_unset=True))
            self.db.commit()
            self.db.refresh(updated)
            return CategoryPublic.model_validate(updated)
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Nombre o slug ya en uso")

    def delete_category(self, category_id: int) -> None:
        category = self.get_category(category_id)
        self.repository.delete(category)
        self.db.commit()
