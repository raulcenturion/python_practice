# Con quién se comparte una nota o una etiqueta, y con qué permiso.
#
# enum.Enum              → biblioteca estándar. Lista cerrada de textos.
# sqlalchemy.UniqueConstraint → un usuario no se repite en la misma nota
#   ni en la misma etiqueta.
# sqlmodel.SQLModel/Field → la tabla y las columnas.

from enum import Enum

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel


class ShareRole(str, Enum):
    # str además de Enum: el valor que se guarda es "read" o "edit", no el nombre READ.
    READ = "read"
    EDIT = "edit"


class NoteShare(SQLModel, table=True):
    __tablename__ = "note_share"
    __table_args__ = (UniqueConstraint("note_id", "user_id", name="uq_note_user"),)

    id: int | None = Field(default=None, primary_key=True)
    # La clase escribe `note_id = int = Field(...)`. Eso no anota el tipo:
    # asigna el Field a note_id y también al nombre int, dentro de la clase.
    # SQLModel no ve la columna. Los dos puntos son la anotación.
    note_id: int = Field(foreign_key="note.id", index=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)


class LabelShare(SQLModel, table=True):
    __tablename__ = "label_share"
    __table_args__ = (UniqueConstraint("label_id", "user_id", name="uq_label_user"),)

    id: int | None = Field(default=None, primary_key=True)
    # Igual que NoteShare. La clase asigna con `=` en vez de anotar con `:`.
    label_id: int = Field(foreign_key="label.id", index=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    role: ShareRole = Field(default=ShareRole.READ)


# Body de POST /shares. No es tabla: no lleva table=True.
# La sección 17 lo agrega. Field(gt=0) rechaza un id 0 o negativo.
class ShareRequest(SQLModel):
    target_user_id: int = Field(gt=0)
    role: ShareRole = ShareRole.READ
