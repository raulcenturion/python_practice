# Rutas de etiquetas. Sección 11.
# GET    /tags              lista, con página, orden y búsqueda. Sin token.
# POST   /tags              crea. Pide token.
# PUT    /tags/{tag_id}     renombra. Pide token.
# DELETE /tags/{tag_id}    borra. Pide token.
# GET    /tags/popular/top  el tag usado en más posts. Pide token.
#
# La clase llama al repository desde acá y hace db.commit() en la ruta.
# Ese commit se mudó a service.py, igual que en posts. Abajo queda comentado
# cómo lo escribía la clase.
#
# fastapi.APIRouter     → el grupo de rutas. prefix="/tags" arma la URL.
# fastapi.Depends        → abre la sesión (get_db) y exige el token (get_current_user).
# fastapi.HTTPException  → la clase lo lanza en la ruta. Ahora lo lanza el servicio.
# fastapi.Query          → lee ?page= &per_page= &order_by= &direction= &search=
# fastapi.status         → 201 y 204 con nombre, en vez del número suelto.
# sqlalchemy.orm.Session → el tipo de la sesión. La abre core/db.py.
# get_current_user       → sección 8. Hoy devuelve el dict del token, no la fila User.
#   Alcanza para saber que hay sesión. El rol (require_editor) todavía no se usa.
#
# La clase importa `from operator import ge` y `from app.api.v1.tags import repository`.
# operator.ge es "mayor o igual" de Python. El ge=1 de Query es un argumento de FastAPI,
# no esa función. El módulo repository tampoco se usa: se usa la clase TagRepository.
# Esos dos imports no van.

from app.core.db import get_db
from app.core.security import get_current_user
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, Query, status

from .schemas import TagCreate, TagPublic, TagUpdate, TagWithCount
from .service import TagService

router = APIRouter(prefix="/tags", tags=["tags"])


# response_model=dict es lo que pone la clase. El cuerpo real trae
# total, pages, page, per_page e items (lista de TagPublic).
@router.get("", response_model=dict)
def list_tags(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    # pattern es una regex. Si order_by no es id ni name, FastAPI responde 422.
    order_by: str = Query("id", pattern="^(id|name)$"),
    direction: str = Query("asc", pattern="^(asc|desc)$"),
    search: str | None = Query(None),
    db: Session = Depends(get_db),
):
    # La clase:
    # repository = TagRepository(db)
    # return repository.list_tags(...)
    return TagService(db).list_tags(
        page=page,
        per_page=per_page,
        order_by=order_by,
        direction=direction,
        search=search,
    )


# response_description es el texto de /docs para el 201. La clase dice
# "Post creado (OK)" en una ruta de tags. El status 201 es el que importa.
@router.post(
    "",
    response_model=TagPublic,
    response_description="Post creado (OK)",
    status_code=status.HTTP_201_CREATED,
)
def create_tag(
    tag: TagCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    # user no se lee. Depends(get_current_user) está para rechazar la petición
    # si no hay token. La clase hace lo mismo.
    # La clase, adentro de la ruta:
    # repository = TagRepository(db)
    # try:
    #     tag_created = repository.create_tag(name=tag.name)
    #     db.commit()
    #     db.refresh(tag_created)
    #     return tag_created
    # except SQLAlchemyError:
    #     db.rollback()
    #     raise HTTPException(status_code=500, detail="Error al crear el tag")
    return TagService(db).create_tag(tag)


@router.put("/{tag_id}", response_model=TagPublic)
def update_tag(
    tag_id: int,
    payload: TagUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    # La clase:
    # tag = TagRepository(db).update(tag_id, name=payload.name)
    # if not tag: raise HTTPException(404, "Tag no encontrado")
    # db.commit()
    # return TagPublic.model_validate(tag)
    return TagService(db).update_tag(tag_id, payload)


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_tag(
    tag_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    # 204 no lleva cuerpo. Por eso la función no devuelve el tag.
    # La clase devuelve None después del commit. El servicio hace el commit
    # y esta función termina sin return: FastAPI manda el 204 vacío.
    # La clase:
    # delete = TagRepository(db).delete(tag_id)
    # if not delete: raise HTTPException(404, "Tag no encontrado")
    # db.commit()
    # return None
    TagService(db).delete_tag(tag_id)


# Va después de /{tag_id} en la clase. Como tag_id es int, "popular" no entra
# en esa ruta. Si algún día tag_id fuera str, /tags/popular chocaría con /{tag_id}
# y esta ruta tendría que declararse antes.
@router.get("/popular/top", response_model=TagWithCount)
def get_most_popular_tag(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    # La clase no pone response_model y devuelve el dict de most_popular().
    # TagWithCount ya estaba en schemas.py y describe id, name y uses.
    # La clase:
    # row = TagRepository(db).most_popular()
    # if not row: raise HTTPException(404, "No hay tags en uso")
    # return row
    return TagService(db).most_popular()
