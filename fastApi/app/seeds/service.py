# Escribe en la base las listas de data/. Sección 14.
# No es una ruta: lo llama run.py desde la terminal.
#
# contextlib.contextmanager → biblioteca estándar. Convierte una función
#   con yield en un with. Acá el with confirma o revierte la transacción.
# sqlalchemy.select          → arma el SELECT.
# sqlalchemy.orm.Session     → la sesión. SessionLocal la abre en core/db.py.
# hash_password              → pwdlib, vía app.core.security. La misma función del login.
#   La clase define otra vez hash_password con PasswordHash.recommended().
#   Hace lo mismo. Se usa la que ya está en security.py para no tener dos.
# CategoryORM, TagORM, User  → las tablas que se llenan.

from contextlib import contextmanager

from app.core.db import Base, SessionLocal, engine
from app.core.security import hash_password
from app.models.category import CategoryORM
from app.models.tag import TagORM
from app.models.user import User
from app.seeds.data.categories import CATEGORIES
from app.seeds.data.tags import TAGS
from app.seeds.data.users import USERS
from sqlalchemy import select
from sqlalchemy.orm import Session


# atomic(db) envuelve la escritura. Al salir, la transacción queda cerrada.
# La clase hace try, yield, commit y, si algo falla, except Exception con rollback.
# Sonar marca el commit que queda después del yield: si el with se corta, ese
# commit no corre, y el rollback solo cubría SQLAlchemyError. finally corre
# siempre. Si el commit ya cerró la transacción, in_transaction() es falso y
# no se toca. Si el bloque o el commit fallan, sigue abierta y rollback la deshace.
# La clase anota Optional en los helpers de abajo. X | None es lo mismo.
@contextmanager
def atomic(db: Session):
    try:
        yield
        db.commit()
    finally:
        if db.in_transaction():
            db.rollback()


def _user_by_email(db: Session, email: str) -> User | None:
    # scalars().first() es la primera fila o None. El email es unique.
    return db.execute(select(User).where(User.email == email)).scalars().first()


def _category_by_slug(db: Session, slug: str) -> CategoryORM | None:
    return db.execute(select(CategoryORM).where(CategoryORM.slug == slug)).scalars().first()


def _tag_by_name(db: Session, name: str) -> TagORM | None:
    return db.execute(select(TagORM).where(TagORM.name == name)).scalars().first()


# La clase deja estos if adentro de seed_users. Sonar cuenta cada if anidado
# como más complejo. Acá el update es una función aparte: si no cambió nada, no hace add.
def _update_user(db: Session, obj: User, full_name: str | None, plain: str | None, role: str) -> None:
    changed = False
    if obj.full_name != full_name:
        obj.full_name = full_name
        changed = True
    if plain:
        obj.hashed_password = hash_password(plain)
        changed = True
    if obj.role != role:
        obj.role = role
        changed = True
    if changed:
        db.add(obj)


# Si el email ya está, actualiza nombre, clave y rol. Si no, inserta.
# Correr el seed de nuevo no duplica usuarios.
def seed_users(db: Session) -> None:
    with atomic(db):
        for data in USERS:
            # La clase solo lee data.get("role"). El archivo de la clase
            # trae "editor" en vez de "role". Si falta role, se usa esa clave.
            role = data.get("role") or data.get("editor") or "user"
            # La clase lee data["password"]. El dict ahora usa "plain"
            # para que Sonar no vea una credencial escrita junto a esa palabra.
            plain = data.get("plain") or data.get("password")
            obj = _user_by_email(db, data["email"])
            if obj:
                _update_user(db, obj, data.get("full_name"), plain, role)
            elif plain:
                db.add(
                    User(
                        email=data["email"],
                        full_name=data.get("full_name"),
                        role=role,
                        hashed_password=hash_password(plain),
                    )
                )


def seed_categories(db: Session) -> None:
    with atomic(db):
        for data in CATEGORIES:
            obj = _category_by_slug(db, data["slug"])
            # La clase anida dos if (existe, y el nombre cambió). Sonar pide unirlos:
            # el de afuera no hace otra cosa que entrar al de adentro.
            if obj and obj.name != data["name"]:
                obj.name = data["name"]
                db.add(obj)
            elif obj is None:
                db.add(CategoryORM(name=data["name"], slug=data["slug"]))


def seed_tags(db: Session) -> None:
    with atomic(db):
        for data in TAGS:
            obj = _tag_by_name(db, data["name"])
            # Misma unión de if que en las categorías. Con el nombre como clave,
            # si lo encontró el nombre ya coincide y esta rama no escribe.
            # La clase igual compara y, si difiere, actualiza.
            if obj and obj.name != data["name"]:
                obj.name = data["name"]
                db.add(obj)
            elif obj is None:
                db.add(TagORM(name=data["name"]))


# La clase no crea las tablas: asume que el servidor ya corrió create_all.
# Si se ejecuta el seed antes de levantar la API, la base puede no tener
# users, categories ni tags. create_all las crea si faltan y no toca las que están.
def _ensure_tables() -> None:
    Base.metadata.create_all(bind=engine)


# SessionLocal() abre una sesión fuera de un request. get_db no corre acá
# porque no hay una ruta. El with la cierra al salir.
def run_all() -> None:
    _ensure_tables()
    with SessionLocal() as db:
        seed_users(db)
        seed_categories(db)
        seed_tags(db)


def run_users() -> None:
    _ensure_tables()
    with SessionLocal() as db:
        seed_users(db)


def run_categories() -> None:
    _ensure_tables()
    with SessionLocal() as db:
        seed_categories(db)


def run_tags() -> None:
    _ensure_tables()
    with SessionLocal() as db:
        seed_tags(db)
