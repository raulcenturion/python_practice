# Rutas HTTP de los posts. Esta capa solo recibe la petición y llama al servicio.
#
# El JSON se valida con schemas.py (FastAPI lo hace antes de entrar a la función).
# La operación (commit, 404, 409, páginas) está en service.py.
# El SQL está en repository.py. El router ya no lo llama.
#
# fastapi
#   APIRouter  → un grupo de rutas. main.py lo engancha con include_router.
#   Query      → parámetros de la URL (?search=hola&page=1).
#   Path       → el id que va en el camino (/posts/3).
#   Depends    → llama a get_db y le pasa la sesión a la función.
#   status     → constantes de códigos HTTP (201, 204). Esos códigos son de la ruta,
#     por eso se quedan en el decorador y no se mudaron al servicio.
# sqlalchemy.orm.Session → el tipo de la sesión. La clase vive en SQLAlchemy.
# typing.Literal         → "id" o "title", "asc" o "desc".
#
# Estos imports se usaban cuando el router hacía el trabajo del servicio.
# Quedaron comentados: la lógica se mudó a service.py.
#   from math import ceil
#       armaba total_pages. Ahora lo hace PostService.list_posts.
#   from sqlalchemy.exc import IntegrityError, SQLAlchemyError
#       el try/except de crear, actualizar y borrar se mudó a service.py.
#   HTTPException
#       los 404, 409 y 500 los lanza el servicio. El router ya no corta el request.
#   from .repository import PostRepository
#       el router ya no instancia el repositorio. Lo instancia PostService.

from typing import Annotated, Literal

from app.core.db import get_db
from app.core.security import get_current_user, oauth2_scheme
from app.services.file_storage import save_uploaded_image
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, File, Path, Query, UploadFile, status

from .schemas import PaginatedPost, PostCreate, PostPublic, PostSummary, PostUpdate
from .service import PostService

# prefix se pega delante de cada ruta de este archivo.
# "" queda en /posts. "/{post_id}" queda en /posts/3.
# tags=["posts"] agrupa estas rutas en la documentación (/docs).
router = APIRouter(prefix="/posts", tags=["posts"])


# --- Sección 9: ejemplo de sync vs async. No está activo. ---
# La clase lo dejó comentado. Sirve para ver la diferencia, no es parte del blog.
# Para probarlo hay que descomentar UNA de las dos rutas, reiniciar el servidor
# y correr fastapi/request_test.py (también comentado).
#
# time        → biblioteca estándar. time.sleep(8) frena el hilo 8 segundos.
# asyncio     → biblioteca estándar. asyncio.sleep(8) es una espera que se puede await.
# threading   → biblioteca estándar. current_thread().name dice en qué hilo corre.
#
# def sync_endpoint + time.sleep:
#   FastAPI corre las funciones def en un hilo del pool.
#   Mientras ese hilo duerme, no puede atender otra cosa. Muchos requests juntos
#   ocupan un hilo cada uno.
#
# async def async_endpoint + await asyncio.sleep:
#   El await suelta el turno. El mismo hilo del event loop atiende otros requests
#   durante esos 8 segundos. Por eso varios /async juntos tardan ~8 s en total,
#   no 8 s por cada uno.
#
# La clase escribió "theread" y "termino". Son typos de thread y terminó.
# El script de prueba manda ?t=3, ?t=5.5, etc. Estas rutas no leen t: siempre
# esperan 8 segundos. El parámetro t del script no cambia la espera.
#
# @router.get("/sync")
# def sync_endpoint():
#     print("SYNC theread: ", threading.current_thread().name)
#     time.sleep(8)
#     return {"message": "Función síncrona termino"}
#
# @router.get("/async")
# async def async_endpoint():
#     print("ASYNC theread: ", threading.current_thread().name)
#     await asyncio.sleep(8)
#     return {"message": "Función asíncrona termino"}


