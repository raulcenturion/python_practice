# Modulos en Python
# Un módulo es un archivo que contiene definiciones y declaraciones de Python. Los módulos permiten organizar el código en partes reutilizables y manejables.
# Crear un módulo
# Para crear un módulo, simplemente crea un archivo con extensión .py. Por ejemplo, crea un archivo llamado mi_modulo.py con el siguiente contenido:
# mi_modulo.py
def saludar(nombre):
    return f"¡Hola, {nombre}!"
def despedir(nombre):
    return f"¡Adiós, {nombre}!"
# Importar un módulo
# Puedes importar un módulo utilizando la palabra clave import.
# Ejemplo:
#import mi_modulo
#print(mi_modulo.saludar("Alice"))
#print(mi_modulo.despedir("Bob"))
# Importar funciones específicas de un módulo
# Puedes importar funciones específicas de un módulo utilizando la palabra clave from ... import ...
#from mi_modulo import saludar
print(saludar("Charlie"))
# Alias para módulos o funciones
# Puedes asignar un alias a un módulo o función utilizando la palabra clave as.
#import mi_modulo as mm
#print(mm.despedir("David"))
#from mi_modulo import saludar as sal
#print(sal("Eve"))
# Módulos estándar de Python
# Python viene con una biblioteca estándar que incluye muchos módulos útiles, como math, os, sys, datetime, entre otros.
import math
print("Valor de pi:", math.pi)
print("Raíz cuadrada de 16:", math.sqrt(16))
import datetime
hoy = datetime.date.today()
print("Fecha de hoy:", hoy)
# Crear paquetes
# Un paquete es una colección de módulos organizados en un directorio. Para crear un paquete, crea un directorio con un archivo __init__.py (puede estar vacío) y coloca los módulos dentro de ese directorio.
# Estructura del paquete:
# mi_paquete/
# ├── __init__.py
# ├── modulo1.py
# └── modulo2.py
# Importar desde un paquete
# Puedes importar módulos desde un paquete utilizando la sintaxis de puntos.
# Ejemplo:
# from mi_paquete import modulo1
# from mi_paquete.modulo2 import funcion_especifica
# Nota: Asegúrate de que el directorio que contiene el paquete esté en la variable de entorno PYTHONPATH o en el mismo directorio desde donde ejecutas el script.
# Módulos personalizados
# Puedes crear tus propios módulos y paquetes para organizar tu código. Simplemente crea archivos .py y directorios según sea necesario.
# Buenas prácticas
# - Usa nombres descriptivos para tus módulos y funciones.
# - Mantén tus módulos enfocados en una sola responsabilidad.   
# - Documenta tus módulos y funciones con docstrings.
# - Evita la importación circular entre módulos.    
# - Usa entornos virtuales para gestionar dependencias de proyectos.
# - Utiliza herramientas como pip para instalar y gestionar paquetes de terceros.
# - Considera usar herramientas como virtualenv o conda para crear entornos aislados para tus proyectos.
# - Usa herramientas como pylint o flake8 para mantener la calidad del código en    tus módulos.
# - Usa herramientas como Sphinx para generar documentación automática de tus módulos y paquetes.
# - Familiarízate con PyPI (Python Package Index) para descubrir y utilizar paquetes de terceros.
# - Usa herramientas como setuptools o poetry para empaquetar y distribuir tus módulos y paquetes.
# - Mantén tus módulos y paquetes actualizados con las últimas versiones de Python y las dependencias que utilizan.
# - Considera usar herramientas como tox para automatizar pruebas en múltiples entornos de Python.
# - Usa herramientas como mypy para añadir tipado estático a tus módulos y paquetes.
# - Usa herramientas como black o autopep8 para formatear automáticamente tu código según las convenciones de estilo de Python (PEP 8).
# - Considera usar herramientas como coverage.py para medir la cobertura de pruebas de tus módulos y paquetes.
# - Usa herramientas como pre-commit para automatizar tareas de calidad de código antes de cada commit.
# - Familiarízate con las convenciones de nombres y estructura de proyectos en Python para mantener la coherencia en tus módulos y paquetes.
# - Considera usar herramientas como pipenv para gestionar dependencias y entornos virtual  es de manera más sencilla.
# - Usa herramientas como bandit para analizar la seguridad de tu código y detectar posibles vulnerabilidades.
# - Mantén una buena documentación y ejemplos de uso para tus módulos y paquetes, facilitando su adopción por parte de otros desarrolladores.
# - Participa en la comunidad de Python para aprender y compartir buenas prácticas sobre el uso de módulos y paquetes.
# Fin de la clase sobre módulos
