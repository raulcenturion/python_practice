# Sección 15. Middlewares: código que corre en cada request, antes y después de la ruta.
# main.py llama a register_middleware(app) al armar la aplicación.
#
# time                         → biblioteca estándar. Mide cuánto tardó el request.
# uuid                         → biblioteca estándar. Arma un id único por request.
# fastapi.FastAPI              → la aplicación. add_middleware y el decorador viven ahí.
# fastapi.HTTPException        → corta con un status HTTP (acá 403).
# fastapi.Request              → el request que entra: método, URL, IP, headers.
# fastapi.middleware.cors.CORSMiddleware
#                              → paquete fastapi (lo implementa Starlette).
#                                Responde el preflight y agrega Access-Control-Allow-Origin.
#                                Sin esa cabecera el navegador de cors-demo (puerto 3000)
#                                no puede leer la respuesta de esta API (puerto 8000).
#
# La clase importa `from urllib import response`. urllib.response es otra cosa
# (la respuesta de urllib, biblioteca estándar) y en el archivo no se usa.
# El nombre response de abajo es el que devuelve call_next, no ese import.

import time
import uuid

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, HTTPException, Request

# IPs bloqueadas. La clase usa un dict y pregunta `ip in BLACKLIST` (mira las claves).
# Vacío: nadie está bloqueado. Para prohibir una IP se agrega la clave, por ejemplo
# BLACKLIST["203.0.113.5"] = True
BLACKLIST: dict[str, bool] = {}


def register_middleware(app: FastAPI) -> None:
    # El último middleware que se registra es el primero que ve el request.
    # Al salir, el orden se invierte: el primero registrado toca la respuesta al final.
    # Por eso CORS queda registrado primero (adentro) y el bloqueo de IP al final (afuera).

    # Orígenes que el navegador puede usar para llamar a esta API.
    # La clase lista el 5555 y el 5173 (el puerto por defecto de Vite).
    # cors-demo de este repo abre en el 3000, así que esos dos orígenes también entran.
    # allow_credentials=True deja pasar cookies. Con eso no se puede usar allow_origins=["*"]:
    # hay que nombrar cada origen.
    # allow_methods y allow_headers en "*" aceptan cualquier verbo y cualquier header.
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://127.0.0.1:5555",
            "http://localhost:5173",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # async porque hay await call_next: se espera a que la ruta termine.
    # Sin ese await la función no tiene que ser async.
    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        # perf_counter es un reloj para medir intervalos, no la hora del día.
        start = time.perf_counter()
        # call_next sigue la cadena: el resto de middlewares y, al final, la ruta.
        response = await call_next(request)
        process_time = time.perf_counter() - start
        # Header propio. El navegador lo recibe junto con el JSON.
        response.headers["X-Process-Time"] = f"{process_time:.4f} s"
        return response

    @app.middleware("http")
    async def log_request(request: Request, call_next):
        # request.method es GET, POST, ... request.url es la URL completa.
        print(f"**ENTRADA: {request.method} {request.url} **")
        response = await call_next(request)
        print(f"**SALIDA: {response.status_code} **")
        return response

    @app.middleware("http")
    async def add_request_id_header(request: Request, call_next):
        # uuid4 es aleatorio. str() lo deja como texto para el header.
        request_id = str(uuid.uuid4())
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response

    @app.middleware("http")
    async def block_ip_middleware(request: Request, call_next):
        # La clase lee request.client.host directo.
        # client es None cuando el request no trae un socket (algunos tests).
        # En ese caso no hay IP que bloquear y se sigue.
        client_ip = request.client.host if request.client else ""
        if client_ip in BLACKLIST:
            # 403: la IP está en la lista. No se llama a la ruta.
            raise HTTPException(status_code=403, detail="Acceso denegado a esta IP")
        return await call_next(request)
