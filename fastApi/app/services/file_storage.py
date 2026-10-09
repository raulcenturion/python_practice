# Sección 10. Guarda una imagen en disco y devuelve la URL para verla.
# Lo usan POST /posts (imagen del post) y POST /upload/save.
#
# os        → biblioteca estándar. Carpetas, nombres y el tamaño del archivo.
# shutil    → biblioteca estándar. copyfileobj copia el archivo por trozos.
# uuid      → biblioteca estándar. Un nombre único para no pisar otro archivo.
# UploadFile → FastAPI. El archivo que llegó en el formulario, no solo los bytes.
# HTTPException, status → FastAPI. 400 si no es imagen, 413 si pesa de más.
#
# La clase también importa APIRouter y File en este archivo. No se usan acá:
# el router de uploads está en api/v1/uploads/router.py.

import os
import shutil
import uuid

from fastapi import HTTPException, UploadFile, status

# Carpeta relativa a donde arrancás el servidor (la carpeta fastapi/).
# El mismo directorio lo publica main.py en la URL /media.
MEDIA_DIR = "app/media"
# El navegador manda este texto en content_type. Solo entran png y jpeg.
ALLOW_MIME = ["image/png", "image/jpeg"]
# Tope en megabytes. Se lee del entorno; si no está, son 3.
MAX_MB = int(os.getenv("MAX_UPLOAD_MB", "3"))
# Un megabyte. copyfileobj lee el archivo de a este tamaño, no entero en memoria.
CHUNKS = 1024 * 1024


def ensure_media_dir() -> None:
    # exist_ok=True: si la carpeta ya existe, no falla.
    os.makedirs(MEDIA_DIR, exist_ok=True)


def save_uploaded_image(file: UploadFile) -> dict:
    # content_type lo declara el cliente. No mira los bytes del archivo.
    if file.content_type not in ALLOW_MIME:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Solo se permiten imágenes PNG o JPEG",
        )

    ensure_media_dir()
    # splitext separa "foto.png" en ("foto", ".png"). Solo guardamos la extensión.
    # La clase usa file.filename directo. Si no viene nombre, es None y revienta.
    # or "" deja la extensión vacía y el archivo se guarda igual.
    ext = os.path.splitext(file.filename or "")[1]
    # uuid4().hex es un nombre aleatorio. No se usa el nombre original:
    # así dos "foto.png" no se pisan y no entra un camino tipo ../.
    filename = f"{uuid.uuid4().hex}{ext}"
    file_path = os.path.join(MEDIA_DIR, filename)

    # La clase deja comentado un contador de trozos, para ver cuántas veces
    # se llama a read y de qué tamaño. No hace falta para guardar el archivo.
    # class _ChunkCounter:
    #     def __init__(self, f):
    #         self._f = f
    #         self.calls = 0
    #         self.sizes = []
    #     def read(self, n=-1):
    #         data = self._f.read(n)
    #         if data:
    #             self.calls += 1
    #             self.sizes.append(len(data))
    #         return data
    #     def __getattr__(self, name):
    #         return getattr(self._f, name)
    # reader = _ChunkCounter(file.file)

    # "wb" = escribir bytes. length=CHUNKS es el tamaño de cada lectura.
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer, length=CHUNKS)

    # El tope se mira después de escribir. Si se pasa, se borra el archivo.
    size = os.path.getsize(file_path)
    if size > MAX_MB * CHUNKS:
        os.remove(file_path)
        raise HTTPException(
            # La clase usa HTTP_413_REQUEST_ENTITY_TOO_LARGE. Ese nombre quedó viejo
            # y el editor avisa. El código actual es HTTP_413_CONTENT_TOO_LARGE: sigue siendo 413.
            status_code=status.HTTP_413_CONTENT_TOO_LARGE,
            detail=f"Archivo demasiado grande (>{MAX_MB} MB)",
        )

    return {
        "filename": filename,
        "content_type": file.content_type,
        # Esta URL la sirve StaticFiles en main.py, no una ruta del router.
        "url": f"/media/{filename}",
        # "size": size,
        # "chunk_size_used": CHUNKS,
        # "chunk_calls": reader.calls,
        # "chunk_sizes_sample": reader.sizes[:5],
    }
