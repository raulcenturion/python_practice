# SQL de la tabla users. Sección 12.
# No hace commit y no responde HTTP. Eso está en service.py.
#
# sqlalchemy.select      → arma el SELECT.
# sqlalchemy.orm.Session → la sesión que abrió get_db.
# app.models.user.User   → la tabla users. La clase no le pone el sufijo ORM.

from app.models.user import User
from sqlalchemy import select
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    # db.get (SQLAlchemy) busca por clave primaria. None si el id no existe.
    # La clase 11 hacía este get dentro de security.py (db.get(User, user_id)).
    # get_current_user lo sigue haciendo allá, porque es la revisión del token
    # y no una operación de "usuarios". Este método lo usa el cambio de rol.
    def get(self, user_id: int) -> User | None:
        return self.db.get(User, user_id)

    # El login busca por email, no por id. El token todavía no existe.
    def get_by_email(self, email: str) -> User | None:
        query = select(User).where(User.email == email)
        return self.db.execute(query).scalar_one_or_none()

    # Arma la fila y la deja en la sesión. El commit lo hace el servicio.
    # hashed_password ya viene hasheado: esta función no ve la clave en texto.
    def create(self, email: str, hashed_password: str, full_name: str | None) -> User:
        user = User(
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
        )
        self.db.add(user)
        # flush manda el INSERT y consigue el id, sin cerrar la transacción.
        self.db.flush()
        self.db.refresh(user)
        return user

    # Cambia la columna role. No elige si ese rol está permitido: eso lo valida
    # RoleUpdate (schemas) antes de llegar acá.
    def set_role(self, user: User, role: str) -> User:
        user.role = role
        self.db.add(user)
        self.db.flush()
        self.db.refresh(user)
        return user
