# ============================
# 📝 Ejercicios: Módulos, Ficheros, JSON
# 📘 Teoría: Clases_teoria/fundamentos/17_modulos.py + 20_ficheros.py + 21_json_xml.py
# ============================

# 🔸 Ejemplo:
import json

data = {"nombre": "Raúl", "edad": 33}
json_str = json.dumps(data, indent=2)
print(json_str)

# ============================
# MÓDULOS
# ============================

# Ejercicio 1: Módulo math
# Importá math y calculá: raíz cuadrada de 144, valor de pi, y 2 elevado a la 10.


# Ejercicio 2: Módulo datetime
# Importá datetime y mostrá: la fecha de hoy, la hora actual, y el día de la semana.


# ============================
# FICHEROS
# ============================

# Ejercicio 3: Escribir y leer
# Escribí 3 líneas en un archivo "notas.txt" (modo "w").
# Después leélas línea por línea e imprimí cada una.


# Ejercicio 4: Agregar contenido
# Agregá una línea más al archivo "notas.txt" (modo "a").
# Leé todo el contenido y mostralo.


# ============================
# JSON
# ============================

# Ejercicio 5: Dict a JSON
# Creá un diccionario con tus datos. Convertilo a JSON con json.dumps().
# Guardalo en un archivo "perfil.json" con json.dump().


# Ejercicio 6: JSON a Dict
# Leé el archivo "perfil.json" y convertilo de vuelta a diccionario con json.load().
# Imprimí el nombre y el tipo del resultado.

