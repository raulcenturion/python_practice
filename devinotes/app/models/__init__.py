# Importar estos módulos registra las tablas en SQLModel.metadata.
# init_db hace create_all sobre ese metadata. Sin estos imports, no hay tablas.
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
