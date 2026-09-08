# ============================
# 📘 JSON y XML en Python
# ============================
# JSON (JavaScript Object Notation): formato ligero de intercambio de datos.
#   - Fácil de leer/escribir para humanos y de parsear para máquinas.
#   - Muy usado en APIs web y configuración.
#   - En Python: módulo stdlib `json`.
#
# XML (eXtensible Markup Language): formato de marcado con etiquetas.
#   - Útil cuando hace falta estructura más rígida o documentos complejos.
#   - Crear/escribir: xml.etree.ElementTree (stdlib).
#   - Parsear de forma segura: defusedxml (evita ataques XXE).
#
# Conversiones clave JSON ↔ Python:
#   dumps / loads  → string JSON ↔ dict/list (en memoria)
#   dump  / load   → archivo JSON ↔ dict/list (en disco)
#
# Path(__file__).parent → archivos se crean junto a esta lección, no en el cwd.

import json
import xml.etree.ElementTree as ET  # crear / escribir XML
from pathlib import Path

import defusedxml.ElementTree as SafeET  # parse seguro (evita XXE)

ENCODING = "utf-8"
# Anclamos rutas a la carpeta de la lección (igual que en teoria_ficheros.py).
DIR = Path(__file__).resolve().parent
ARCHIVO_JSON = DIR / "data.json"
ARCHIVO_XML = DIR / "data.xml"


def cargar_xml(ruta):
    """Carga un XML desde archivo con parser seguro (defusedxml)."""
    # SafeET.parse evita vulnerabilidades XXE del parser XML “clásico”.
    return SafeET.parse(ruta)


# ============================
# 🔹 Diccionario → string JSON (dumps)
# ============================
print("--- Diccionario a JSON (dumps) ---")

# Dict de Python con tipos que JSON entiende: str, int, list, bool, None.
data = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hijos": ["Ana", "Luis"],
    "casado": True,   # en JSON → true
    "mascota": None,  # en JSON → null
}

# dumps = dump string: convierte el dict a un str con formato JSON.
# indent=4 → sangría legible (no cambia el significado de los datos).
json_data = json.dumps(data, indent=4)
print("JSON generado:")
print(json_data)

# ============================
# 🔹 String JSON → diccionario (loads)
# ============================
print("\n--- JSON a diccionario (loads) ---")

# loads = load string: parsea el str JSON y vuelve a un dict de Python.
data_cargada = json.loads(json_data)
print("Diccionario cargado desde JSON:", data_cargada)

# ============================
# 🔹 Guardar JSON en archivo (dump)
# ============================
print("\n--- Guardar JSON en archivo (dump) ---")

# dump (sin s) escribe directo al archivo; no necesitamos el string intermedio.
with open(ARCHIVO_JSON, "w", encoding=ENCODING) as json_file:
    json.dump(data, json_file, indent=4)
print(f"JSON guardado en {ARCHIVO_JSON.name!r}")

# ============================
# 🔹 Cargar JSON desde archivo (load)
# ============================
print("\n--- Cargar JSON desde archivo (load) ---")

# load lee el archivo y lo convierte a dict/list de Python.
with open(ARCHIVO_JSON, "r", encoding=ENCODING) as json_file:
    data_desde_archivo = json.load(json_file)
print(f"Diccionario cargado desde {ARCHIVO_JSON.name!r}:", data_desde_archivo)

# ============================
# 🔹 Crear documento XML (ElementTree)
# ============================
# XML se arma como un árbol: raíz → hijos → texto dentro de cada etiqueta.
print("\n--- Crear documento XML ---")

# Element("persona") crea el nodo raíz <persona>...</persona>
root = ET.Element("persona")
# SubElement agrega un hijo; .text es el contenido entre etiquetas.
nombre = ET.SubElement(root, "nombre")
nombre.text = "Juan"
edad = ET.SubElement(root, "edad")
edad.text = "30"  # en XML el contenido suele ser texto (str)
ciudad = ET.SubElement(root, "ciudad")
ciudad.text = "Madrid"

# tostring serializa el árbol a un string XML (encoding="unicode" → str, no bytes).
xml_data = ET.tostring(root, encoding="unicode")
print("XML generado:", xml_data)

# ============================
# 🔹 Guardar XML en archivo
# ============================
print("\n--- Guardar XML en archivo ---")

# ElementTree envuelve la raíz para poder .write() al disco.
tree = ET.ElementTree(root)
# "wb" + encoding: ElementTree escribe bytes con declaración XML.
with open(ARCHIVO_XML, "wb") as xml_file:
    tree.write(xml_file, encoding=ENCODING, xml_declaration=True)
print(f"XML guardado en {ARCHIVO_XML.name!r}")

