# ============================
# 📝 Ejercicios: Modelos de datos (Pydantic)
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

from dataclasses import dataclass


# 🔸 Ejemplo dataclass:
@dataclass
class ProductoDC:
    nombre: str
    precio: float


print(ProductoDC("Teclado", 49.99))

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: dataclass
# Creá una dataclass Libro con: titulo (str), anio (int), leido (bool=False).
# Instanciá un libro e imprimilo.


# Ejercicio 2: BaseModel
# Con Pydantic, creá class Libro(BaseModel) con los mismos campos.
# Creá una instancia y mostrá model_dump().


# Ejercicio 3: Validación
# Agregá Field(ge=0) al año (o validá anio >= 0).
# Intentá crear Libro(titulo="X", anio=-1) y capturá ValidationError.


# Ejercicio 4: Desde dict (como body de API)
# Dado payload = {"titulo": "Dune", "anio": "1965", "leido": False}
# Usá model_validate(payload) e imprimí el modelo.
# (Pydantic debería coerciónar "1965" → int)


# Ejercicio 5: Respuesta estilo FastAPI
# Creá class UsuarioOut(BaseModel) con id: int, nombre: str.
# Escribí una función (puede ser sync) create_user(nombre: str) -> UsuarioOut
# que retorne UsuarioOut(id=1, nombre=nombre).
# Imprimí el resultado como dict con model_dump().


# Requiere: pip install 'pydantic[email]'  (o al menos pydantic)
# from pydantic import BaseModel, Field, ValidationError
