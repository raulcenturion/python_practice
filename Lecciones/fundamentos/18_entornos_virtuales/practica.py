# ============================
# 📝 Ejercicios: Entornos virtuales y dependencias
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import os
import sys

# --- Módulos estándar en Python ---
#
# import os → módulo para interactuar con el sistema operativo.
#   - os.getcwd() → directorio actual.
#   - os.listdir() → lista archivos en un directorio.
#   - os.remove("archivo.txt") → elimina un archivo.
#   - os.environ → variables de entorno.
#
# import sys → módulo para interactuar con el intérprete de Python.
#   - sys.argv → argumentos pasados por línea de comandos.
#   - sys.exit() → termina el programa.
#   - sys.version → versión de Python en uso.
#   - sys.stdout / sys.stdin → salida y entrada estándar.
#
# --- Conceptos ---
# - Ambos son parte de la biblioteca estándar de Python (no requieren instalación).
# - Se usan para tareas de bajo nivel: sistema operativo (os) y entorno del intérprete (sys).
# - Documentación oficial: Python Standard Library.


# 🔸 Ejemplo:
print("Python:", sys.executable)
print("¿venv activo?:", sys.prefix != getattr(sys, "base_prefix", sys.prefix))

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Crear venv
# En la terminal, desde la raíz del repo:
#   python3 -m venv .venv
# Verificá que exista la carpeta .venv/
print("Resultado ejercicio 1:")
print(os.path.exists('.venv'))


# Ejercicio 2: Activar
# Activá el entorno:
#   source .venv/bin/activate
# Confirmá que el prompt muestra (.venv)
print("Resultado ejercicio 2:")
print(sys.prefix)


# Ejercicio 3: Instalar y listar
# Con el venv activo:
#   pip install requests
#   pip list
# Anotá si aparece requests.
print("Resultado ejercicio 3:")
print(os.listdir())


# Ejercicio 4: requirements.txt
# Generá/actualizá dependencias:
#   pip freeze > requirements.txt
# Abrí el archivo y confirmá que lista paquetes con versión.
print("Resultado ejercicio 4:")
print(os.path.exists('requirements.txt'))


# Ejercicio 5: Script de verificación
# Completá la función debajo para retornar True si el proceso corre en un venv.
# Imprimí también la ruta de sys.executable.
print("Resultado ejercicio 5:")
print(sys.executable)

def corriendo_en_venv() -> bool:
    return sys.prefix != sys.base_prefix
    


if __name__ == "__main__":
    print("Resultado ejercicio 5:", corriendo_en_venv())

# Ejercicio 6: Reinstalar desde cero (mental / práctico)
# Desactivá (deactivate), borrá .venv (solo si estás seguro),
# recrealo e instalá con:
#   pip install -r requirements.txt
print("Resultado ejercicio 6:")
print(os.listdir())

# --- Ejercicios con venv ---
#
# Ejercicio 1: Crear venv
#   python3 -m venv .venv
#   Verifica existencia con os.path.exists('.venv').
#
# Ejercicio 2: Activar
#   source .venv/bin/activate
#   sys.prefix muestra la ruta del entorno activo.
#
# Ejercicio 3: Instalar y listar
#   pip install requests
#   pip list → muestra paquetes instalados.
#   (No usar os.listdir(), eso lista archivos del directorio).
#
# Ejercicio 4: requirements.txt
#   pip freeze > requirements.txt
#   Verificar archivo con os.path.exists('requirements.txt').
#   (os.listdir espera directorio, no archivo).
#
# Ejercicio 5: Script de verificación
#   sys.executable → ruta del intérprete activo.
#   corriendo_en_venv() → retorna True si sys.prefix != sys.base_prefix.
#   Buenas prácticas: encapsular la lógica en función reutilizable.
#
# Ejercicio 6: Reinstalar desde cero
#   deactivate, borrar .venv, recrear, instalar con pip install -r requirements.txt.
#   os.listdir() → lista archivos del directorio actual.
#
# --- Buenas prácticas ---
# - Usar os.path.exists() para verificar archivos.
# - Usar pip list / pip freeze en terminal para paquetes, no os.listdir().
# - Implementar funciones reutilizables (ej. corriendo_en_venv).
# - Mantener separación entre comandos de terminal y código Python.
