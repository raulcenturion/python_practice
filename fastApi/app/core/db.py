# Conexión a la base. La usa cualquier ruta a través de Depends(get_db).
#
# os              → biblioteca estándar de Python. Lee variables de entorno.
# dotenv          → paquete python-dotenv. load_dotenv() lee el archivo .env.
# sqlalchemy      → paquete SQLAlchemy. El ORM y el motor de la base.
#   create_engine → abre la base a partir de una URL.
#   sessionmaker  → fábrica de sesiones (una charla con la base por request).
#   Session       → esa charla: add, commit, execute, close.
#   DeclarativeBase → clase madre de los modelos (AuthorORM, PostORM, TagORM).

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

# La clase llama load_dotenv() en main.py, después de importar este módulo.
# Llega tarde: la línea de DATABASE_URL ya se ejecutó al importar.
# Por eso se carga el .env acá, antes de leer la variable.
load_dotenv()

# Si .env no tiene DATABASE_URL, se usa el archivo SQLite blog.db.
# sqlite:///./blog.db se crea en la carpeta desde donde arrancás el servidor.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./blog.db")

# SQLite no deja usar la misma conexión en otro hilo.
# FastAPI a veces lo hace, así que check_same_thread=False solo para sqlite.
# Postgres (postgresql+psycopg://...) no necesita esa clave.
engine_kwargs = {}
if DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

# echo=True imprime el SQL en la terminal. future=True pide el estilo de SQLAlchemy 2
# (en la versión 2 ya es el default; la clase lo deja escrito igual).
engine = create_engine(DATABASE_URL, echo=True, future=True, **engine_kwargs)

# autoflush=False: no manda cambios solos; hay que flush() o commit().
# autocommit=False: hay que llamar db.commit() para guardar.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=Session)


# Base no es un modelo de Pydantic. Es la madre de las tablas de SQLAlchemy.
class Base(DeclarativeBase):
    pass


# FastAPI llama a get_db en cada request que declara db: Session = Depends(get_db).
# yield entrega la sesión a la ruta. finally cierra la sesión aunque la ruta falle.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
