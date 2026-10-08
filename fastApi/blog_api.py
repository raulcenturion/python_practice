# Histórico. La clase siguió en el paquete app/ (app/main.py).
# Este archivo queda para ver el módulo 6 en un solo archivo.
#
# Módulo 6: la API deja de usar la lista en memoria y habla con una base de datos.
#
# Nombres de este proyecto (la clase usa Post / /posts):
#   BlogPost, BlogPostCreate, BlogPostUpdate, BlogPostResponse, BlogPostSummary
#   PaginatedBlogPosts
#   BlogPostORM, AuthorORM, TagORM   (en la clase: PostORM, AuthorORM, TagORM)
#   rutas /blog-posts                 (en la clase: /posts)
#
# La clase importa Optional, List y Union. Eso sigue funcionando, pero es la forma vieja.
# Lo que queda activo es el equivalente actual (hace lo mismo, sin esos imports):
#   Optional[X]  →  X | None
#   List[X]      →  list[X]
#   Union[A, B]  →  A | B
# Literal no tiene reemplazo: sigue saliendo de typing.
# Body está importado en la clase y no se usa: un modelo Pydantic en el parámetro YA es el body.

# os, datetime, math, typing: biblioteca estándar de Python (no se instalan).
#   os.getenv lee DATABASE_URL. datetime guarda created_at.
#   ceil redondea las páginas. Literal limita un texto a "id"/"title" o "asc"/"desc".
import os
from datetime import datetime
from math import ceil
from typing import Literal

# python-dotenv: load_dotenv() lee el archivo .env.
# pydantic: los modelos del JSON (lo que entra y lo que sale por la API).
# sqlalchemy: el ORM. create_engine abre la base, select/func arman el SQL,
#   IntegrityError y SQLAlchemyError son los errores de la base.
#   Session es la conversación con la base (add, commit, query).
from dotenv import load_dotenv
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    UniqueConstraint,
    create_engine,
    func,
    select,
)
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    joinedload,
    mapped_column,
    relationship,
    selectinload,
    sessionmaker,
)

# fastapi: la API. Depends inyecta la sesión. status son los códigos HTTP (201, 204).
# Va separado de pydantic/sqlalchemy: en esta máquina la carpeta fastapi/ del repo
# hace que Ruff trate a fastapi como código propio, no como paquete de terceros.
from fastapi import Depends, FastAPI, HTTPException, Path, Query, status

# load_dotenv busca un archivo .env en la carpeta desde donde arrancás el servidor.
# No pisa variables que ya existan en el entorno.
# DATABASE_URL no va en el código: vive en .env, y .env está en .gitignore.
load_dotenv()
# os.getenv es de la stdlib. El segundo argumento es el valor si la variable no existe.
# sqlite:///./blog.db = archivo blog.db en el directorio actual (tres barras: sqlite:// + /ruta).
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

# create_engine abre la conexión. echo=True imprime el SQL en la terminal (sirve para estudiar).
# future=True pide el estilo de SQLAlchemy 2. En la versión 2 ya es el default; la clase lo deja igual.
# SQLite no deja usar la misma conexión en otro hilo. FastAPI a veces lo hace,
# por eso check_same_thread=False. En Postgres o MySQL esa clave no se pasa.
engine_kwargs = {}
if DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, echo=True, future=True, **engine_kwargs)

# sessionmaker fabrica una Session por request. La Session es la que hace add/commit/query.
# autoflush=False: no manda cambios a la base hasta el flush o el commit explícito.
# autocommit=False: hay que llamar db.commit() para guardar.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=Session)


# DeclarativeBase (SQLAlchemy) es la clase madre de las tablas. No es un modelo de Pydantic.
class Base(DeclarativeBase):
    pass


# Tabla intermedia de la relación muchos-a-muchos posts ↔ tags.
# No es una clase: es sqlalchemy.Table. Las dos columnas juntas son la clave primaria.
# ondelete="CASCADE": si se borra el post o el tag, se borra la fila de esta tabla.
post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)


class AuthorORM(Base):
    __tablename__ = "authors"

    # Mapped + mapped_column es el estilo de SQLAlchemy 2 (en la 1.x era Column suelto).
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)

    # relationship no es una columna: es el vínculo con BlogPostORM.author.
    posts: Mapped[list["BlogPostORM"]] = relationship(back_populates="author")