# ============================
# 🔹 Cargar XML desde archivo (parser seguro)
# ============================
print("\n--- Cargar XML desde archivo ---")

# Usamos defusedxml (cargar_xml) en lugar de ET.parse para leer de forma segura.
tree = cargar_xml(ARCHIVO_XML)
root = tree.getroot()  # nodo raíz <persona>
print(f"Datos cargados desde {ARCHIVO_XML.name!r}:")
# Cada hijo directo: .tag = nombre de etiqueta, .text = contenido.
for child in root:
    print(f"{child.tag}: {child.text}")

# Nota: JSON suele ser más simple y ligero para APIs modernas.
# XML brilla en documentos con estructura compleja o esquemas estrictos.
# Siempre validá/sanitizá datos externos (por eso usamos defusedxml al parsear).

# ============================
# 🔹 Ejemplo práctico JSON (crear → guardar → leer → dumps → borrar)
# ============================
print("\n--- Ejemplo práctico JSON: crear diccionario ---")

data = {
    "nombre": "Raúl",
    "edad": 32,
    "lenguajes": ["Python", "JavaScript", "Go"],
    "activo": True,
}
print("data:", data)

file_name_json = DIR / "ejemplo.json"

print("\n--- Ejemplo práctico JSON: guardar archivo ---")
with open(file_name_json, "w", encoding=ENCODING) as file:
    # dump → dict a JSON en archivo
    # indent=4 → legible
    # ensure_ascii=False → respeta tildes y ñ (Raúl se ve bien)
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Archivo JSON creado y escrito ✅")

print("\n--- Ejemplo práctico JSON: leer archivo ---")
with open(file_name_json, "r", encoding=ENCODING) as file:
    contenido = json.load(file)  # load → JSON de archivo a dict
    print("contenido:", contenido)

print("\n--- Ejemplo práctico JSON: dumps (string) ---")
# dumps útil cuando necesitás el JSON como str (enviar por red, log, etc.).
json_string = json.dumps(data, indent=2, ensure_ascii=False)
print("json_string:", json_string)

print("\n--- Ejemplo práctico JSON: eliminar archivo ---")
if file_name_json.exists():
    file_name_json.unlink()
    print("Archivo JSON eliminado ✅")

# ============================
# 🔹 Ejemplo práctico XML (árbol anidado + búsqueda)
# ============================
file_name_xml = DIR / "ejemplo.xml"

print("\n--- Ejemplo práctico XML: crear árbol ---")
root = ET.Element("persona")  # Nodo raíz
nombre = ET.SubElement(root, "nombre")
nombre.text = "Raúl"
edad = ET.SubElement(root, "edad")
edad.text = "32"
lenguajes = ET.SubElement(root, "lenguajes")

# Dentro de <lenguajes> creamos varios <lenguaje>...</lenguaje>
for lang in ["Python", "JavaScript", "Go"]:
    ET.SubElement(lenguajes, "lenguaje").text = lang

activo = ET.SubElement(root, "activo")
activo.text = "true"
print("Árbol XML creado: OK")

print("\n--- Ejemplo práctico XML: guardar archivo ---")
tree = ET.ElementTree(root)
# write acepta una ruta (str/Path) directamente.
tree.write(file_name_xml, encoding=ENCODING, xml_declaration=True)

print("Archivo XML creado y escrito ✅")

print("\n--- Ejemplo práctico XML: leer y parsear ---")
tree = cargar_xml(file_name_xml)
root = tree.getroot()

print("Contenido XML leído:")
# child.text de <lenguajes> es None porque sus datos están en nietos.
for child in root:
    print(child.tag, ":", child.text)

print("\n--- Ejemplo práctico XML: buscar lenguajes ---")
# find("lenguajes") busca el hijo con esa etiqueta; luego iteramos sus hijos.
for lang in root.find("lenguajes"):
    print("lenguaje:", lang.text)

print("\n--- Ejemplo práctico XML: eliminar archivo ---")
if file_name_xml.exists():
    file_name_xml.unlink()
    print("Archivo XML eliminado ✅")

# Limpiar data.json / data.xml creados en la teoría.
for ruta in (ARCHIVO_JSON, ARCHIVO_XML):
    if ruta.exists():
        ruta.unlink()

# ============================
# 🔹 Resumen
# ============================
# - JSON: json.dumps/loads (memoria) y json.dump/load (archivo)
# - True/False/None de Python ↔ true/false/null en JSON
# - ensure_ascii=False conserva tildes y ñ al serializar
# - XML: ET.Element / SubElement para crear; ElementTree.write para guardar
# - Parsear XML externo: preferí defusedxml (XXE) sobre ElementTree.parse
# - find() / iterar hijos → navegar el árbol XML
# 💡 Para APIs modernas, JSON suele ser la primera opción
