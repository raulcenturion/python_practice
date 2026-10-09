# Marca la carpeta app/ como paquete de Python.
# Desde la carpeta fastapi/ se puede escribir: from app.main import app
#
# __init__.py que sí hacen falta:
#   app/__init__.py         este archivo: el paquete y el mapa de la arquitectura.
#   app/models/__init__.py  reexporta las tablas. repository.py hace
#                           from app.models import PostORM, AuthorORM, TagORM
#                           y al importarlas registra las relaciones de SQLAlchemy.
# api/, api/v1/, posts/ y core/ no tienen __init__.py. Nadie importa "la carpeta":
# se importa el módulo concreto (app.core.db, app.api.v1.posts.router).
#
# --- Arquitectura por capas en FastAPI ---
#
# Estructura recomendada:
# app/
#   api/v1/posts/
#       router.py      → Define los endpoints (rutas de la API).
#       service.py     → Completa la operación: transacción, 404/409/500, páginas.
#       schemas.py     → Valida y estructura datos de entrada/salida (DTOs con Pydantic).
#       repository.py  → Encapsula consultas y operaciones en la base de datos.
#
#   core/db.py         → Configuración de la conexión a la base de datos (engine, sesión).
#   core/security.py   → Sección 8. Firma el JWT, lo verifica y devuelve el usuario actual.
#
#   api/v1/auth/
#       router.py      → POST /login y GET /me. Usuarios de práctica en FAKE_USERS.
#       schemas.py     → Token, TokenData y UserPublic (el JSON, no la tabla).
#
#   api/v1/uploads/router.py → Sección 10. Recibir un archivo (bytes, UploadFile o guardarlo).
#   services/file_storage.py → Escribe la imagen en app/media y devuelve /media/<nombre>.
#   main.py monta esa carpeta con StaticFiles para poder abrir la imagen en el navegador.
#
#   models/            → Modelos declarativos de SQLAlchemy (tablas y relaciones).
#       post.py, author.py, tag.py
#
#   main.py            → Punto de entrada de la aplicación, monta los routers.
#
# Responsabilidades:
# - Router: recibe la petición HTTP, valida con schemas y delega al servicio.
# - Service: arma la operación, hace commit o rollback y traduce los errores de la base a HTTP.
# - Schemas: garantizan que los datos cumplan con tipos y restricciones, tanto en requests como en responses.
# - Repository: maneja las consultas y operaciones en la base de datos, aislando la lógica de acceso a datos.
# - Models: representan las tablas de la base de datos en forma de clases Python.
# - Core: configura la infraestructura (DB, seguridad, middlewares).
#   La seguridad de la sección 8 está en core/security.py.
#
# Beneficios de este formato:
# - Separación de responsabilidades → cada capa cumple un rol claro.
# - Escalabilidad → fácil agregar nuevas entidades o módulos sin romper la estructura.
# - Mantenibilidad → el código es más limpio y entendible.
# - Testabilidad → se pueden probar servicios y repositorios de forma aislada.
# - Flexibilidad → si cambia el motor de base de datos (SQL Server, Oracle, PostgreSQL), solo se ajusta el repository/core.
#
# Cómo viaja un request en ESTE proyecto (POST /posts):
#   1. main.py incluye el router. La URL /posts la atiende router.py.
#   2. FastAPI lee el JSON y lo valida con PostCreate (schemas.py, Pydantic).
#      Si no cumple (título con "spam", email inválido), responde 422 y no llega al servicio.
#   3. Depends(get_db) abre una Session. get_db vive en core/db.py. Eso se queda en el router:
#      abrir y cerrar la sesión es parte del request.
#   4. Antes de la función, Depends(get_current_user) lee el header Authorization.
#      Sin token, o con un token vencido o mal firmado, responde 401 y no sigue.
#      El router llama a PostService(db).create_post(post, user). El user sale del token.
#   5. El servicio le pide el INSERT a PostRepository. El repository usa
#      PostORM, AuthorORM y TagORM (models/). No hace commit.
#   6. El servicio hace commit. Si el título ya existe, la base lanza IntegrityError,
#      el servicio hace rollback y responde 409. Un 500 sale del mismo archivo.
#   7. FastAPI convierte el PostORM a PostPublic (schema de salida) y cierra la sesión
#      en el finally de get_db.
#
#   Antes, los pasos 4, 5 y 6 los hacía el router directo contra el repository.
#   El commit y el 409 vivían en router.py. Se comentó ahí y se mudó a service.py
#   para que la ruta solo reciba HTTP y la operación quede en una capa propia.
#
# Quién puede importar a quién (las flechas no se cruzan al revés):
#   router → schemas, service, core.db
#   service → repository, schemas
#   repository → models
#   models → core.db (solo la clase Base)
#   core no importa routers ni models de negocio
#   schemas no importa la base: un schema no sabe si atrás hay SQLite o Postgres
#
# El servicio ya está: app/api/v1/posts/service.py.
# Recorrido: router → service → repository → models.
# El servicio lanza HTTPException para el 404, el 409 y el 500. El 201 y el 204
# siguen en el decorador de router.py, porque son el contrato de la ruta.
#
# --- Así estaba escrito antes de agregar service.py. Quedó como registro. ---
# Capa que esta app todavía no tiene: el servicio (service.py).
# Hoy el router llama al repository directo. El commit y el rollback están en el router.
# Un service iría en el medio cuando aparezcan reglas que no son ni HTTP ni SQL
# (por ejemplo armar un post, avisar por mail y escribir en dos tablas en la misma operación).
# Las rutas quedarían: router → service → repository → models.
#
# Otras piezas de esta carpeta fastapi/, fuera de app/:
#   00_*.py         prácticas sueltas, no usan esta arquitectura.
#   blog_api.py     el mismo blog en un solo archivo. Quedó de histórico, antes del corte en capas.
#   request_test.py sección 9. Ejemplo comentado: varios GET a la vez para ver
#                   sync (time.sleep) frente a async (await asyncio.sleep).
#                   Las rutas /sync y /async están comentadas en posts/router.py.
#   .env            DATABASE_URL. Lo lee core/db.py con python-dotenv. No se sube al repo.
#
# api/v1/ es la versión 1. Otra versión sería api/v2/ con sus propios routers,
# sin borrar v1. Cada recurso (posts, y más adelante authors o tags) es su propia carpeta
# con router, service, schemas y repository.
