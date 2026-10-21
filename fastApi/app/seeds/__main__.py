# Sección 14. Este archivo corre cuando ejecutás el paquete como módulo.
#
# Desde la carpeta fastapi/, con el venv del repo activo:
#   python3 -m app.seeds all
#
# -m le dice a Python que ejecute un módulo, no un archivo suelto.
# app.seeds es este paquete. Al usar -m, Python entra a __main__.py.
# El argumento all es un comando de typer (run.py): carga las tres listas.
#
# Sirve para no crear a mano el admin, las categorías y las etiquetas.
# Se puede correr más de una vez: si el email, el slug o el tag ya están,
# no inserta otra fila.
#
# Otros comandos, mismo lugar:
#   python3 -m app.seeds users
#   python3 -m app.seeds categories
#   python3 -m app.seeds tags
#
# Hay que pararse en fastapi/. Desde la raíz del repo, Python confunde
# la carpeta fastapi/ con el paquete instalado fastapi y app.seeds no se encuentra.

from .run import app

if __name__ == "__main__":
    # app es el Typer de run.py. app() lee el argumento (all, users, ...) y llama.
    app()
