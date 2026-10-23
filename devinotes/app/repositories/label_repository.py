# SQL de etiquetas y de la tabla intermedia note_label_link.
#
# sqlmodel.Session / select / delete → sesión, SELECT y DELETE.
#   exec() de SQLModel, cuando el SELECT es de una sola columna o de un modelo,
#   ya devuelve un ScalarResult. La sección 16 encadenaba otro .scalars().
#   La aclaración de la sección 17 dice lo mismo: con session.execute() de
#   SQLAlchemy sí hace falta .scalars(); con session.exec() de SQLModel no.
#   ScalarResult no tiene scalars. AttributeError.
#   La sección 17 lo dejó en .all(). Acá también.

from sqlmodel import Session, delete, select

from app.models.label import Label, NoteLabelLink
from app.models.share import LabelShare


class LabelRepository:
    def __init__(self, db: Session):
        self.db = db

    def list_by_user(self, owner_id: int) -> list[Label]:
        query = select(Label).where(Label.owner_id == owner_id).order_by(Label.name.asc())
        return list(self.db.exec(query).all())

    def get(self, label_id: int) -> Label | None:
        return self.db.get(Label, label_id)

    def get_by_name(self, owner_id: int, name: str) -> Label | None:
        query = select(Label).where(Label.owner_id == owner_id, Label.name == name)
        return self.db.exec(query).first()

    def create(self, owner_id: int, name: str) -> Label:
        label = Label(owner_id=owner_id, name=name)
        self.db.add(label)
        self.db.commit()
        self.db.refresh(label)
        return label

    def delete(self, label: Label) -> None:
        # Borra los vínculos y los shares de esta etiqueta antes que la fila.
        self.db.exec(delete(NoteLabelLink).where(NoteLabelLink.label_id == label.id))
        self.db.exec(delete(LabelShare).where(LabelShare.label_id == label.id))
        self.db.delete(label)
        self.db.commit()

    def list_ids_for_owner_subset(self, owner_id: int, ids: list[int]) -> list[int]:
        if not ids:
            return []

        # select(Label.id) es una columna. exec() ya hizo scalars().
        # La clase: ).scalars().all()
        found = self.db.exec(
            select(Label.id).where(Label.owner_id == owner_id, Label.id.in_(set(ids)))
        ).all()
        return list(found)

    def list_label_ids_for_note(self, note_id: int) -> list[int]:
        # La clase también llama .scalars() acá. Mismo error.
        found = self.db.exec(
            select(NoteLabelLink.label_id).where(NoteLabelLink.note_id == note_id)
        ).all()
        return list(found)

    def list_note_ids_by_label_ids(self, label_ids: list[int]) -> list[int]:
        if not label_ids:
            return []

        found = self.db.exec(
            select(NoteLabelLink.note_id).where(NoteLabelLink.label_id.in_(label_ids))
        ).all()
        return list(found)
