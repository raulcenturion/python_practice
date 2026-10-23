# Etiquetas del usuario logueado. La sección 17 lo agrega.
#
# HTTPException → 400 si el nombre ya existe, 404 si no es del dueño.
# Label / LabelCreate → tabla y body.
# LabelRepository     → list, get, get_by_name, create, delete.

from sqlmodel import Session

from app.models.label import Label, LabelCreate
from app.repositories.label_repository import LabelRepository
from fastapi import HTTPException


class LabelService:
    def __init__(self, db: Session):
        self.repo = LabelRepository(db)

    def list(self, owner_id: int) -> list[Label]:
        return self.repo.list_by_user(owner_id)

    def create(self, owner_id: int, payload: LabelCreate) -> Label:
        if self.repo.get_by_name(owner_id, payload.name):
            raise HTTPException(status_code=400, detail="La etiqueta ya existe")
        return self.repo.create(owner_id, payload.name)

    def delete(self, owner_id: int, label_id: int) -> None:
        label = self.repo.get(label_id)
        if not label or label.owner_id != owner_id:
            raise HTTPException(
                status_code=404, detail="La etiqueta no existe o no autorizado"
            )
        self.repo.delete(label)
