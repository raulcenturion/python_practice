# JSON de las categorías. No es la tabla: la tabla es CategoryORM.
#
# pydantic.BaseModel → la forma del body y de la respuesta.
# pydantic.Field     → largo mínimo y máximo. Si no cumple, FastAPI responde 422.
# ConfigDict         → from_attributes arma el JSON desde un CategoryORM.
#   La clase escribe model_config = {"from_attributes": True}. Es el mismo flag
#   en forma de dict. ConfigDict es la forma que usa el resto del proyecto.

from pydantic import BaseModel, ConfigDict, Field


# name y slug obligatorios, entre 2 y 60 caracteres.
class CategoryBase(BaseModel):
    name: str = Field(min_length=2, max_length=60)
    slug: str = Field(min_length=2, max_length=60)


# Body del POST. Hereda name y slug. pass: no agrega campos.
class CategoryCreate(CategoryBase):
    pass


# Body del PUT. Los dos son opcionales: se puede mandar solo el nombre, solo el slug, o los dos.
# str | None es lo mismo que Optional[str].
class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=60)
    slug: str | None = Field(default=None, min_length=2, max_length=60)


# Lo que devuelve la API. Suma el id que puso la base.
class CategoryPublic(CategoryBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
