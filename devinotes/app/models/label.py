# Etiquetas de una nota, y la tabla intermedia nota ↔ etiqueta.
#
# sqlalchemy.UniqueConstraint → paquete SQLAlchemy. Un índice único de
#   varias columnas. SQLModel no trae un atajo propio para esto, así que
#   se usa el de SQLAlchemy. La clase lo importa igual.
# sqlmodel.SQLModel / Field  → la tabla y las columnas.

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class Label(SQLModel, table=True):
    # La clase fija el nombre. Sin esto SQLModel usaría "label" igual,
    # porque la clase se llama Label. Queda escrito para que no dependa del default.
    __tablename__ = "label"
    # Un usuario no puede tener dos etiquetas con el mismo nombre.
    __table_args__ = (UniqueConstraint("owner_id", "name", name="uq_label_owner_name"),)

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, min_length=1, max_length=50)
    owner_id: int = Field(foreign_key="user.id", index=True)


class NoteLabelLink(SQLModel, table=True):
    __tablename__ = "note_label_link"
    # La sección 16 pone name="uq_label_owner_name", el mismo nombre que en Label.
    # En Postgres el nombre de un constraint es único en el esquema, y
    # create_all falla al repetirlo. Acá se usó uq_note_label.
    # La migración de la sección 18 lo llama uq_note_label_link. El modelo
    # usa ese nombre para que autogenerate no pida otro rename.
    __table_args__ = (UniqueConstraint("note_id", "label_id", name="uq_note_label_link"),)

    id: int | None = Field(default=None, primary_key=True)
    note_id: int = Field(foreign_key="note.id", index=True)
    label_id: int = Field(foreign_key="label.id", index=True)


class LabelCreate(SQLModel):
    name: str


class LabelRead(SQLModel):
    id: int
    name: str
    model_config = {"from_attributes": True}
