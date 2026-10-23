# SQL de usuarios. La sesión entra por el constructor, igual que en las notas.
#
# sqlmodel.Session → la sesión que abre get_session.
# sqlmodel.select  → el SELECT. where filtra por email, que es unique.

from sqlmodel import Session, select

from app.models.user import User


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:
        # first() es la primera fila o None. Con el unique del email hay una o ninguna.
        return self.db.exec(select(User).where(User.email == email)).first()

    def create(self, user: User) -> User:
        self.db.add(user)
        # La clase deja comentado self.db.flush() y llama self.commit().
        # flush manda el INSERT y todavía no cierra la transacción.
        # commit cierra. UserRepository no define commit: es self.db.commit().
        # self.db.flush()
        self.db.commit()
        self.db.refresh(user)
        return user
