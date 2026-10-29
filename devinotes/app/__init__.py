# Devinote. App aparte de fastapi/.
# Capas, librerías y la diferencia con el blog: ESTRUCTURA.md, en la raíz del repo.
# Sección 16: core, models y repositories. Arma las tablas.
# Sección 17: services, routers y main.py. La API HTTP.
# Sección 18: Alembic. create_all queda comentado.
# Sección 19: deploy. postgres:// pasa a postgresql+psycopg://.
#   En el servidor el proceso es gunicorn. El comando está en app/core/db.py.
#
# Desde esta carpeta (devinotes/), no desde la raíz del repo.
# El paquete se llama app, igual que fastapi/app.
#
#   source ../.venv/bin/activate
#   python -m app
#     ya no crea tablas. init_db quedó en pass en la sección 18.
#   alembic upgrade head
#     crea o actualiza devinotes.db. El resto de los comandos, qué es Alembic
#     y cuándo sirve, está en app/core/db.py.
#   ../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8001
#     Los comandos de las tres apps están en el README de la raíz, "Cómo levantar".
#     API en el 8001. El blog sigue en el 8000.
#     Swagger: http://127.0.0.1:8001/docs
#     Antes, upgrade head: el servidor ya no llama a create_all.
