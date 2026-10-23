# CRUD de etiquetas del usuario del token.
#
# APIRouter / status → FastAPI.
# CurrentUser, DBSession → api/deps.py.
# LabelCreate, LabelRead → models/label.py.
# LabelService → services/label_service.py.

from app.api.deps import CurrentUser, DBSession
from app.models.label import LabelCreate, LabelRead
from app.services.label_service import LabelService
from fastapi import APIRouter, status

router = APIRouter(prefix="/labels", tags=["Labels"])


@router.get("/", response_model=list[LabelRead])
def list_labels(db: DBSession, user: CurrentUser):
    return LabelService(db).list(user.id)


@router.post("/", response_model=LabelRead, status_code=status.HTTP_201_CREATED)
def create_label(payload: LabelCreate, db: DBSession, user: CurrentUser):
    return LabelService(db).create(user.id, payload)


@router.delete("/{label_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_label(label_id: int, db: DBSession, user: CurrentUser):
    # Igual que en notas: la clase hace return None y el 204 no lleva body.
    LabelService(db).delete(user.id, label_id)
