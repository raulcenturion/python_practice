# Operación de registro, login y cambio de rol. Sección 12.
# El router pide. Este archivo confirma la transacción y arma el 400, el 401 y el 404.
#
# La clase no tiene este archivo: el router crea UserRepository y hace commit
# en la ruta. En posts y en tags esa mezcla se mudó al servicio. Acá también.
# El código de la clase quedó comentado en router.py.
#
# sqlalchemy.orm.Session → la sesión que abrió get_db. Este archivo no la cierra.
# fastapi.HTTPException  → 400 email repetido, 401 clave mala, 404 id inexistente.
# hash_password          → pwdlib. La clave no se guarda en texto plano.
# verify_password        → compara el texto con el hash de la fila.
# create_access_token    → firma el JWT. En sub va el id del usuario, como texto.
# invalid_credentials    → el 401 "Credenciales inválidas". La clase lo usa en /token
#   y en /login arma el HTTPException a mano, con el mismo status y el mismo texto.

from app.core.security import (
    create_access_token,
    hash_password,
    invalid_credentials,
    verify_password,
)
from app.models.user import User
from sqlalchemy.orm import Session

from fastapi import HTTPException

from .repository import UserRepository
from .schemas import TokenResponse, UserCreate, UserLogin, UserPublic


class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = UserRepository(db)

    # None si el email no está o si la clave no coincide con el hash.
    # La respuesta es la misma en los dos casos: no se dice cuál falló.
    def authenticate(self, email: str, password: str) -> User:
        user = self.repository.get_by_email(email)
        if not user or not verify_password(password, user.hashed_password):
            raise invalid_credentials()
        return user

    def register(self, payload: UserCreate) -> User:
        if self.repository.get_by_email(payload.email):
            raise HTTPException(status_code=400, detail="Email ya registrado")

        user = self.repository.create(
            email=payload.email,
            hashed_password=hash_password(payload.password),
            full_name=payload.full_name,
        )
        # El rol no se manda en el body. La columna tiene default "user".
        self.db.commit()
        self.db.refresh(user)
        return user

    def login(self, payload: UserLogin) -> TokenResponse:
        user = self.authenticate(payload.email, payload.password)
        # sub es el id, no el email. get_current_user hace int(sub) y busca la fila.
        token = create_access_token(sub=str(user.id))
        return TokenResponse(
            access_token=token,
            user=UserPublic.model_validate(user),
        )

    # Lo usa POST /token, el formulario de Swagger. El campo del form se llama
    # username; el valor que escribís es el email.
    def token_for(self, email: str, password: str) -> dict:
        user = self.authenticate(email, password)
        token = create_access_token(sub=str(user.id))
        return {"access_token": token, "token_type": "bearer"}

    def set_role(self, user_id: int, role: str) -> User:
        user = self.repository.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")

        updated = self.repository.set_role(user, role)
        self.db.commit()
        self.db.refresh(updated)
        return updated
