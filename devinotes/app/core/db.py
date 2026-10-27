# Motor y sesión de Devinote. Sección 16.
#
# typing.Iterator     → biblioteca estándar. get_session es un generador:
#                       yield entrega la sesión y el with la cierra.
# sqlmodel.SQLModel   → paquete sqlmodel. La clase madre de las tablas.
#                       metadata junta todas las que heredan de SQLModel.
# sqlmodel.Session    → la charla con la base. Es la Session de SQLAlchemy,
#                       con exec() en vez de execute() para las consultas del ORM.
# sqlmodel.create_engine
#                     → el mismo create_engine de SQLAlchemy. Abre la base
#                       a partir de la URL (sqlite, postgres, ...).

from collections.abc import Iterator

from sqlmodel import Session, create_engine

# from sqlmodel import SQLModel
# La sección 16 usaba SQLModel.metadata.create_all(engine) en init_db.
from app.core.config import settings


# Sección 19. Render y Heroku entregan la URL como postgres://.
# SQLAlchemy, con el driver psycopg 3, no abre ese esquema: el driver va
# en la URL, postgresql+psycopg://. postgresql:// pelado es el driver viejo.
# La clase lo copia en este archivo y otra vez en alembic/env.py, y lee
# os.environ["DATABASE_URL"]. Si la variable no está, eso es un KeyError
# y se pierde el default sqlite de Settings. Acá se normaliza una sola vez
# y env.py llama a esta función.
def normalize_database_url(raw_url: str) -> str:
    postgres = "postgres://"
    postgresql = "postgresql://"
    with_driver = "postgresql+psycopg://"
    if raw_url.startswith(postgres):
        return with_driver + raw_url.removeprefix(postgres)
    if raw_url.startswith(postgresql) and "+psycopg" not in raw_url:
        return with_driver + raw_url.removeprefix(postgresql)
    return raw_url


database_url = normalize_database_url(settings.DATABASE_URL)

# echo=False no imprime el SQL. La clase lo deja así.
# pool_pre_ping=True pregunta si la conexión sigue viva antes de usarla.
# En un servidor el host cierra las que quedan ociosas. La sección 19 lo agrega.
# check_same_thread=False solo en SQLite: FastAPI puede usar la conexión
# en otro hilo, y SQLite por defecto lo prohíbe. En Postgres el dict queda vacío.
# La clase comenta este create_engine y deja solo:
#   engine = create_engine(url, pool_pre_ping=True)
# En local la base sigue siendo SQLite, así que el connect_args se queda.
engine = create_engine(
    database_url,
    echo=False,
    pool_pre_ping=True,
    connect_args={"check_same_thread": False} if "sqlite" in database_url else {},
)


def init_db() -> None:
    # Sección 16: sin importar los modelos, metadata está vacío y create_all
    # no crea nada. import app.models registra user, note, label y share.
    # import app.models
    # if settings.ENVIRONMENT == "DEV":
    #     SQLModel.metadata.create_all(engine)
    #
    # Sección 18: la clase deja ese bloque comentado y esta función en pass.
    # create_all crea tablas que faltan y no cambia una que ya existe.
    # Agregar user.active sobre un devinotes.db viejo no haría nada.
    # Eso lo hace Alembic. Comandos y para qué sirve: el bloque de abajo.
    pass


# Sección 18. Alembic en Devinote.
#
# Alembic versiona el esquema de la base. Cada cambio queda en un archivo
# de alembic/versions/ con upgrade() (aplicar) y downgrade() (deshacer).
# Alembic anota en la tabla alembic_version hasta qué revisión llegó esta base.
#
# Sirve cuando la base ya tiene datos y el modelo cambió:
#   - una columna nueva (user.active, la segunda revisión de esta sección)
#   - un índice, una unique, un tipo, una tabla nueva al lado de las viejas
#   - el mismo cambio en otra máquina: se commitea el archivo y el otro
#     corre upgrade head, sin copiar el .db
#   - producción: el proceso que atiende HTTP no crea ni altera tablas al arrancar
#
# create_all no reemplaza eso. Crea lo que falta y deja quieta la tabla que
# ya está. No agrega active, no renombra un constraint, no se puede deshacer.
# Si la base es de prueba y se puede borrar el .db, create_all alcanza.
# En cuanto hay filas que querés conservar, Alembic es el camino.
#
# Paquete: alembic (instala Mako, el motor de la plantilla script.py.mako).
# El venv es el de la raíz del repo, no una carpeta venv/ adentro de devinotes/.
# Todo se corre parado en devinotes/. Desde la raíz, `app` es el blog.
# Si la terminal tiene DATABASE_URL del blog, Alembic usa esa base.
# Para Devinote no exportes esa variable, o apuntála a sqlite:///./devinotes.db.
# El .db y el .env no se commitean.
#
# Arranque, una sola vez (la clase, captura de `alembic init alembic`):
#   cd devinotes
#   source ../.venv/bin/activate
#   alembic init alembic
# Crea alembic/, alembic/versions/, script.py.mako, env.py, README y alembic.ini.
# El comando avisa que hay que editar alembic.ini antes de seguir.
# En este repo eso ya está: env.py lee settings.DATABASE_URL y el ini
# deja sqlalchemy.url comentado.
#
# Atajos, siempre desde devinotes/:
#   alembic revision --autogenerate -m "add field active to User"
#       Compara los modelos contra la base y escribe una revisión nueva.
#       Hay que leer el archivo: autogenerate no adivina renombres ni datos.
#   alembic upgrade head
#       Aplica todas las revisiones que faltan. Es el comando de todos los días.
#   alembic upgrade +1
#       Solo la siguiente.
#   alembic downgrade -1
#       Deshace la última (corre downgrade() de esa revisión).
#   alembic downgrade base
#       Deshace todas.
#   alembic current
#       Qué revisión tiene esta base.
#   alembic history
#       La cadena de revisiones, de la primera a la última.
#   alembic upgrade head --sql
#       Imprime el SQL y no toca la base.
#
# Revisiones ya escritas, en este orden:
#   0bd823c6c863  init schema          crea user, note, label y las de share
#   fa5e26298a8d  add field active     agrega user.active
# No hace falta volver a autogenerar esas dos.
#
# Si devinotes.db se creó antes, con create_all, upgrade head falla:
# las tablas ya existen y no hay alembic_version. Ese archivo es local.
# Se borra y se corre upgrade head. No pisa blog.db.
#
# Sección 19. Deploy.
# En la máquina local el proceso es uvicorn, un solo proceso, y la base es SQLite.
# En un servidor la base es Postgres y el proceso que escucha es gunicorn:
# abre varios workers y cada worker corre la app de uvicorn.
# Antes de escuchar hay que aplicar las migraciones. El host inyecta PORT
# y DATABASE_URL. Esa URL suele llegar como postgres://; normalize_database_url
# la pasa a postgresql+psycopg://, que es el driver psycopg 3.
#
#   cd devinotes
#   alembic upgrade head
#   gunicorn app.main:app \
#     --worker-class uvicorn.workers.UvicornWorker \
#     --bind 0.0.0.0:$PORT
#
# La clase agrega gunicorn al requirements, sin versión. Acá queda pinneado.
# No hace falta levantarlo para estudiar: en local sigue uvicorn en el 8001.


def get_session() -> Iterator[Session]:
    # with cierra la sesión al salir, también si la ruta falla.
    # api/deps.py hace yield from get_session() para que el with dure el request.
    # exec() de esta Session ya devuelve ScalarResult: no se le encadena .scalars().
    with Session(engine) as session:
        yield session
