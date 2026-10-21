# Modelos del JSON: lo que entra y lo que sale por la API.
# No son tablas. Las tablas están en app/models.
#
# pydantic          → valida el body y arma la respuesta.
#   BaseModel       → clase madre de estos modelos.
#   Field           → reglas (largo, ejemplo, valor por defecto).
#   field_validator → función que revisa un campo después de leerlo.
#   EmailStr        → solo acepta un email. Viene de pydantic (usa email-validator).
#   ConfigDict      → opciones del modelo. from_attributes lee un objeto ORM.
# typing            → biblioteca estándar.
#   Optional[X]     → X o None. Hoy se escribe X | None y hace lo mismo.
#   List[X]         → lista de X. Hoy se escribe list[X].
#   Literal         → el valor solo puede ser uno de esos textos.
#   Annotated       → junta el tipo con Form(...) en el mismo parámetro.
# fastapi.Form      → el campo llega como formulario, no como JSON.

from typing import Annotated, Literal

from app.api.v1.auth.schemas import UserPublic
from app.api.v1.categories.schemas import CategoryPublic
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator

from fastapi import Form


class Tag(BaseModel):
    # Field(...) = obligatorio. min_length y max_length limitan el texto.
    name: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Nombre de la etiqueta",
    )
    # from_attributes (Pydantic v2) arma este modelo desde un TagORM.
    # En Pydantic v1 el mismo flag se llamaba orm_mode = True.
    model_config = ConfigDict(from_attributes=True)


class Author(BaseModel):
    name: str
    email: EmailStr  # "hola" falla con 422. "ana@mail.com" pasa.

    model_config = ConfigDict(from_attributes=True)


# Campos comunes de un post. El id no va acá: lo asigna la base al insertar.
# En la clase, tags es Optional[List[Tag]]. list[Tag] es el equivalente.
class PostBase(BaseModel):
    title: str
    content: str
    # default_factory=list crea una lista nueva por objeto.
    # = [] compartiría la misma lista entre todos los posts.
    tags: list[Tag] | None = Field(default_factory=list)
    # Sección 13. Antes la respuesta traía author (tabla authors):
    # author: Author | None = None
    # Ahora trae el usuario logueado (tabla users) y, si tiene, la categoría.
    # UserPublic y CategoryPublic son schemas, no las tablas.
    user: UserPublic | None = None
    category: CategoryPublic | None = None
    # Sección 10. URL pública de la imagen, por ejemplo /media/abc.png.
    # None si el post se creó sin archivo. La clase lo escribe Optional[str].
    image_url: str | None = None

    model_config = ConfigDict(from_attributes=True)


# Body del POST. No hereda de PostBase: el título y el contenido tienen reglas propias.
class PostCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Titulo del post (mínimo 3 caracteres, máximo 100)",
        examples=["Mi primer post con FastAPI"],
    )
    # Si el cliente no manda content, se usa el default.
    content: str | None = Field(
        default="Contenido no disponible",
        min_length=10,
        description="Contenido del post (mínimo 10 caracteres)",
        examples=["Este es un contenido válido porque tiene 10 caracteres o más"],
    )
    # Sección 13. Id de la categoría. En el modelo es opcional.
    # En el formulario de abajo la clase lo pide siempre (Form sin default).
    category_id: int | None = None
    tags: list[Tag] = Field(default_factory=list)
    # Sección 8. El autor ya no se manda en el JSON: lo pone el token en create_post.
    # La clase comenta esta línea. La respuesta (PostBase) sigue teniendo author.
    # author: Author | None = None

    # field_validator corre después de leer el título.
    # ValueError acá se convierte en 422. No hace falta HTTPException.
    @field_validator("title")
    @classmethod
    def not_allowed_title(cls, value: str) -> str:
        if "spam" in value.lower():
            raise ValueError("El título no puede contener la palabra: 'spam'")
        return value

    # Arma el PostCreate desde campos de formulario, no desde un JSON.
    # El POST del post ahora es multipart: así puede viajar la imagen al lado.
    # Form(min_length=3) valida el texto igual que Field, pero en el form.
    # tags llega como textos sueltos ("python", "fastapi") y acá se vuelven Tag.
    @classmethod
    def as_form(
        cls,
        title: Annotated[str, Form(min_length=3)],
        content: Annotated[str, Form(min_length=10)],
        # ge=1: el id es 1 o más. Sin default, el formulario no crea el post si falta.
        # La clase lo escribe así. Antes de la sección 13 este campo no estaba.
        category_id: Annotated[int, Form(ge=1)],
        tags: Annotated[list[str] | None, Form()] = None,
    ):
        tag_objs = [Tag(name=tag) for tag in (tags or [])]
        return cls(title=title, content=content, category_id=category_id, tags=tag_objs)


# Body del PUT. Los dos campos son opcionales: se puede mandar solo uno.
# Field(None, ...) de la clase es lo mismo que Field(default=None).
class PostUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=100)
    content: str | None = None


# Respuesta completa. Suma el id a PostBase.
# Hereda from_attributes, y además la clase lo repite en esta clase.
class PostPublic(PostBase):
    id: int
    # Sección 14. El slug no se manda en el alta: lo arma el repository desde el título.
    slug: str

    model_config = ConfigDict(from_attributes=True)


# Respuesta corta, cuando include_content=false. Sin content, sin tags, sin autor.
class PostSummary(BaseModel):
    id: int
    title: str

    model_config = ConfigDict(from_attributes=True)


# Envoltorio de la lista paginada. items son posts completos (PostPublic).
class PaginatedPost(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    has_prev: bool
    has_next: bool
    # Literal (typing) rechaza cualquier otro texto con 422.
    order_by: Literal["id", "title"]
    direction: Literal["asc", "desc"]
    search: str | None = None
    items: list[PostPublic]