class TagORM(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, index=True)

    # secondary=post_tags: el vínculo pasa por la tabla intermedia.
    # lazy="selectin": al leer tags, SQLAlchemy trae los posts con un SELECT ... IN (...).
    posts: Mapped[list["BlogPostORM"]] = relationship(
        secondary=post_tags,
        back_populates="tags",
        lazy="selectin",
    )


# En la clase esta clase se llama PostORM y la tabla sigue llamándose "posts".
class BlogPostORM(Base):
    __tablename__ = "posts"
    # UniqueConstraint: dos posts no pueden tener el mismo title. Si pasa, la base lanza IntegrityError.
    __table_args__ = (UniqueConstraint("title", name="unique_post_title"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    # La clase usa datetime.utcnow (stdlib). Devuelve la hora UTC sin zona horaria.
    # El equivalente actual es datetime.now(timezone.utc). Se deja utcnow para coincidir con el módulo.
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # author_id es la columna real (clave foránea). author es el objeto AuthorORM.
    author_id: Mapped[int | None] = mapped_column(ForeignKey("authors.id"))
    author: Mapped[AuthorORM | None] = relationship(back_populates="posts")

    tags: Mapped[list[TagORM]] = relationship(
        secondary=post_tags,
        back_populates="posts",
        lazy="selectin",
        # passive_deletes: el DELETE del post lo resuelve la base (ON DELETE CASCADE),
        # SQLAlchemy no recorre la lista de tags para borrar las filas de post_tags.
        passive_deletes=True,
    )


# Crea las tablas si no existen. La clase lo marca como "dev": en un proyecto real
# las tablas las arma una migración (Alembic), no create_all al importar el archivo.
Base.metadata.create_all(bind=engine)


# Depends(get_db) (FastAPI) llama a esta función en cada request.
# yield entrega la Session a la ruta. El finally corre siempre, también si la ruta falla.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI(title="API de prueba", description="Esta es una API de prueba")

# --- Lista en memoria del módulo anterior. Ya no es la fuente de datos. ---
# La base arranca vacía: los posts se crean con POST /blog-posts.
# Estos títulos se repiten ("Django vs FastAPI" está tres veces) y la tabla
# posts ahora tiene un título único, así que esta lista no se puede insertar tal cual.
# BLOG_POSTS = [
#     {"id": 1, "title": "Hola desde FastAPI1", "content": "Mi primer post con FastAPI1"},
#     {"id": 2, "title": "Mi segundo Post con FastAPI1", "content": "Mi segundo post con FastAPI1"},
#     {
#         "id": 3,
#         "title": "Django vs FastAPI1",
#         "content": "FastAPI es más rápido por varias razones concretas1",
#         "tags": [{"name": "Python"}, {"name": "fastapi"}, {"name": "Django"}],
#     },
#     {"id": 4, "title": "Hola desde FastAPI2", "content": "Mi primer post con FastAPI2"},
#     {"id": 5, "title": "Mi segundo Post con FastAPI2", "content": "Mi segundo post con FastAPI2 blablabla"},
#     {"id": 6, "title": "Django vs FastAPI2", "content": "FastAPI es más rápido por varias razones concretas2"},
#     {"id": 7, "title": "Hola desde FastAPI3", "content": "Mi primer post con FastAPI3"},
#     {"id": 8, "title": "Mi segundo Post con FastAPI3", "content": "Mi segundo post con FastAPI3 blablabla"},
#     {"id": 9, "title": "Django vs FastAPI3", "content": "FastAPI es más rápido por varias razones concretas3"},
#     {"id": 10, "title": "Hola desde FastAPI4", "content": "Mi primer post con FastAPI4"},
#     {"id": 11, "title": "Mi segundo Post con FastAPI", "content": "Mi segundo post con FastAPI blablabla"},
#     {
#         "id": 12,
#         "title": "Django vs FastAPI",
#         "content": "FastAPI es más rápido por varias razones concretas",
#         "tags": [{"name": "Python"}, {"name": "fastapi"}, {"name": "Django"}],
#     },
#     {"id": 13, "title": "Hola desde FastAPI", "content": "Mi primer post con FastAPI"},
#     {"id": 14, "title": "Mi segundo Post con FastAPI", "content": "Mi segundo post con FastAPI blablabla"},
#     {
#         "id": 15,
#         "title": "Django vs FastAPI",
#         "content": "FastAPI es más rápido por varias razones concretas",
#         "tags": [{"name": "Python"}, {"name": "fastapi"}, {"name": "Django"}],
#     },
# ]


class Tag(BaseModel):
    # Field(...) = el nombre es obligatorio. min/max = largo del texto.
    name: str = Field(..., min_length=2, max_length=30, description="Nombre de la etiqueta")
    # from_attributes (Pydantic v2) deja armar este modelo desde un TagORM.
    # En Pydantic v1 el mismo flag se llamaba orm_mode = True.
    model_config = ConfigDict(from_attributes=True)


class Author(BaseModel):
    name: str
    # EmailStr (pydantic) rechaza "hola" y acepta "ana@mail.com".
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# Base del post (en la clase: PostBase). El id no va acá: lo asigna la base al crear.
class BlogPost(BaseModel):
    title: str
    content: str
    # default_factory=list crea una lista nueva por post.
    # La clase antes usaba = [] y esa misma lista se compartía entre objetos.
    tags: list[Tag] = Field(default_factory=list)
    author: Author | None = None

    model_config = ConfigDict(from_attributes=True)


class BlogPostCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Titulo del post (mínimo 3 caracteres, máximo 100)",
        examples=["Mi primer post con FastAPI"],
    )
    # str | None = Optional[str]. El default se usa si el cliente no manda content.
    content: str | None = Field(
        default="Contenido no disponible",
        min_length=10,
        description="Contenido del post (mínimo 10 caracteres)",
        examples=["Este es un contenido válido porque tiene 10 caracteres o más"],
    )
    tags: list[Tag] = Field(default_factory=list)
    author: Author | None = None

    @field_validator("title")
    @classmethod
    def not_allowed_title(cls, value: str) -> str:
        # ValueError acá se convierte en 422, no hace falta HTTPException.
        if "spam" in value.lower():
            raise ValueError("El título no puede contener la palabra: 'spam'")
        return value


# La clase deja title opcional. Así el PUT puede mandar solo content.
# Field(None, ...) de la clase = Field(default=None).
class BlogPostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    content: str | None = None


# Respuesta completa (en la clase: PostPublic). Suma el id a la base.
# Hereda model_config de BlogPost, así FastAPI puede devolver un BlogPostORM.
class BlogPostResponse(BlogPost):
    id: int


# Respuesta corta, sin content (en la clase: PostSummary).
class BlogPostSummary(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


# Envoltorio de la lista paginada. En la clase: PaginatedPost / List[PostPublic].
class PaginatedBlogPosts(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    has_prev: bool
    has_next: bool
    # Literal (typing) solo acepta esos textos. Otro valor → 422.
    order_by: Literal["id", "title"]
    direction: Literal["asc", "desc"]
    search: str | None = None
    items: list[BlogPostResponse]


# La clase devuelve "Bienvenidos a Mini Blog por Devtalles".
# Se deja el mensaje de este proyecto.
@app.get("/")
def read_root():
    return {"message": "Esta es una API de prueba"}


# --- Lista anterior: filtraba y paginaba la lista BLOG_POSTS en Python. ---
# @app.get("/blog-posts", response_model=PaginatedBlogPosts)
# def get_blog_posts(...):
#     results = BLOG_POSTS
#     query = query or text
#     if query:
#         results = [post for post in results if query.lower() in post["title"].lower()]
#     total = len(results)
#     results = sorted(results, key=lambda post: post[order_by], reverse=(direction == "desc"))
#     start = (current_page - 1) * per_page
#     items = results[start : start + per_page]
#     return PaginatedBlogPosts(...)
#
# Ahora el filtro, el conteo, el orden y el corte de página los hace SQL.
# db: Session = Depends(get_db) pide la sesión de get_db. Depends es de FastAPI.
@app.get("/blog-posts", response_model=PaginatedBlogPosts)
def get_blog_posts(
    # text está obsoleto: sigue andando para no romper clientes viejos, Swagger lo marca deprecated.
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
        # Solo letras, números, espacio, acentos y guion. Otra cosa → 422.
        pattern=r"^[\w\sáéíóúÁÉÍÓÚüÜ-]+$",
    ),
    per_page: int = Query(10, ge=1, le=50, description="Número de resultados (1-50)"),
    page: int = Query(1, ge=1, description="Número de página (>=1)"),
    order_by: Literal["id", "title"] = Query("id", description="Campo de orden"),
    direction: Literal["asc", "desc"] = Query("asc", description="Dirección de orden"),
    db: Session = Depends(get_db),
):
    # select() arma el SQL. Todavía no lo ejecuta: eso lo hace db.execute / db.scalar.
    results = select(BlogPostORM)

    query = query or text
    if query:
        # ilike es el LIKE de SQL sin importar mayúsculas. % es el comodín.
        results = results.where(BlogPostORM.title.ilike(f"%{query}%"))

    # func.count() (sqlalchemy) cuenta filas. subquery() convierte el select filtrado en una tabla.
    total = db.scalar(select(func.count()).select_from(results.subquery())) or 0
    total_pages = ceil(total / per_page) if total > 0 else 0
    current_page = 1 if total_pages == 0 else min(page, total_pages)

    if order_by == "id":
        order_col = BlogPostORM.id
    else:
        # func.lower ordena el título sin que "Z" quede antes que "a".
        order_col = func.lower(BlogPostORM.title)

    results = results.order_by(order_col.asc() if direction == "asc" else order_col.desc())
    # Antes, con la lista en memoria, el orden era este:
    # results = sorted(results, key=lambda post: post[order_by], reverse=(direction == "desc"))

    if total_pages == 0:
        items: list[BlogPostORM] = []
    else:
        start = (current_page - 1) * per_page
        # limit/offset es el corte de página en SQL. scalars() devuelve objetos BlogPostORM, no filas crudas.
        items = db.execute(results.limit(per_page).offset(start)).scalars().all()

    has_prev = current_page > 1
    has_next = current_page < total_pages if total_pages > 0 else False

    return PaginatedBlogPosts(
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


# Esta ruta va ANTES de /blog-posts/{post_id}.
# Si estuviera después, "by-tags" se interpretaría como un id y fallaría.
# --- Antes comparaba los dict de BLOG_POSTS en Python. ---
# tags_lower = [tag.lower() for tag in tags]
# return [post for post in BLOG_POSTS if any(tag["name"].lower() in tags_lower for tag in post.get("tags", []))]
# La clase pide min_length=1 (una etiqueta alcanza). Antes este archivo pedía 2.
@app.get("/blog-posts/by-tags", response_model=list[BlogPostResponse])
def filter_by_tags(
    tags: list[str] = Query(
        ...,
        min_length=1,
        description="Una o más etiquetas. Ejemplo: ?tags=python&tags=fastapi",
    ),
    db: Session = Depends(get_db),
):
    normalized_tag_names = [tag.strip().lower() for tag in tags if tag.strip()]

    if not normalized_tag_names:
        return []

    # selectinload y joinedload (sqlalchemy.orm) dicen cómo traer las relaciones en esta consulta.
    # tags ya tiene lazy="selectin" en el modelo; acá se repite para que el SELECT quede explícito.
    # author no tiene ese lazy, por eso joinedload lo trae en el mismo query (JOIN).
    post_list = (
        select(BlogPostORM)
        .options(
            selectinload(BlogPostORM.tags),
            joinedload(BlogPostORM.author),
        )
        .where(BlogPostORM.tags.any(func.lower(TagORM.name).in_(normalized_tag_names)))
        .order_by(BlogPostORM.id.asc())
    )

    posts = db.execute(post_list).scalars().all()
    return posts


# --- Antes recorría BLOG_POSTS con un for y devolvía el dict. ---
# for post in BLOG_POSTS:
#     if post["id"] == post_id:
#         if not include_content:
#             return {"id": post["id"], "title": post["title"]}
#         return post
# raise HTTPException(status_code=404, detail="Post no encontrado!!!")
#
# La clase pone Path(...) para documentar y rechazar id < 1.
# Escribieron example=1; en Pydantic reciente se usa examples=[1].
# También escribieron return HTTPException: eso responde 200. Acá se usa raise.
@app.get(
    "/blog-posts/{post_id}",
    response_model=BlogPostResponse | BlogPostSummary,
    response_description="Post encontrado",
)
def get_blog_post(
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
    post_find = select(BlogPostORM).where(BlogPostORM.id == post_id)
    # scalar_one_or_none: un objeto, o None si no hay fila. Si hubiera dos, lanza error.
    post = db.execute(post_find).scalar_one_or_none()
    # Forma corta de la clase, equivalente cuando el id es la clave primaria:
    # post = db.get(BlogPostORM, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado!")

    # model_validate arma el modelo Pydantic desde el ORM (from_attributes).
    if include_content:
        return BlogPostResponse.model_validate(post, from_attributes=True)

    return BlogPostSummary.model_validate(post, from_attributes=True)


# --- Antes calculaba el id a mano y hacía BLOG_POSTS.append. ---
# new_id = (BLOG_POSTS[-1]["id"] + 1) if BLOG_POSTS else 1
# new_post = {"id": new_id, "title": post.title, "content": post.content, ...}
# BLOG_POSTS.append(new_post)
#
# status.HTTP_201_CREATED (fastapi.status) es el 201. Antes este archivo respondía 200.
@app.post(
    "/blog-posts",
    response_model=BlogPostResponse,
    response_description="Post creado (OK)",
    status_code=status.HTTP_201_CREATED,
)
def create_blog_post(post: BlogPostCreate, db: Session = Depends(get_db)):
    author_obj = None
    if post.author:
        # Si el email ya existe, se reutiliza ese autor. Si no, se inserta uno nuevo.
        author_obj = db.execute(
            select(AuthorORM).where(AuthorORM.email == post.author.email)
        ).scalar_one_or_none()

        if not author_obj:
            author_obj = AuthorORM(name=post.author.name, email=post.author.email)
            db.add(author_obj)
            # flush manda el INSERT y consigue el id, sin cerrar la transacción.
            db.flush()

    new_post = BlogPostORM(title=post.title, content=post.content, author=author_obj)
    # La clase hace db.add recién antes del commit.
    # Si el autor o el tag ya están en la sesión y el post todavía no,
    # SQLAlchemy avisa "not in session" al armar la relación. Agregarlo ahora lo evita.
    db.add(new_post)

    for tag in post.tags:
        # ilike: "Python" y "python" son el mismo tag.
        tag_obj = db.execute(select(TagORM).where(TagORM.name.ilike(tag.name))).scalar_one_or_none()
        if not tag_obj:
            tag_obj = TagORM(name=tag.name)
            db.add(tag_obj)
            db.flush()
        new_post.tags.append(tag_obj)

    try:
        db.commit()  # acá sí se guarda
        db.refresh(new_post)  # relee la fila para traer el id y created_at que puso la base
        return new_post
    except IntegrityError:
        # IntegrityError (sqlalchemy.exc): el título único ya existe, u otra regla de la tabla.
        db.rollback()
        raise HTTPException(status_code=409, detail="El título ya existe, prueba con otro")
    except SQLAlchemyError:
        # Cualquier otro error de la base. rollback deshace lo que no se commiteó.
        db.rollback()
        raise HTTPException(status_code=500, detail="Error al crear el post")


# --- Antes recorría la lista y copiaba title/content en el dict. ---
# for post in BLOG_POSTS:
#     if post["id"] == post_id:
#         payload = data.model_dump(exclude_unset=True)
#         ...
# exclude_unset=True: solo cambia los campos que vinieron en el JSON.
# response_model_exclude_none=True: no muestra en la respuesta las claves en None.
# setattr escribe el atributo del ORM; el commit lo persiste.
@app.put(
    "/blog-posts/{post_id}",
    response_model=BlogPostResponse,
    response_description="Post actualizado",
    response_model_exclude_none=True,
)
def update_post(post_id: int, data: BlogPostUpdate, db: Session = Depends(get_db)):
    # db.get busca por clave primaria. Equivale al select por id del GET.
    post = db.get(BlogPostORM, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")

    updates = data.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(post, key, value)

    db.add(post)
    db.commit()
    db.refresh(post)

    return post


# --- Antes hacía BLOG_POSTS.pop(index). ---
# status.HTTP_204_NO_CONTENT es el 204: éxito sin cuerpo. Antes el número estaba suelto (status_code=204).
@app.delete("/blog-posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.get(BlogPostORM, post_id)

    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")

    db.delete(post)
    db.commit()
    # 204 no lleva cuerpo. La clase cierra con `return` vacío.
    # Sin ese return la función igual termina y FastAPI responde 204.
