# Sección 11. Corta una consulta en páginas.
# Lo usa TagRepository.list_tags. Los posts ya paginan dentro de su repository.
#
# math.ceil        → biblioteca estándar. Redondea hacia arriba la cantidad de páginas.
# typing           → Any, Optional y Dict son de la biblioteca estándar.
#   Optional[str] hoy se escribe str | None. Dict[str, Any] se escribe dict[str, Any].
# sqlalchemy       → func.count arma el COUNT. select arma el SQL. Session lo ejecuta.

from math import ceil
from typing import Any

from sqlalchemy import func, select
from sqlalchemy.orm import Session

# Tope si alguien llama esta función sin el Query(le=100) del router.
DEFAULT_PER_PAGE = 10
MAX_PER_PAGE = 100


# page menor a 1 pasa a 1. per_page fuera de 1..100 se recorta.
def sanitize_pagination(page: int = 1, per_page: int = DEFAULT_PER_PAGE):
    page = max(1, int(page or 1))
    per_page = min(MAX_PER_PAGE, max(1, int(per_page or DEFAULT_PER_PAGE)))
    return page, per_page


def paginate_query(
    db: Session,
    model,
    base_query=None,
    page: int = 1,
    per_page: int = DEFAULT_PER_PAGE,
    order_by: str | None = None,
    direction: str = "asc",
    allowed_order: dict[str, Any] | None = None,
):
    page, per_page = sanitize_pagination(page, per_page)
    # Sin consulta propia, se listan todas las filas del modelo.
    query = base_query if base_query is not None else select(model)

    # La clase cuenta la tabla entera, sin el filtro de search:
    # total = db.scalar(select(func.count()).select_from(model)) or 0
    # Con ?search=py el total diría "todos los tags", no "los que coinciden".
    # select_from(query.subquery()) cuenta la consulta que ya tiene el WHERE.
    total = db.scalar(select(func.count()).select_from(query.subquery())) or 0

    if total == 0:
        return {
            "total": 0,
            "pages": 0,
            "page": page,
            "per_page": per_page,
            "items": [],
        }

    # allowed_order es un dict nombre → columna. Si el nombre no está, cae en "id".
    # El router ya limita order_by a id o name. Esto es la segunda barrera.
    if allowed_order and order_by:
        col = allowed_order.get(order_by, allowed_order.get("id"))
        query = query.order_by(col.desc() if direction == "desc" else col.asc())

    # offset salta las páginas anteriores. limit deja solo per_page filas.
    items = db.execute(query.offset((page - 1) * per_page).limit(per_page)).scalars().all()

    return {
        "total": total,
        "pages": ceil(total / per_page),
        "page": page,
        "per_page": per_page,
        "items": items,
    }