# Lista paginada. response_model obliga a la respuesta a tener la forma de PaginatedPost.
@router.get("", response_model=PaginatedPost)
def list_posts(
    # deprecated=True: Swagger lo marca viejo. Sigue funcionando.
    text: str | None = Query(
        default=None,
        deprecated=True,
        description="Parámetro obsoleto, usa 'query o search' en su lugar.",
    ),
    query: str | None = Query(
        default=None,
        description="Texto para buscar por título",
        alias="search",  # el cliente escribe ?search=fastapi
        min_length=3,
        max_length=50,
        # Otra cosa que no sea letra, número, espacio, acento o guion → 422.
        pattern=r"^[\w\sáéíóúÁÉÍÓÚüÜ-]+$",
    ),
    per_page: int = Query(10, ge=1, le=50, description="Número de resultados (1-50)"),
    page: int = Query(1, ge=1, description="Número de página (>=1)"),
    order_by: Literal["id", "title"] = Query("id", description="Campo de orden"),
    direction: Literal["asc", "desc"] = Query("asc", description="Dirección de orden"),
    # Depends (FastAPI) ejecuta get_db, que abre y cierra la Session (SQLAlchemy).
    # Abrir la sesión se queda en la ruta: es parte del request, no de la operación.
    db: Session = Depends(get_db),
):
    # Si mandan search, se usa. Si no, cae al parámetro viejo text.
    # Se queda acá porque es elegir cuál parámetro de la URL vale.
    query = query or text

    # --- Antes el router buscaba y armaba la página. Se mudó a service.py. ---
    # Por qué: contar páginas y armar PaginatedPost no es la ruta HTTP.
    # repository = PostRepository(db)
    # total, items = repository.search(query, order_by, direction, page, per_page)
    # total_pages = ceil(total / per_page) if total > 0 else 0
    # current_page = 1 if total_pages == 0 else min(page, total_pages)
    # has_prev = current_page > 1
    # has_next = current_page < total_pages if total_pages > 0 else False
    # return PaginatedPost(page=current_page, per_page=per_page, total=total, ...)
    return PostService(db).list_posts(query, order_by, direction, page, per_page)


# Va ANTES de /{post_id}. Si estuviera después, "by-tags" se leería como un id.
@router.get("/by-tags", response_model=list[PostPublic])
def filter_by_tags(
    tags: list[str] = Query(
        ...,
        min_length=1,
        description="Una o más etiquetas. Ejemplo: ?tags=python&tags=fastapi",
    ),
    db: Session = Depends(get_db),
):
    # --- Antes llamaba al repository directo. Se mudó a service.py. ---
    # Por qué: el router no tiene que conocer PostRepository.
    # repository = PostRepository(db)
    # return repository.by_tags(tags)
    return PostService(db).filter_by_tags(tags)


# Sección 8. La clase pegó esta ruta al final del archivo, después de /{post_id}.
# Va antes: si no, "secure" compite con el id. oauth2_scheme solo exige que el
# header traiga un token; no mira si venció ni de quién es. Para eso está get_current_user.
@router.get("/secure")
def secure_endpoint(token: str = Depends(oauth2_scheme)):
    return {"message": "Acceso con token", "token_recibido": token}


# La clase anota Union[PostPublic, PostSummary]. A | B es lo mismo.
# Escribieron example=1. En Pydantic reciente el argumento es examples=[1].
# El texto de la clase dice "mayor a 1", pero ge=1 significa mayor o igual a 1.
@router.get(
    "/{post_id}",
    response_model=PostPublic | PostSummary,
    response_description="Post encontrado",
)
def get_post(
    post_id: int = Path(
        ...,
        ge=1,
        title="ID del post",
        description="Identificador entero del post. Debe ser mayor o igual a 1",
        examples=[1],
    ),
    include_content: bool = Query(default=True, description="Incluir o no el contenido"),
    db: Session = Depends(get_db),
):
    # --- Antes el router buscaba, lanzaba el 404 y elegía el schema. ---
    # Se mudó a PostService.get_post, en service.py.
    # Por qué: "no existe" y qué campos devolver son la operación, no la ruta.
    # repository = PostRepository(db)
    # post = repository.get(post_id)
    # if not post:
    #     raise HTTPException(status_code=404, detail="Post no encontrado!!")
    # if include_content:
    #     return PostPublic.model_validate(post, from_attributes=True)
    # return PostSummary.model_validate(post, from_attributes=True)
    return PostService(db).get_post(post_id, include_content)


