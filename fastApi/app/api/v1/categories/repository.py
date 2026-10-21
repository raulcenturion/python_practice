# SQL de las categorías. No hace commit y no arma el 404.
# Eso está en service.py.
#
# from __future__ import annotations → biblioteca estándar. Las anotaciones
#   (CategoryORM | None) no se evalúan al importar el archivo.
# collections.abc.Sequence → el tipo de "una secuencia de filas". No es una lista concreta.
#   La clase también importa Iterable y IterableABC. Ninguno se usa. No van.
# sqlalchemy.select / func → arman el SELECT y el COUNT.
# sqlalchemy.orm.Session   → la sesión que abrió get_db.
# sqlalchemy.exc.IntegrityError → la clase lo importa y no lo usa. El choque de
#   nombre o slug lo traduce el servicio, no este archivo.
# CategoryORM → la tabla categories.

from __future__ import annotations

from collections.abc import Sequence

from app.models.category import CategoryORM
from sqlalchemy import func, select
from sqlalchemy.orm import Session


class CategoryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    # skip salta filas. limit corta. offset(0).limit(50) es la primera página suelta,
    # sin contar el total. Lo usa GET /categories.
    def list_many(self, *, skip: int = 0, limit: int = 50) -> Sequence[CategoryORM]:
        query = select(CategoryORM).offset(skip).limit(limit)
        return self.db.execute(query).scalars().all()

    # La rama de la clase deja esta función en pass. El router no la llama:
    # lista con list_many. Queda armada para devolver el total y la página,
    # el mismo par (total, items) que usa el listado de posts.
    # def list_with_total(...) -> tuple[int, list[CategoryORM]]:
    #     pass
    def list_with_total(
        self,
        *,
        page: int = 1,
        per_page: int = 50,
    ) -> tuple[int, list[CategoryORM]]:
        page = max(1, page)
        per_page = max(1, per_page)
        total = self.db.scalar(select(func.count()).select_from(CategoryORM)) or 0
        items = self.db.execute(
            select(CategoryORM)
            .order_by(CategoryORM.id.asc())
            .offset((page - 1) * per_page)
            .limit(per_page)
        ).scalars().all()
        return total, list(items)

    # db.get busca por clave primaria. None si el id no existe.
    def get(self, category_id: int) -> CategoryORM | None:
        return self.db.get(CategoryORM, category_id)

    # scalars().first() es la primera fila o None. Si hubiera dos, no falla:
    # el unique de slug hace que no pueda haber dos.
    def get_by_slug(self, slug: str) -> CategoryORM | None:
        query = select(CategoryORM).where(CategoryORM.slug == slug)
        return self.db.execute(query).scalars().first()

    # Deja la fila en la sesión. El commit lo hace el servicio.
    def create(self, *, name: str, slug: str) -> CategoryORM:
        category = CategoryORM(name=name, slug=slug)
        self.db.add(category)
        # flush manda el INSERT y consigue el id, sin cerrar la transacción.
        self.db.flush()
        return category

    # updates es un dict, normalmente el model_dump(exclude_unset=True) del PUT.
    # Solo llegan las claves que el cliente mandó.
    # La clase comenta allowed_items = {"name", "slug"} y no filtra: setattr
    # escribe cualquier clave del dict. CategoryUpdate solo tiene name y slug,
    # así que el dict no trae otra cosa.
    def update(self, category: CategoryORM, updates: dict) -> CategoryORM:
        # allowed_items = {"name", "slug"}
        for key, value in updates.items():
            setattr(category, key, value)

        self.db.add(category)
        self.db.flush()
        return category

    # Marca la fila para DELETE. Hasta el commit del servicio no se va de la base.
    def delete(self, category: CategoryORM) -> None:
        self.db.delete(category)
