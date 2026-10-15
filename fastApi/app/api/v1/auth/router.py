# Rutas de autenticación.
# Sección 8: login contra FAKE_USERS y /me con email y username. Quedó comentado.
# Sección 12: la tabla users, la clave hasheada y los roles.
#
# POST /api/v1/auth/register     alta. El rol inicial es "user".
# POST /api/v1/auth/login        JSON {email, password}. Devuelve token y usuario.
# POST /api/v1/auth/token        formulario. Lo usa el botón Authorize de /docs.
# GET  /api/v1/auth/me           la fila del token.
# PUT  /api/v1/auth/role/{id}    cambia el rol. Solo un admin.
#
# El prefix "/auth" se suma al "/api/v1" que pone main.py.
#
# fastapi.APIRouter                    → el grupo de rutas.
# fastapi.Depends                       → abre la sesión y exige token o rol.
# fastapi.HTTPException                 → la clase lo lanza en la ruta. Ahora lo lanza el servicio.
# fastapi.Path                          → el id de la URL. ge=1 rechaza 0 y negativos.
# fastapi.status                        → 201 con nombre, en vez del número suelto.
# fastapi.security.OAuth2PasswordRequestForm
#   → usuario y clave como formulario. Swagger lo manda así a /token.
#     El campo se llama username. Acá el valor es el email.
# sqlalchemy.orm.Session                → el tipo de la sesión. La abre core/db.py.
# app.models.user.User                  → la fila que devuelve get_current_user.
# require_admin                         → el token tiene que ser de un admin. Si no, 403.

from app.core.db import get_db
from app.core.security import auth2_token, get_current_user, require_admin
from app.models.user import User
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, Path, status

from .schemas import RoleUpdate, TokenResponse, UserCreate, UserLogin, UserPublic
from .service import AuthService

# --- Sección 8. Usuarios en memoria. Ya no se usa. ---
# La clave estaba en texto plano. La sección 12 guarda el hash en la tabla users.
#
# from datetime import timedelta
# from fastapi.security import OAuth2PasswordRequestForm
# from app.core.security import create_access_token
# from .schemas import Token
#
# FAKE_USERS = {
#     "ricardo@example.com": {
#         "email": "ricardo@example.com",
#         "username": "ricardo",
#         "password": "secret123",
#     },
#     "alumno@example.com": {
#         "email": "alumno@example.com",
#         "username": "alumno",
#         "password": "123456",
#     },
# }
#
# @router.post("/login", response_model=Token)
# def login(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = FAKE_USERS.get(form_data.username)
#     if not user or user["password"] != form_data.password:
#         raise HTTPException(status_code=401, detail="Credenciales inválidas")
#     token = create_access_token(
#         data={"sub": user["email"], "username": user["username"]},
#         expires_delta=timedelta(minutes=30),
#     )
#     return {"access_token": token, "token_type": "bearer"}
#
# @router.get("/me", response_model=UserPublic)
# def read_me(current=Depends(get_current_user)):
#     return {"email": current["email"], "username": current["username"]}

router = APIRouter(prefix="/auth", tags=["auth"])


# El body es JSON (UserCreate), no el formulario de la sección 8.
@router.post("/register", response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    # La clase, en la ruta:
    # repository = UserRepository(db)
    # if repository.get_by_email(payload.email):
    #     raise HTTPException(status_code=400, detail="Email ya registrado")
    # user = repository.create(email=..., hashed_password=hash_password(...), full_name=...)
    # db.commit()
    # db.refresh(user)
    # return UserPublic.model_validate(user)
    user = AuthService(db).register(payload)
    return UserPublic.model_validate(user)


# La clase lo escribió async def login. Es def: la consulta es síncrona
# (Session de SQLAlchemy, sin await). async sin await no espera y el editor avisa.
# Volvería a ser async con await si el acceso a la base fuera un cliente async.
@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    # La clase:
    # user = UserRepository(db).get_by_email(payload.email)
    # if not user or not verify_password(payload.password, user.hashed_password):
    #     raise HTTPException(status_code=401, detail="Credenciales inválidas")
    # token = create_access_token(sub=str(user.id))
    # return TokenResponse(access_token=token, user=UserPublic.model_validate(user))
    return AuthService(db).login(payload)


# current es la fila User, no el dict {email, username} de la sección 8.
# La clase lo escribió async def read_me. Es def porque solo arma el JSON.
@router.get("/me", response_model=UserPublic)
def read_me(current: User = Depends(get_current_user)):
    return UserPublic.model_validate(current)


# require_admin corre antes de la función. Un user o un editor reciben 403.
# Un usuario nuevo se registra como "user". Esta ruta no puede crear al primer
# admin: hace falta una fila que ya tenga role = "admin".
# La clase anota payload: RoleUpdate = None. Ese None deja el body opcional y
# después payload.role revienta si no mandan JSON. El body es obligatorio.
@router.put("/role/{user_id}", response_model=UserPublic)
def set_role(
    # El body va primero: no tiene default. Si va después de user_id=Path(...),
    # Python rechaza la función (un parámetro sin default no puede seguir a uno con default).
    # FastAPI igual lee user_id de la URL y payload del JSON.
    payload: RoleUpdate,
    user_id: int = Path(..., ge=1),
    db: Session = Depends(get_db),
    _admin: User = Depends(require_admin),
):
    # _admin no se lee. Depends(require_admin) está para frenar a quien no es admin.
    # La clase:
    # user = UserRepository(db).get(user_id)
    # if not user: raise HTTPException(404, "Usuario no encontrado")
    # updated = repository.set_role(user, payload.role)
    # db.commit()
    # db.refresh(updated)
    # return UserPublic.model_validate(updated)
    updated = AuthService(db).set_role(user_id, payload.role)
    return UserPublic.model_validate(updated)


# tokenUrl de OAuth2PasswordBearer apunta acá: /api/v1/auth/token.
# Swagger manda username y password como formulario, no como el JSON de /login.
# La clase lo escribió async def token_endpoint. auth2_token no tiene await.
@router.post("/token")
def token_endpoint(response=Depends(auth2_token)):
    # La dependencia ya armó {access_token, token_type}. La ruta lo devuelve.
    return response
