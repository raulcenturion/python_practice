# Webhooks. App aparte de fastapi/, devinotes/ y websocket/.
# Repo: ricardocuellar/Devtalles-Fastapi-Webhooks.
# La clase deja este archivo vacío. Estas líneas son cómo se corre.
#
# Un webhook es al revés de una consulta. Nosotros no le preguntamos a GitHub
# si hay issues nuevos. GitHub hace un POST a nuestra URL cuando se abre uno.
# La firma HMAC (X-Hub-Signature-256) demuestra que quien llama conoce el secreto.
# Discord va al revés: nosotros hacemos el POST a la URL del canal.
#
# El paquete se llama app, igual que fastapi/app y devinotes/app.
# Hay que correr desde esta carpeta (webhooks/), no desde la raíz.
# Desde la raíz, Python no encuentra este app, o puede agarrar otro.
#
#   ../.venv/bin/python -m uvicorn app.main:app --host 127.0.0.1 --port 8004
#   Swagger: http://127.0.0.1:8004/docs
#   POST /webhooks/github   lo llama GitHub
#   GET  /issues            lo que se guardó
#
# El comando, el curl firmado y el de Discord están en el README de la raíz,
# sección "Cómo levantar". El blog sigue en el 8000, Devinote en el 8001,
# el chat en el 8002 y el eco en el 8003.
#
# El requirements.txt de la clase fija fastapi 0.135, SQLAlchemy 2.0.48 y
# sqlmodel 0.0.37. No se instala: bajaría el venv de este repo.
# Esta app usa fastapi, sqlmodel, httpx y python-dotenv, que ya están.
