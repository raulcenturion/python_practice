# JSON de las etiquetas. No es la tabla: la tabla es TagORM en models/tag.py.
#
# pydantic.BaseModel   → la forma del body y de la respuesta.
# pydantic.ConfigDict  → from_attributes deja armar el JSON desde un TagORM.
# pydantic.Field       → largo mínimo, máximo y el texto que muestra /docs.
#
# La clase importa `from click import Option`. click es la librería de
# terminales, no tiene que ver con este schema, y Option no se usa.
# Ese import no va.

from pydantic import BaseModel, ConfigDict, Field


# Lo que devuelve el API. id lo pone la base. name lo valida Field.
class TagPublic(BaseModel):
    id: int
    # ... significa obligatorio. Sin name, FastAPI responde 422.
    name: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Nombre de la etiqueta1",
    )

    # Sin esto, model_validate(tag_orm) no lee los atributos del objeto.
    model_config = ConfigDict(from_attributes=True)


# Body del POST. No trae id: lo genera la base.
class TagCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Nombre de la etiqueta2",
    )


# Body del PUT. En la clase name es obligatorio, así que el PUT manda el nombre entero.
class TagUpdate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=30,
        description="Nombre de la etiqueta",
    )


# La usa GET /tags/popular/top: el tag más unido a posts, más cuántas veces.
# La clase define esta clase y la ruta devuelve el dict suelto, sin response_model.
# El router de este proyecto sí la usa, para que /docs muestre id, name y uses.
class TagWithCount(TagPublic):
    uses: int
