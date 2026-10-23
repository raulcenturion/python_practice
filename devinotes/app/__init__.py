# Devinote. App aparte de fastapi/.
# Sección 16: core, models y repositories. Arma las tablas.
# Sección 17: services, routers y main.py. La API HTTP.
#
# Desde esta carpeta (devinotes/), no desde la raíz del repo.
# El paquete se llama app, igual que fastapi/app.
#
#   source ../.venv/bin/activate
#   python -m app
#     crea devinotes.db (init_db) sin levantar el servidor.
#   ../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8001
#     API en el 8001. El blog sigue en el 8000.
#     Swagger: http://127.0.0.1:8001/docs
