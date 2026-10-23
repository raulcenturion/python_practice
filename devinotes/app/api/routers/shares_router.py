# Compartir una nota o una etiqueta con otro usuario.
#
# APIRouter / status → FastAPI. 201 al compartir, 204 al quitar.
# CurrentUser, DBSession → api/deps.py.
# ShareRequest → target_user_id y role, en models/share.py.
# ShareService → solo el dueño puede llamar.

from app.api.deps import CurrentUser, DBSession
from app.models.share import ShareRequest
from app.services.share_service import ShareService
from fastapi import APIRouter, status

router = APIRouter(prefix="/shares", tags=["Shares"])


@router.post("/notes/{note_id}", status_code=status.HTTP_201_CREATED)
def share_note(note_id: int, payload: ShareRequest, db: DBSession, user: CurrentUser):
    share = ShareService(db).share_note(
        user.id, note_id, payload.target_user_id, payload.role
    )
    return {
        "id": share.id,
        "note_id": note_id,
        "user_target_id": payload.target_user_id,
        "role": share.role,
    }


@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def unshare_note(note_id: int, target_user_id: int, db: DBSession, user: CurrentUser):
    # target_user_id es un query param: no hay body en el DELETE de la clase.
    # La clase también hace return None. El 204 no lleva body.
    ShareService(db).unshare_note(user.id, note_id, target_user_id)


@router.post("/labels/{label_id}", status_code=status.HTTP_201_CREATED)
def share_label(label_id: int, payload: ShareRequest, db: DBSession, user: CurrentUser):
    share = ShareService(db).share_label(
        user.id, label_id, payload.target_user_id, payload.role
    )
    return {
        "id": share.id,
        "label_id": label_id,
        "user_target_id": payload.target_user_id,
        "role": share.role,
    }


@router.delete("/labels/{label_id}", status_code=status.HTTP_204_NO_CONTENT)
def unshare_label(label_id: int, target_user_id: int, db: DBSession, user: CurrentUser):
    # Igual que unshare_note: la clase retorna None y acá el 204 queda vacío.
    ShareService(db).unshare_label(user.id, label_id, target_user_id)
