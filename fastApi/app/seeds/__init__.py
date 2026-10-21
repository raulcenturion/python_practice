# Marca seeds/ como paquete, para que funcione: python3 -m app.seeds
# La clase reexporta el Typer. Así `from app.seeds import app` también lo encuentra.
from .run import app

__all__ = ["app"]
