# Tabla note y los JSON de alta, edición y lectura.
#
# typing.Optional → biblioteca estándar. Optional[str] es str | None.
#   La clase lo usa. Acá queda str | None, que es lo mismo.
# sqlmodel        → SQLModel es la clase madre. Field declara la columna
#   y, en los DTO, las reglas del JSON.

from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    # Tabla "note". owner_id apunta a user.id: la nota es de un usuario.
    id: int | None = Field(default=None, primary_key=True)
    title: str
    content: str = ""
    # La clase anota Optional[str]. str | None es el mismo tipo.
    color: str | None = None
    owner_id: int = Field(foreign_key="user.id", index=True)


# DTOs. No llevan table=True: no son tablas.
# label_ids no es una columna de note. El vínculo está en note_label_link.
class NoteCreate(SQLModel):
    title: str
    content: str = ""
    color: str | None = None
    label_ids: list[int] | None = None


class NoteUpdate(SQLModel):
    title: str | None = None
    content: str | None = None
    color: str | None = None
    label_ids: list[int] | None = None


class NoteRead(SQLModel):
    id: int
    title: str
    content: str
    color: str | None
    model_config = {"from_attributes": True}
