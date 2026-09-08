# ============================
# 📝 Ejercicios: Modelos de datos (Pydantic)
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

from dataclasses import dataclass

from pydantic import BaseModel, EmailStr, Field, ValidationError


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

print("Resultado ejercicio 1:")


@dataclass
class LibroDC:
    titulo: str
    anio: int
    leido: bool = False


print(LibroDC("El principito", 1943, True))

# Ejercicio 2: BaseModel
# Con Pydantic, creá class Libro(BaseModel) con los mismos campos.
# Creá una instancia y mostrá model_dump().

print("Resultado ejercicio 2:")


class Libro(BaseModel):
    titulo: str
    anio: int
    leido: bool = False


print(Libro(titulo="El principito", anio=1943, leido=True).model_dump())

# Ejercicio 3: Validación
# Agregá Field(ge=0) al año (o validá anio >= 0).
# Intentá crear Libro(titulo="X", anio=-1) y capturá ValidationError.

print("Resultado ejercicio 3:")


class LibroValidado(BaseModel):
    titulo: str
    anio: int = Field(ge=0)
    leido: bool = False


try:
    LibroValidado(titulo="X", anio=-1)
    print("No se lanzó ValidationError")
except ValidationError as e:
    print(e)

# Ejercicio 4: Desde dict (como body de API)
# Dado payload = {"titulo": "Dune", "anio": "1965", "leido": False}
# Usá model_validate(payload) e imprimí el modelo.
# (Pydantic debería coerciónar "1965" → int)

print("Resultado ejercicio 4:")
payload = {"titulo": "Dune", "anio": "1965", "leido": False}
print(Libro.model_validate(payload))

# Ejercicio 5: Respuesta estilo FastAPI
# Creá class UsuarioOut(BaseModel) con id: int, nombre: str.
# Escribí una función (puede ser sync) create_user(nombre: str) -> UsuarioOut
# que retorne UsuarioOut(id=1, nombre=nombre).
# Imprimí el resultado como dict con model_dump().

print("Resultado ejercicio 5:")


class UsuarioOut(BaseModel):
    id: int
    nombre: str


def create_user(nombre: str) -> UsuarioOut:
    return UsuarioOut(id=1, nombre=nombre)


print(create_user("Juan").model_dump())

# Extra: EmailStr (requiere: pip install 'pydantic[email]')
print("Resultado extra EmailStr:")


class UsuarioIn(BaseModel):
    nombre: str
    email: EmailStr


usuario = UsuarioIn(nombre="Juan", email="juan@example.com")
print(usuario.model_dump())
