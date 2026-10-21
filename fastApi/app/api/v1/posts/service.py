# Capa de servicio. El router le pide la operación. Este archivo la completa.
# El SQL sigue en repository.py. Este archivo no arma SELECT ni INSERT.
#
# Llegó acá desde router.py, porque el router estaba haciendo tres trabajos:
#   la ruta HTTP, la transacción (commit / rollback) y el 404 / 409 / 500.
# La ruta se quedó en router.py. La transacción y esos errores viven acá.
#
# math.ceil              → biblioteca estándar. Cantidad de páginas.
# sqlalchemy.exc         → IntegrityError (regla de la tabla) y SQLAlchemyError (el resto).
# sqlalchemy.orm.Session → la sesión que abrió get_db. El servicio no la abre ni la cierra.
# fastapi.HTTPException  → convierte un fallo de la operación en un status HTTP.
#   El router ya no lanza estos 404, 409 y 500: los lanza este archivo.

from math import ceil

from app.models.category import CategoryORM
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from fastapi import HTTPException

from .repository import PostRepository
from .schemas import PaginatedPost, PostCreate, PostPublic, PostSummary, PostUpdate


class PostService:
    # db llega desde el router (Depends(get_db)). El repository usa esa misma sesión.
    def __init__(self, db: Session):
        self.db = db
        self.repository = PostRepository(db)

    # Antes este armado estaba en router.list_posts.
    # Se mudó porque calcular páginas no es parte de la URL: es la operación de listar.
    def list_posts(
        self,
        query: str | None,
        order_by: str,
        direction: str,
        page: int,
        per_page: int,
    ) -> PaginatedPost:
        total, items = self.repository.search(query, order_by, direction, page, per_page)

        # ceil(7/3) = 3 páginas. Sin resultados, 0 páginas.
        total_pages = ceil(total / per_page) if total > 0 else 0
        current_page = 1 if total_pages == 0 else min(page, total_pages)

        has_prev = current_page > 1
        has_next = current_page < total_pages if total_pages > 0 else False

        return PaginatedPost(
            page=current_page,
            per_page=per_page,
            total=total,
            total_pages=total_pages,
            has_prev=has_prev,
            has_next=has_next,
            order_by=order_by,
            direction=direction,
            search=query,
            items=items,
        )

    # Antes: router.filter_by_tags llamaba al repository directo.
    # Pasa por acá para que el router no conozca PostRepository.
    def filter_by_tags(self, tags: list[str]) -> list[PostPublic]:
        return self.repository.by_tags(tags)

    # Antes el 404 y el model_validate estaban en router.get_post.
    # Se mudaron porque decidir "no existe" y qué forma devolver es la operación,
    # no la declaración de la ruta.
    def get_post(self, post_id: int, include_content: bool) -> PostPublic | PostSummary:
        post = self.repository.get(post_id)

        if not post:
            raise HTTPException(status_code=404, detail="Post no encontrado!!")

        # model_validate arma el modelo Pydantic desde el ORM (from_attributes).
        if include_content:
            return PostPublic.model_validate(post, from_attributes=True)

        return PostSummary.model_validate(post, from_attributes=True)

    # Sección 14. Igual que get_post, pero busca por slug.
    # La clase lo hace en la ruta, contra el repository:
    # post = PostRepository(db).get_by_slug(slug)
    # if not post: raise HTTPException(404, "post no encontrado")
    # El 404 y la elección del schema quedan en el servicio, como el get por id.
    # El texto "post no encontrado" es el de la clase, en minúscula.
    def get_post_by_slug(self, slug: str, include_content: bool) -> PostPublic | PostSummary:
        post = self.repository.get_by_slug(slug)
        if not post:
            raise HTTPException(status_code=404, detail="post no encontrado")
        if include_content:
            return PostPublic.model_validate(post, from_attributes=True)
        return PostSummary.model_validate(post, from_attributes=True)

    # Antes el try/commit/rollback estaba en router.create_post.
    # Se mudó porque guardar o deshacer la transacción es la operación completa.
    # El 201 lo sigue declarando el router, en el decorador de la ruta.
    # Sección 8: author: dict, con email y username sacados del token.
    # Sección 12: author es la fila User. El repositorio lee full_name y email.
    def create_post(self, data: PostCreate, author, image_url: str | None = None) -> PostPublic:
        try:
            # model_dump pasa el modelo Pydantic a un dict, que es lo que espera el repositorio.
            # Antes el autor salía del body:
            # author=(data.author.model_dump() if data.author else None),
            # Sección 8: author era el dict del token ({email, username}).
            # Sección 12: es la fila User que devolvió get_current_user.
            # Sección 13. La clase pasa category_id en la llamada del router al
            # repository. Acá sale de PostCreate, que es lo que el servicio ya tiene.
            # La clase no revisa que ese id exista. Si no está, la respuesta trae
            # category en null aunque el número se haya guardado (SQLite no obliga
            # la clave foránea salvo que se prenda). Se responde 404 antes de insertar.
            if data.category_id is not None and self.db.get(CategoryORM, data.category_id) is None:
                raise HTTPException(status_code=404, detail="Categoría no encontrada")
            post = self.repository.create_post(
                title=data.title,
                content=data.content,
                author=author,
                tags=[tag.model_dump() for tag in data.tags],
                # Sección 10. La ruta ya guardó el archivo y manda la URL, o None.
                image_url=image_url,
                category_id=data.category_id,
            )
            self.db.commit()  # acá se confirma la transacción
            self.db.refresh(post)  # relee la fila por si la base completó columnas
            return post
        except IntegrityError:
            # IntegrityError (sqlalchemy.exc): el título único ya existe, u otra regla.
            self.db.rollback()
            raise HTTPException(status_code=409, detail="El título ya existe, prueba con otro")
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al crear el post")

    # Antes el 404, el commit y el rollback estaban en router.update_post.
    def update_post(self, post_id: int, data: PostUpdate) -> PostPublic:
        post = self.repository.get(post_id)

        if not post:
            raise HTTPException(status_code=404, detail="Post no encontrado")

        try:
            # exclude_unset=True: solo cambian los campos que vinieron en el JSON.
            updates = data.model_dump(exclude_unset=True)
            post = self.repository.update_post(post, updates)
            self.db.commit()
            self.db.refresh(post)
            return post
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar el post")

    # Antes el 404, el delete y el commit estaban en router.delete_post.
    # El 204 lo sigue declarando el router, en el decorador. Acá no hay cuerpo que devolver.
    def delete_post(self, post_id: int) -> None:
        post = self.repository.get(post_id)

        if not post:
            raise HTTPException(status_code=404, detail="Post no encontrado")

        try:
            self.repository.delete_post(post)
            self.db.commit()
        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al eliminar el post")
