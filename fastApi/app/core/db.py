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

# Hasta la sección 14 la clase usa echo=True: imprime cada SQL en la terminal.
# Sección 15 lo pasa a False. Si queda en True, el ENTRADA/SALIDA del middleware
# se pierde entre las consultas. future=True pide el estilo de SQLAlchemy 2
# (en la versión 2 ya es el default; la clase lo deja escrito igual).
# engine = create_engine(DATABASE_URL, echo=True, future=True, **engine_kwargs)
engine = create_engine(DATABASE_URL, echo=False, future=True, **engine_kwargs)

# autoflush=False: no manda cambios solos; hay que flush() o commit().
# autocommit=False: hay que llamar db.commit() para guardar.
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=Session)


# Base no es un modelo de Pydantic. Es la madre de las tablas de SQLAlchemy.
class Base(DeclarativeBase):
    pass


# Módulo 16 del curso. Comparación SQLAlchemy vs SQLModel. No cambia el código
# de arriba: este proyecto sigue con SQLAlchemy. SQLModel no está instalado.
#
# SQLAlchemy (lo que usa este archivo: create_engine, Session, DeclarativeBase):
#   - ORM maduro y muy usado. Modelos declarativos (la clase Base de arriba).
#   - Sirve como ORM y también como SQL puro (el Core: select, join, text).
#   - Comunidad grande, estable, y habla con casi cualquier base.
#   - Cuesta más configuración y más código. La curva es más alta al empezar.
#   La diapositiva separa la tabla del JSON:
#     class UserORM(Base):          __tablename__, Mapped, mapped_column
#     class UserSchema(BaseModel):  el DTO, otro archivo, con Pydantic
#   Acá es igual: la tabla vive en app/models/ y el JSON en api/v1/.../schemas.py.
#   La diapositiva arma Base con declarative_base(). Este archivo usa
#   class Base(DeclarativeBase), que es la forma actual de SQLAlchemy 2.
#
# SQLModel (paquete sqlmodel, de Sebastián Ramírez, el autor de FastAPI):
#   - Junta el ORM de SQLAlchemy con Pydantic en la misma clase.
#   - Tipado con type hints. Menos código. Una clase sirve de tabla y de validación.
#   - Más cómodo para un proyecto nuevo y chico.
#   - Menos control fino que SQLAlchemy, y menos comunidad y documentación.
#   La diapositiva lo muestra así, y dice que no hace falta una segunda clase:
#     from sqlmodel import SQLModel, Field
#     class User(SQLModel, table=True):
#         id: int | None = Field(default=None, primary_key=True)
#         name: str
#         email: str
#
# Diferencias que marca el módulo:
#   Propósito     SQLAlchemy: toolkit completo de SQL y ORM.
#                 SQLModel: el ORM simplificado para APIs con FastAPI.
#   Base          SQLAlchemy: SQLAlchemy + Declarative.
#                 SQLModel: SQLAlchemy ORM + modelos de Pydantic.
#   Validación    SQLAlchemy: el DTO va aparte (Pydantic).
#                 SQLModel: la misma clase valida y es la tabla.
#   Control       SQLAlchemy: Core, ORM y SQL nativo.
#                 SQLModel: menos control del detalle.
#
# Ejemplo de carpetas de un proyecto con SQLModel (la diapositiva "Estructura
# del proyecto"). Es el mismo recorrido de capas que este repo. Cambia el
# agrupado: la clase junta por tipo de archivo; acá se junta por recurso.
#
#   app/
#     main.py                         arma la app e incluye los routers
#     core/
#       db.py                         engine y sesión. Este mismo archivo.
#     models/
#       note.py                       la tabla. Con SQLModel, note.py también
#                                     valida el JSON (no hay schemas.py aparte).
#     repositories/
#       note_repository.py            el SQL. Acá es api/v1/posts/repository.py
#     services/
#       note_service.py               commit, 404, reglas. Acá es service.py
#                                     al lado del router, no en una carpeta global.
#     api/
#       routers/
#         notes_router.py             las rutas. Acá es api/v1/posts/router.py
#     deps.py                         lo que se inyecta con Depends.
#                                     Acá get_db está en este archivo y el
#                                     usuario del token está en core/security.py.
#
# El "..." de la diapositiva es el resto de modelos, con la misma forma
# (un repository, un service y un router por cada uno).
#
# Cuándo elige cada uno el módulo:
#   SQLModel    APIs rápidas, proyectos chicos o de estudio, productividad.
#   SQLAlchemy  sistemas grandes, consultas complejas, librerías empresariales,
#               control fino del SQL.
#
# ¿Pueden convivir?
#   Sí. SQLModel no es otro motor: usa SQLAlchemy por debajo. El engine de
#   este archivo les sirve a los dos, y una tabla de SQLModel se puede consultar
#   con select() de SQLAlchemy. No hace falta otra base ni otro SessionLocal.
#   Lo que no conviene es declarar la misma tabla dos veces (una clase ORM y
#   otra SQLModel). Convivir es: tablas simples con SQLModel y, en el
#   repository, SQLAlchemy cuando la consulta se complica.
#
# Para un FastAPI real que puede crecer, conviene SQLAlchemy.
#   Es lo que ya hace este repo: la fila (models/) no es el JSON (schemas/).
#   UserPublic no lleva hashed_password, PostCreate no es PostORM. Con SQLModel
#   esa diferencia obliga igual a clases extra, que es lo que la diapositiva
#   quería evitar. El propio módulo reserva SQLAlchemy para consultas complejas
#   y control fino. Si más adelante una parte nueva es un CRUD chico, se puede
#   sumar SQLModel al lado sin tirar este engine. La conclusión de la clase va
#   por ahí: SQLModel no reemplaza a SQLAlchemy, lo extiende. Si el proyecto
#   pide más control, se usa SQLAlchemy, que ya está debajo.


# FastAPI llama a get_db en cada request que declara db: Session = Depends(get_db).
# yield entrega la sesión a la ruta. finally cierra la sesión aunque la ruta falle.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
