# CRUD de notas. El usuario sale del token (CurrentUser), no del body.
#
# APIRouter / status → FastAPI. 201 al crear, 204 al borrar.
# CurrentUser, DBSession → api/deps.py.
# NoteCreate, NoteRead, NoteUpdate → models/note.py.
# NoteService → services/note_service.py.

from app.api.deps import CurrentUser, DBSession
from app.models.note import NoteCreate, NoteRead, NoteUpdate
from app.services.note_service import NoteService
from fastapi import APIRouter, status

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.get("/", response_model=list[NoteRead])
def list_notes(db: DBSession, user: CurrentUser):
    return NoteService(db).list_visible(user.id)


@router.post("/", response_model=NoteRead, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, db: DBSession, user: CurrentUser):
    return NoteService(db).create(user.id, payload)


@router.patch("/{note_id}", response_model=NoteRead)
def update_note(note_id: int, payload: NoteUpdate, db: DBSession, user: CurrentUser):
    return NoteService(db).update(user.id, note_id, payload)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: DBSession, user: CurrentUser):
    # La clase cierra con return None. Un 204 no lleva body.
    NoteService(db).delete(user.id, note_id)
