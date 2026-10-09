# Sección 10. Tres formas de recibir un archivo, separadas del blog.
#   POST /upload/bytes  → FastAPI lee todo y entrega bytes.
#   POST /upload/file   → entrega un UploadFile, sin guardarlo.
#   POST /upload/save   → lo guarda en app/media y devuelve la URL.
#
# File        → FastAPI. Marca el parámetro como archivo del formulario.
# UploadFile  → el archivo con nombre, content_type y un file para leerlo.
# File(...)   → obligatorio. Si no viene el campo, responde 422.
#
# La clase declara estas funciones async. No hay await: la lectura y el disco
# son llamadas normales. Quedan como def, igual que get_current_user.
# La clase también importa os, shutil y uuid acá. No se usan: el guardado
# está en app/services/file_storage.py. MEDIA_DIR de la clase tampoco se usa
# en este archivo; lo usa file_storage.

from app.services.file_storage import save_uploaded_image

from fastapi import APIRouter, File, UploadFile

# prefix="/upload" → las rutas de abajo quedan /upload/bytes, /upload/file, /upload/save.
router = APIRouter(prefix="/upload", tags=["uploads"])


@router.post("/bytes")
def upload_bytes(file: bytes = File(...)):
    # bytes = File(...) hace que FastAPI lea el archivo entero en memoria.
    # Sirve para ver el tamaño. Con un archivo grande, ocupa toda esa RAM.
    return {
        "filename": "archivo_subido",
        "size_bytes": len(file),
    }


@router.post("/file")
def upload_file(file: UploadFile = File(...)):
    # UploadFile no lee el contenido todavía. Solo muestra lo que dijo el cliente.
    return {
        "filename": file.filename,
        "content_type": file.content_type,
    }


@router.post("/save")
def save_file(file: UploadFile = File(...)):
    # save_uploaded_image escribe el archivo y arma la URL /media/...
    saved = save_uploaded_image(file)

    return {
        "filename": saved["filename"],
        # La clase escribe la clave "conten_type" (le falta la t). El valor
        # correcto es content_type, que es lo que devuelve file_storage.
        "content_type": saved["content_type"],
        "url": saved["url"],
        # "size": saved["size"],
        # "chunk_size_used": saved["chunk_size_used"],
        # "chunk_calls": saved["chunk_calls"],
        # "chunk_sizes_sample": saved["chunk_sizes_sample"],
    }
