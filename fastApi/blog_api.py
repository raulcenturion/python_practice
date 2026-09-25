# Nombres de este proyecto (la clase usa Post / BLOG_POST / /posts):
#   BlogPost, BlogPostCreate, BlogPostUpdate, BlogPostResponse, BlogPostSummary
#   PaginatedBlogPosts
#   lista BLOG_POSTS
#   rutas /blog-posts
#
# La clase importa Optional, List y Union. Eso sigue funcionando, pero es la forma vieja.
# Lo que queda activo es el equivalente actual (hace lo mismo, sin esos imports):
#   Optional[X]  →  X | None
#   List[X]      →  list[X]
#   Union[A, B]  →  A | B
# Literal no tiene reemplazo: sigue saliendo de typing.
# Body está importado en la clase y no se usa: un modelo Pydantic en el parámetro YA es el body.

from math import ceil
from typing import Literal

from pydantic import BaseModel, EmailStr, Field, field_validator

from fastapi import FastAPI, HTTPException, Path, Query

app = FastAPI(title="API de prueba", description="Esta es una API de prueba")

# 15 posts para poder ver la paginación (page / per_page).
# tags solo en algunos: el resto usa la lista vacía del modelo.
BLOG_POSTS = [
    {"id": 1, "title": "Hola desde FastAPI1", "content": "Mi primer post con FastAPI1"},
    {"id": 2, "title": "Mi segundo Post con FastAPI1", "content": "Mi segundo post con FastAPI1"},
    {
        "id": 3,
        "title": "Django vs FastAPI1",
        "content": "FastAPI es más rápido por varias razones concretas1",
        "tags": [{"name": "Python"}, {"name": "fastapi"}, {"name": "Django"}],
    },
    {"id": 4, "title": "Hola desde FastAPI2", "content": "Mi primer post con FastAPI2"},
    {"id": 5, "title": "Mi segundo Post con FastAPI2", "content": "Mi segundo post con FastAPI2 blablabla"},
    {"id": 6, "title": "Django vs FastAPI2", "content": "FastAPI es más rápido por varias razones concretas2"},
    {"id": 7, "title": "Hola desde FastAPI3", "content": "Mi primer post con FastAPI3"},
    {"id": 8, "title": "Mi segundo Post con FastAPI3", "content": "Mi segundo post con FastAPI3 blablabla"},
    {"id": 9, "title": "Django vs FastAPI3", "content": "FastAPI es más rápido por varias razones concretas3"},
    {"id": 10, "title": "Hola desde FastAPI4", "content": "Mi primer post con FastAPI4"},
    {"id": 11, "title": "Mi segundo Post con FastAPI", "content": "Mi segundo post con FastAPI blablabla"},
    {
        "id": 12,
        "title": "Django vs FastAPI",
        "content": "FastAPI es más rápido por varias razones concretas",
        "tags": [{"name": "Python"}, {"name": "fastapi"}, {"name": "Django"}],
    },
    {"id": 13, "title": "Hola desde FastAPI", "content": "Mi primer post con FastAPI"},
    {"id": 14, "title": "Mi segundo Post con FastAPI", "content": "Mi segundo post con FastAPI blablabla"},
    {
        "id": 15,
        "title": "Django vs FastAPI",
        "content": "FastAPI es más rápido por varias razones concretas",
        "tags": [{"name": "Python"}, {"name": "fastapi"}, {"name": "Django"}],
    },
]


class Tag(BaseModel):
    # Field(...) = el nombre es obligatorio. min/max = largo del texto.
    name: str = Field(..., min_length=2, max_length=30, description="Nombre de la etiqueta")


class Author(BaseModel):
    name: str
    # EmailStr rechaza "hola" y acepta "ana@mail.com".
    email: EmailStr


# Base del post (en la clase: PostBase). El id no va acá: lo asigna el servidor al crear.
class BlogPost(BaseModel):
    title: str
    content: str
    # default_factory=list crea una lista nueva por post.
    # La clase antes usaba = [] y esa misma lista se compartía entre objetos.
    tags: list[Tag] = Field(default_factory=list)
    author: Author | None = None


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


# La clase ahora deja title opcional (antes en este archivo era obligatorio).
# Así el PUT puede mandar solo content. Field(None, ...) de la clase = Field(default=None).
class BlogPostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    content: str | None = None


# Respuesta completa (en la clase: PostPublic). Suma el id a la base.
class BlogPostResponse(BlogPost):
    id: int


# Respuesta corta, sin content (en la clase: PostSummary).
class BlogPostSummary(BaseModel):
    id: int
    title: str


