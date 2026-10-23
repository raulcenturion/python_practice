# SQL de las notas. No hay commit en el router: esta sección no tiene rutas.
# El repository abre la sesión que le pasan y confirma él mismo.
#
# sqlmodel.Session → la sesión. exec corre un select o un delete de SQLModel.
# sqlmodel.select  → arma el SELECT. Es el select de SQLAlchemy.
# sqlmodel.delete  → arma el DELETE de filas. No es el delete de httpx.
#
# La clase importa `from httpx import delete` y después
# `from sqlmodel import Session, select, delete`. El segundo pisa al primero.
# httpx.delete es para un HTTP DELETE. Acá no se usa. No se importa.

from sqlmodel import Session, delete, select

from app.models.label import NoteLabelLink
from app.models.note import Note


class NoteRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_owned(self, owner_id: int) -> list[Note]:
        # order_by id desc: la nota más nueva primero.
        query = select(Note).where(Note.owner_id == owner_id).order_by(Note.id.desc())
        # exec ya devuelve las filas Note. .all() es la lista.
        return list(self.db.exec(query).all())

    def get(self, note_id: int) -> Note | None:
        # get busca por clave primaria. None si no está.
        return self.db.get(Note, note_id)

    def create(self, note: Note) -> Note:
        self.db.add(note)
        # La clase llama self.commit(). NoteRepository no tiene ese método:
        # AttributeError al crear. El commit es de la sesión.
        self.db.commit()
        # refresh vuelve a leer la fila: llena el id que generó la base.
        self.db.refresh(note)
        return note

    def update(self, note: Note) -> Note:
        # La clase copia create: add, commit y refresh.
        # Sonar lo marca porque los dos métodos hacen lo mismo.
        # create inserta una fila nueva. update cambia una que ya tiene id.
        # merge escribe ese estado sobre la fila persistente. add, en una nota
        # que no está en la sesión, puede intentar otro INSERT y chocar con la clave.
        if note.id is None:
            raise ValueError("update necesita una nota que ya tenga id")
        merged = self.db.merge(note)
        self.db.commit()
        self.db.refresh(merged)
        return merged

    def delete(self, note: Note) -> None:
        # Primero los vínculos nota-etiqueta. Si no, la clave foránea puede frenar el DELETE.
        self.db.exec(delete(NoteLabelLink).where(NoteLabelLink.note_id == note.id))
        self.db.delete(note)
        self.db.commit()

    def replace_labels(self, owner_id: int, note_id: int, label_ids: list[int]) -> None:
        # owner_id lo recibe la clase y esta sección no lo usa para filtrar.
        # Queda en la firma para cuando el servicio compruebe que la nota es de ese usuario.
        _ = owner_id
        self.db.exec(delete(NoteLabelLink).where(NoteLabelLink.note_id == note_id))

        # set quita ids repetidos. `or []` cubre el None que puede traer el DTO.
        for label in set(label_ids or []):
            self.db.add(NoteLabelLink(note_id=note_id, label_id=label))

        self.db.commit()

    def list_by_ids(self, ids: list[int]) -> list[Note]:
        if not ids:
            return []

        return list(self.db.exec(select(Note).where(Note.id.in_(ids))).all())
