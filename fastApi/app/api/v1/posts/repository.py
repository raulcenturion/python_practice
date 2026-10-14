# El repositorio habla con la base. No lo llama el router: lo llama service.py.
# Antes las rutas le pedían los datos directo a esta clase. Eso se mudó al servicio
# para que este archivo solo deje consultas y filas listas, sin commit ni status HTTP.
#
# math.ceil     → biblioteca estándar. Redondea hacia arriba la cantidad de páginas.
# typing        → Optional, List y Tuple son de la biblioteca estándar.
#   Tuple[int, list] hoy se escribe tuple[int, list[...]].
# sqlalchemy    → select y func arman el SQL. Session lo ejecuta.
#   selectinload, joinedload → cómo traer las relaciones en una consulta.
# app.models    → las tablas. PostORM, AuthorORM, TagORM.

from math import ceil

from app.models import AuthorORM, PostORM, TagORM
from sqlalchemy import func, select
from sqlalchemy.orm import Session, joinedload, selectinload


class PostRepository:
    # db es la Session que FastAPI abre en get_db y cierra al terminar el request.
    def __init__(self, db: Session):
        self.db = db

    # Un post por id, o None si no existe.
    # scalar_one_or_none (SQLAlchemy) devuelve el objeto o None. Si hubiera dos filas, lanza error.
    def get(self, post_id: int) -> PostORM | None:
        post_find = select(PostORM).where(PostORM.id == post_id)
        return self.db.execute(post_find).scalar_one_or_none()

    # Busca por título, ordena y corta la página.
    # Devuelve (cantidad total, posts de esta página). La clase lo anota Tuple[int, List[PostORM]].
    def search(
        self,
        query: str | None,
        order_by: str,
        direction: str,
        page: int,
        per_page: int,
    ) -> tuple[int, list[PostORM]]:
        # select() no ejecuta nada todavía. Es el SQL en construcción.
        results = select(PostORM)

        if query:
            # ilike es el LIKE de SQL sin mirar mayúsculas. % es el comodín.
            results = results.where(PostORM.title.ilike(f"%{query}%"))

        # func.count() cuenta filas. subquery() usa el select de arriba como tabla.
        total = self.db.scalar(select(func.count()).select_from(results.subquery())) or 0

        if total == 0:
            return 0, []

        # Si piden la página 99 y solo hay 2, nos quedamos en la última.
        current_page = min(page, max(1, ceil(total / per_page)))

        # func.lower ordena el título sin que "Z" quede antes que "a".
        order_col = PostORM.id if order_by == "id" else func.lower(PostORM.title)

        results = results.order_by(order_col.asc() if direction == "asc" else order_col.desc())
        # Con la lista en memoria, el mismo orden era:
        # results = sorted(results, key=lambda post: post[order_by], reverse=(direction == "desc"))

        # Página 2 con per_page 10 empieza en el registro 10. offset saltea, limit corta.
        start = (current_page - 1) * per_page
        items = self.db.execute(results.limit(per_page).offset(start)).scalars().all()

        return total, items

    # Posts que tengan alguna de las etiquetas pedidas.
    def by_tags(self, tags: list[str]) -> list[PostORM]:
        # strip saca espacios. lower unifica "Python" y "python".
        normalized_tag_names = [tag.strip().lower() for tag in tags if tag.strip()]

        if not normalized_tag_names:
            return []

        # selectinload trae los tags en un segundo SELECT.
        # joinedload trae el autor con un JOIN en la misma consulta.
        # tags.any(...) existe si el post tiene un tag cuyo nombre está en la lista.
        post_list = (
            select(PostORM)
            .options(
                selectinload(PostORM.tags),
                joinedload(PostORM.author),
            )
            .where(PostORM.tags.any(func.lower(TagORM.name).in_(normalized_tag_names)))
            .order_by(PostORM.id.asc())
        )

        return self.db.execute(post_list).scalars().all()

    # Si el email ya existe, devuelve ese autor. Si no, lo inserta.
    def ensure_author(self, name: str, email: str) -> AuthorORM:
        author_obj = self.db.execute(
            select(AuthorORM).where(AuthorORM.email == email)
        ).scalar_one_or_none()

        if author_obj:
            return author_obj

        author_obj = AuthorORM(name=name, email=email)
        self.db.add(author_obj)
        # flush manda el INSERT y consigue el id, sin cerrar la transacción.
        self.db.flush()

        return author_obj

    # Igual que el autor: si el nombre ya existe, devuelve esa fila.
    # Antes: TagORM.name.ilike(name). ilike es "parecido", no "igual".
    # Sección 11 compara el nombre ya pasado a minúsculas.
    def ensure_tag(self, name: str) -> TagORM:
        normalize = name.strip().lower()
        tag_obj = self.db.execute(
            select(TagORM).where(func.lower(TagORM.name) == normalize)
        ).scalar_one_or_none()

        if tag_obj:
            return tag_obj

        # Se guarda en minúsculas, igual que TagRepository.create_tag.
        # Así "Python" escrito en un post y "python" creado en /tags son la misma fila.
        tag_obj = TagORM(name=normalize)
        self.db.add(tag_obj)
        self.db.flush()
        return tag_obj

    # Arma el post, le cuelga autor y tags, y lo deja en la sesión.
    # El commit no es de este archivo. Antes lo hacía router.py.
    # Se mudó a service.py (PostService.create_post): confirmar la transacción
    # es la operación completa, no la ruta HTTP ni el SQL de esta función.
    def create_post(
        self,
        title: str,
        content: str,
        author: dict | None,
        tags: list[dict],
        image_url: str | None = None,
    ) -> PostORM:
        # La clase asigna el autor en el constructor y hace db.add al final.
        # Si el autor ya está en la sesión y el post todavía no, SQLAlchemy avisa
        # "not in session". Por eso el post entra a la sesión antes de colgarle relaciones.
        # Antes: PostORM(title=title, content=content)
        # Sección 10: image_url es la ruta /media/... o None si no hubo archivo.
        post = PostORM(title=title, content=content, image_url=image_url)
        self.db.add(post)

        if author:
            # Antes: ensure_author(author["name"], author["email"])
            # El body traía Author, con name y email.
            # Sección 8: el token trae username, no name. Esa cadena se guarda
            # en la columna name de authors.
            post.author = self.ensure_author(author["username"], author["email"])

        # Sección 11. La clase toma solo el primer tag y parte el nombre por comas:
        # names = tags[0]["name"].split(",")
        # for name in names:
        #     name = name.strip().lower()
        #     if not name:
        #         continue
        #     post.tags.append(self.ensure_tag(name))
        # El formulario puede mandar una etiqueta ("python,fastapi") o varias
        # ("python" y "fastapi"). Se recorre cada una y, además, se parte por comas.
        # ensure_tag vuelve a pasar a minúsculas. Acá también, para el comentario de la clase.
        for tag in tags:
            for name in tag["name"].split(","):
                name = name.strip().lower()
                if not name:
                    continue
                post.tags.append(self.ensure_tag(name))

        # flush escribe el INSERT. refresh relee id y created_at que puso la base.
        self.db.flush()
        self.db.refresh(post)
        return post

    # Copia al objeto solo las claves que vinieron en el JSON.
    # setattr escribe el atributo. El commit lo guarda service.py, no esta función.
    # Antes el comentario decía que lo guardaba la ruta.
    def update_post(self, post: PostORM, updates: dict) -> PostORM:
        for key, value in updates.items():
            setattr(post, key, value)

        return post

    # Marca la fila para borrarla. El commit lo confirma service.py.
    # Antes lo confirmaba la ruta, en router.delete_post.
    def delete_post(self, post: PostORM) -> None:
        self.db.delete(post)