# Envoltorio de la lista paginada. En la clase: PaginatedPost / List[PostPublic].
class PaginatedBlogPosts(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    has_prev: bool
    has_next: bool
    # Literal solo acepta esos textos. Otro valor → 422.
    order_by: Literal["id", "title"]
    direction: Literal["asc", "desc"]
    search: str | None = None
    items: list[BlogPostResponse]


@app.get("/")
def read_root():
    return {"message": "Esta es una API de prueba"}


# --- Lista anterior: devolvía todos los posts, sin página ni orden. ---
# @app.get("/blog-posts", response_model=list[BlogPostResponse])
# def get_blog_posts(query: str | None = Query(default=None, description="Texto para buscar")):
#     if query:
#         return [post for post in BLOG_POSTS if query.lower() in post["title"].lower()]
#     return BLOG_POSTS
#
# Ahora la lista pagina, ordena y busca. El nombre en la URL puede ser search
# (alias) aunque el parámetro en Python se llame query.
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
):
    results = BLOG_POSTS
    # Si mandan search, se usa. Si no, cae al parámetro viejo text.
    query = query or text
    if query:
        results = [post for post in results if query.lower() in post["title"].lower()]

    total = len(results)
    # ceil(7/3) = 3 páginas. Si no hay resultados, 0 páginas.
    total_pages = ceil(total / per_page) if total > 0 else 0
    # Si piden la página 99 y solo hay 2, nos quedamos en la última.
    current_page = 1 if total_pages == 0 else min(page, total_pages)

    # reverse=True cuando direction es desc. order_by solo puede ser id o title.
    results = sorted(results, key=lambda post: post[order_by], reverse=(direction == "desc"))

    if total_pages == 0:
        items = []
    else:
        # Página 2 con per_page 10 → empieza en el índice 10.
        start = (current_page - 1) * per_page
        items = results[start : start + per_page]

    return PaginatedBlogPosts(
        page=current_page,
        per_page=per_page,
        total=total,
        total_pages=total_pages,
        has_prev=current_page > 1,
        has_next=current_page < total_pages if total_pages > 0 else False,
        order_by=order_by,
        direction=direction,
        search=query,
        items=items,
    )


# Esta ruta va ANTES de /blog-posts/{post_id}.
# Si estuviera después, "by-tags" se interpretaría como un id y fallaría.
@app.get("/blog-posts/by-tags", response_model=list[BlogPostResponse])
def filter_by_tags(
    tags: list[str] = Query(
        ...,
        min_length=2,
        description="Una o más etiquetas. Ejemplo: ?tags=python&tags=fastapi",
    ),
):
    # Comparar en minúsculas para que "Python" y "python" coincidan.
    tags_lower = [tag.lower() for tag in tags]
    return [
        post
        for post in BLOG_POSTS
        if any(tag["name"].lower() in tags_lower for tag in post.get("tags", []))
    ]


# --- Antes el id era un int pelado, sin mínimo ni texto de ayuda. ---
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
):
    for post in BLOG_POSTS:
        if post["id"] == post_id:
            if not include_content:
                return {"id": post["id"], "title": post["title"]}
            return post
    raise HTTPException(status_code=404, detail="Post no encontrado!!!")


@app.post(
    "/blog-posts",
    response_model=BlogPostResponse,
    response_description="Post creado (OK)",
)
def create_blog_post(post: BlogPostCreate):
    new_id = (BLOG_POSTS[-1]["id"] + 1) if BLOG_POSTS else 1
    new_post = {
        "id": new_id,
        "title": post.title,
        "content": post.content,
        "tags": [tag.model_dump() for tag in post.tags],
        "author": post.author.model_dump() if post.author else None,
    }
    BLOG_POSTS.append(new_post)
    return new_post


# exclude_unset=True: solo cambia los campos que vinieron en el JSON.
# response_model_exclude_none=True: no muestra en la respuesta las claves en None.
@app.put(
    "/blog-posts/{post_id}",
    response_model=BlogPostResponse,
    response_description="Post actualizado",
    response_model_exclude_none=True,
)
def update_post(post_id: int, data: BlogPostUpdate):
    for post in BLOG_POSTS:
        if post["id"] == post_id:
            payload = data.model_dump(exclude_unset=True)
            if "title" in payload:
                post["title"] = payload["title"]
            if "content" in payload:
                post["content"] = payload["content"]
            return post
    raise HTTPException(status_code=404, detail="Post no encontrado")


@app.delete("/blog-posts/{post_id}", status_code=204)
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POSTS):
        if post["id"] == post_id:
            BLOG_POSTS.pop(index)
            return
    raise HTTPException(status_code=404, detail="Post no encontrado")
