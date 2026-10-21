# Comandos de la carga inicial. Sección 14.
#
# typer → paquete typer (pip install typer). Arma una mini CLI.
#   @app.command("all") registra la palabra que escribís después del módulo.
#   typer.echo escribe en la terminal, como print, y typer la puede colorear.
# app.seeds.service → las funciones que abren la sesión y escriben en la base.
#
# No es una ruta HTTP. Se usa desde la terminal. Ver el comentario de __main__.py:
#   python3 -m app.seeds all

import typer
from app.seeds.service import run_all, run_categories, run_tags, run_users

# help es el texto de: python3 -m app.seeds --help
app = typer.Typer(help="Seeds: users, categories, tags")


# La función no puede llamarse all: all es una función de Python.
# all_ es el nombre en el archivo. "all" es el nombre del comando.
@app.command("all")
def all_():
    run_all()
    typer.echo("Todos los seeds creados")


@app.command("users")
def users():
    run_users()
    typer.echo("Usuarios cargados")


@app.command("categories")
def categories():
    run_categories()
    typer.echo("Categorias cargadas")


@app.command("tags")
def tags():
    run_tags()
    typer.echo("Etiquetas cargadas")
