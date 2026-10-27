# Importar estos módulos registra las tablas en SQLModel.metadata.
# Alembic (alembic/env.py) lee ese metadata para armar y comparar migraciones.
# La sección 16 lo usaba create_all. Desde la 18 ese create_all está comentado.
# El orden importa por las claves foráneas: user primero, después note y label,
# y share al final porque apunta a note, user y label.

from app.models.label import Label, NoteLabelLink
from app.models.note import Note
from app.models.share import LabelShare, NoteShare
from app.models.user import User

__all__ = [
    "Label",
    "LabelShare",
    "Note",
    "NoteLabelLink",
    "NoteShare",
    "User",
]
