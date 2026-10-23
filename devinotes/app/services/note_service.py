# Notas visibles y permisos. La sección 17 lo agrega.
#
# Una nota se ve si sos el dueño, si te la compartieron directo,
# o si te compartieron una etiqueta que la nota tiene.
# Editar pide el rol "edit" en ese share. Borrar solo lo hace el dueño.
#
# HTTPException → 403 sin permiso, 404 si no está o no es tuya.
# Note, NoteCreate, NoteUpdate → tabla y bodies.
# ShareRole → "read" / "edit".
# Los tres repositorios → notas, etiquetas y shares.

from sqlmodel import Session

from app.models.note import Note, NoteCreate, NoteUpdate
from app.models.share import ShareRole
from app.repositories.label_repository import LabelRepository
from app.repositories.note_repository import NoteRepository
from app.repositories.share_repository import ShareRepository
from fastapi import HTTPException


class NoteService:
    def __init__(self, db: Session):
        self.notes = NoteRepository(db)
        self.labels = LabelRepository(db)
        self.shares = ShareRepository(db)

    def user_can_read(self, user_id: int, note: Note) -> bool:
        if note.owner_id == user_id:
            return True
        if note.id is None:
            return False
        if self.shares.has_note_share(note_id=note.id, user_id=user_id):
            return True
        label_ids = self.labels.list_label_ids_for_note(note.id)
        return self.shares.has_any_label_share(label_ids=label_ids, user_id=user_id)

    def user_can_edit(self, user_id: int, note: Note) -> bool:
        if note.owner_id == user_id:
            return True
        if note.id is None:
            return False
        if self.shares.has_note_share(
            note_id=note.id, user_id=user_id, role=ShareRole.EDIT
        ):
            return True
        label_ids = self.labels.list_label_ids_for_note(note.id)
        return self.shares.has_any_label_share(
            label_ids=label_ids, user_id=user_id, role=ShareRole.EDIT
        )

    def list_visible(self, user_id: int) -> list[Note]:
        owned = self.notes.list_owned(user_id)
        direct_ids = self.shares.list_note_ids_shared_directly(user_id)
        shared_label_ids = self.shares.list_label_ids_shared_with_user(user_id)
        ids_by_label = self.labels.list_note_ids_by_label_ids(shared_label_ids)

        # El set junta ids directos e ids que llegan por etiqueta, sin repetir.
        # La clase hace list({...}). Sonar pide la lista entre corchetes, no el
        # constructor list(). [*conjunto] es esa lista. El set sigue sacando repetidos.
        combined_ids = [*{*direct_ids, *ids_by_label}]
        shared = self.notes.list_by_ids(combined_ids)

        combined = {note.id: note for note in owned}
        for note in shared:
            combined.setdefault(note.id, note)

        return sorted(combined.values(), key=lambda note: note.id or 0, reverse=True)

    def create(self, owner_id: int, payload: NoteCreate) -> Note:
        # label_ids no es columna de note. Se guarda en note_label_link.
        note = self.notes.create(
            Note(
                owner_id=owner_id,
                **payload.model_dump(exclude={"label_ids"}),
            )
        )
        if payload.label_ids:
            self._set_labels(owner_id, note.id, payload.label_ids)
        return note

    def update(self, user_id: int, note_id: int, payload: NoteUpdate) -> Note:
        note = self.notes.get(note_id)
        if not note:
            raise HTTPException(status_code=404, detail="Nota no encontrada")
        if not self.user_can_edit(user_id, note):
            raise HTTPException(status_code=403, detail="No autorizado")

        # exclude_none: un campo que no vino en el PATCH no pisa el valor viejo.
        updates = payload.model_dump(exclude_none=True)
        label_ids = updates.pop("label_ids", None)
        for key, value in updates.items():
            setattr(note, key, value)

        note = self.notes.update(note)

        if label_ids is not None:
            # Cambiar etiquetas solo lo hace el dueño, no quien tiene rol edit.
            if note.owner_id != user_id:
                raise HTTPException(
                    status_code=404, detail="No existe o no autorizados"
                )
            self._set_labels(user_id, note.id, label_ids)

        return note

    def delete(self, user_id: int, note_id: int) -> None:
        note = self.notes.get(note_id)
        if not note or note.owner_id != user_id:
            raise HTTPException(
                status_code=404, detail="No existe la nota o no autorizado"
            )
        self.notes.delete(note)

    def _set_labels(self, owner_id: int, note_id: int | None, label_ids: list[int]) -> None:
        if note_id is None:
            raise HTTPException(status_code=404, detail="Nota no encontrada")
        # list_ids_for_owner_subset tira las etiquetas que no son de este usuario.
        valid_ids = self.labels.list_ids_for_owner_subset(owner_id, label_ids or [])
        self.notes.replace_labels(owner_id, note_id, valid_ids)
