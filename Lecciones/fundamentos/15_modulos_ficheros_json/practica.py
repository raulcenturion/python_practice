# ============================
# 📝 Ejercicios: Módulos, Ficheros, JSON
# 📘 Teoría: teoria_ficheros.py, teoria_json_xml.py, teoria_modulos.py (misma carpeta)
# ============================

import json
import math
from datetime import datetime, timezone

# 🔸 Ejemplo:
data = {"nombre": "Raúl", "edad": 33}
json_str = json.dumps(data, indent=2)
print(json_str)

# ============================
# MÓDULOS
# ============================

# Ejercicio 1: Módulo math
# Importá math y calculá: raíz cuadrada de 144, valor de pi, y 2 elevado a la 10.
print("Ejercicio 1: Módulo math")
print(math.sqrt(144))
print(math.pi)
print(math.pow(2, 10))


# Ejercicio 2: Módulo datetime
# Importá datetime y mostrá: la fecha de hoy, la hora actual, y el día de la semana.
print("Ejercicio 2: Módulo datetime")
ahora = datetime.now(timezone.utc)
print(ahora)  # fecha y hora (UTC)
print(ahora.hour)  # hora actual
print(ahora.strftime("%A"))  # día de la semana (nombre)


# ============================
# FICHEROS
# ============================

# Ejercicio 3: Escribir y leer
# Escribí 3 líneas en un archivo "notas.txt" (modo "w").
# Después leélas línea por línea e imprimí cada una.
print("Ejercicio 3: Escribir y leer")
with open("notas1.txt", "w") as file:
    file.write("Línea 1\n")
    file.write("Línea 2\n")
    file.write("Línea 3\n")
with open("notas1.txt", "r") as file:
    for linea in file:
        print(linea.strip())


# Ejercicio 4: Agregar contenido
# Agregá una línea más al archivo "notas.txt" (modo "a").
# Leé todo el contenido y mostralo.
print("Ejercicio 4: Agregar contenido")
with open("notas.txt", "a") as file:
    file.write("Línea 4\n")
with open("notas.txt", "r") as file:
    print(file.read())


# ============================
# JSON
# ============================

# Ejercicio 5: Dict a JSON
# Creá un diccionario con tus datos. Convertilo a JSON con json.dumps().
# Guardalo en un archivo "perfil.json" con json.dump().
print("Ejercicio 5: Dict a JSON")
datos = {"nombre": "Juan", "edad": 25}
json_str = json.dumps(datos, indent=2)
with open("perfil.json", "w") as file:
    file.write(json_str)


# Ejercicio 6: JSON a Dict
# Leé el archivo "perfil.json" y convertilo de vuelta a diccionario con json.load().
# Imprimí el nombre y el tipo del resultado.
print("Ejercicio 6: JSON a Dict")
with open("perfil.json", "r") as file:
    datos = json.load(file)
    print(datos["nombre"])
    print(type(datos))