# status.HTTP_201_CREATED es el 201: el recurso se creó.
# El código se queda en el decorador. El commit está en el servicio.
@router.post(
    "",
    response_model=PostPublic,
    response_description="Post creado (OK)",
    status_code=status.HTTP_201_CREATED,
)
def create_post(
    # Antes el cuerpo era JSON: post: PostCreate.
    # Sección 10. Depends(as_form) lee title, content y tags del formulario.
    # Así el mismo request puede traer la imagen. Un JSON ya no arma el post.
    post: Annotated[PostCreate, Depends(PostCreate.as_form)],
    # File(None): la imagen es opcional. File(...) la haría obligatoria.
    image: UploadFile | None = File(None),
    db: Session = Depends(get_db),
    # Sección 8. Sin token válido FastAPI responde 401 y no entra a la función.
    # user es el dict de get_current_user: email y username. El autor ya no viene en el JSON.
    user=Depends(get_current_user),
):
    # --- Antes el router hacía el insert, el commit y traducía los errores. ---
    # Se mudó a PostService.create_post, en service.py.
    # Por qué: commit, rollback, 409 y 500 son la operación de guardar, no la ruta.
    # repository = PostRepository(db)
    # try:
    #     post = repository.create_post(
    #         title=post.title,
    #         content=post.content,
    #         author=(post.author.model_dump() if post.author else None),
    #         tags=[tag.model_dump() for tag in post.tags],
    #     )
    #     db.commit()
    #     db.refresh(post)
    #     return post
    # except IntegrityError:
    #     db.rollback()
    #     raise HTTPException(status_code=409, detail="El título ya existe, prueba con otro")
    # except SQLAlchemyError:
    #     db.rollback()
    #     raise HTTPException(status_code=500, detail="Error al crear el post")
    # Antes: return PostService(db).create_post(post)
    # El autor salía del body. Ahora se lo pasamos desde el token.
    # Sección 10. Si vino una imagen, se guarda antes de crear el post.
    # La clase hace este guardado en la ruta y después llama al repository.
    # Acá la URL entra al servicio, que es quien llama al repository.
    # Si el archivo se guardó y el insert falla, el archivo queda en app/media.
    saved = None
    if image is not None:
        saved = save_uploaded_image(image)
    image_url = saved["url"] if saved else None
    return PostService(db).create_post(post, user, image_url)


# response_model_exclude_none=True: la respuesta no muestra claves en None.
# Sigue acá porque es forma de la respuesta HTTP, no de la base.
@router.put(
    "/{post_id}",
    response_model=PostPublic,
    response_description="Post actualizado",
    response_model_exclude_none=True,
)
def update_post(
    post_id: int,
    data: PostUpdate,
    db: Session = Depends(get_db),
    # El parámetro no se usa en el cuerpo. Está para que la ruta exija token.
    # La clase hace lo mismo: protege el PUT y todavía no mira quién es el dueño del post.
    user=Depends(get_current_user),
):
    # --- Antes el router buscaba, lanzaba el 404 y hacía el commit. ---
    # Se mudó a PostService.update_post, en service.py.
    # repository = PostRepository(db)
    # post = repository.get(post_id)
    # if not post:
    #     raise HTTPException(status_code=404, detail="Post no encontrado")
    # try:
    #     updates = data.model_dump(exclude_unset=True)
    #     post = repository.update_post(post, updates)
    #     db.commit()
    #     db.refresh(post)
    #     return post
    # except SQLAlchemyError:
    #     db.rollback()
    #     raise HTTPException(status_code=500, detail="Error al actualizar el post")
    return PostService(db).update_post(post_id, data)


# 204: salió bien y no hay cuerpo. La clase usa status.HTTP_204_NO_CONTENT.
# El 204 se queda en el decorador. El delete y el commit están en el servicio.
@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    # Igual que en el PUT: user obliga el token. Borrar sigue sin chequear el dueño.
    user=Depends(get_current_user),
):
    # --- Antes el router buscaba, lanzaba el 404 y confirmaba el DELETE. ---
    # Se mudó a PostService.delete_post, en service.py.
    # repository = PostRepository(db)
    # post = repository.get(post_id)
    # if not post:
    #     raise HTTPException(status_code=404, detail="Post no encontrado")
    # try:
    #     repository.delete_post(post)
    #     db.commit()
    # except SQLAlchemyError:
    #     db.rollback()
    #     raise HTTPException(status_code=500, detail="Error al eliminar el post")
    PostService(db).delete_post(post_id)
