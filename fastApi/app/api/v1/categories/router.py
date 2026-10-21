# Rutas de categorías. Sección 13.
# GET    /categories              lista. skip y limit cortan, sin token.
# POST   /categories              crea. Sin token en la clase.
# GET    /categories/{id}         una fila.
# PUT    /categories/{id}         cambia name y/o slug.
# DELETE /categories/{id}        borra. 204 sin cuerpo.
#
# La clase llama al repository desde acá y hace db.commit() en la ruta.
# Ese commit se mudó a service.py. Abajo queda comentado cómo lo escribía.
#
# fastapi.APIRouter     → el grupo de rutas. prefix="/categories" arma la URL.
# fastapi.Depends        → abre la sesión con get_db.
# fastapi.HTTPException  → la clase lo lanza en la ruta. Ahora lo lanza el servicio.
# fastapi.status         → 201 y 204 con nombre, en vez del número suelto.
# sqlalchemy.orm.Session → el tipo de la sesión. La abre core/db.py.
#
# La clase importa además:
#   from email.policy import HTTP
#     email.policy es de los mails de la biblioteca estándar. HTTP no es un status.
#     No se usa.
#   from app.api.v1.auth import repository
#     El repositorio de usuarios no entra en estas rutas. No se usa.

from app.core.db import get_db
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, status

from .schemas import CategoryCreate, CategoryPublic, CategoryUpdate
from .service import CategoryService

router = APIRouter(prefix="/categories", tags=["categories"])


# skip y limit son query params porque no están en la URL.
# La clase los anota como int = 0 e int = 50, sin Query. FastAPI igual los lee de ?skip=&limit=
@router.get("", response_model=list[CategoryPublic])
def list_categories(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
):
    # La clase:
    # repository = CategoryRepository(db)
    # return repository.list_many(skip=skip, limit=limit)
    return CategoryService(db).list_categories(skip=skip, limit=limit)


@router.post("", response_model=CategoryPublic, status_code=status.HTTP_201_CREATED)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    # La clase, adentro de la ruta:
    # repository = CategoryRepository(db)
    # if repository.get_by_slug(data.slug):
    #     raise HTTPException(status_code=400, detail="Slug en uso")
    # category = repository.create(name=data.name, slug=data.slug)
    # db.commit()
    # db.refresh(category)
    # return category
    return CategoryService(db).create_category(data)


@router.get("/{category_id}", response_model=CategoryPublic)
def get_category(category_id: int, db: Session = Depends(get_db)):
    # La clase:
    # category = CategoryRepository(db).get(category_id)
    # if not category:
    #     raise HTTPException(status_code=404, detail="Categoría no encontrada")
    # return category
    return CategoryService(db).get_category(category_id)


@router.put("/{category_id}", response_model=CategoryPublic)
def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
):
    # La clase:
    # category = CategoryRepository(db).get(category_id)
    # if not category: raise HTTPException(404, "Categoría no encontrada")
    # updated = repository.update(category, data.model_dump(exclude_unset=True))
    # db.commit()
    # db.refresh(updated)
    # return updated
    return CategoryService(db).update_category(category_id, data)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    # 204 no lleva cuerpo. La clase devuelve None después del commit.
    # La clase:
    # category = CategoryRepository(db).get(category_id)
    # if not category: raise HTTPException(404, "Categoría no encontrada")
    # repository.delete(category)
    # db.commit()
    # return None
    CategoryService(db).delete_category(category_id)
