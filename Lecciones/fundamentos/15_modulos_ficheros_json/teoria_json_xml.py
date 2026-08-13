# Json y xml en python
import json
import os
import xml.etree.ElementTree as ET  # crear / escribir XML

import defusedxml.ElementTree as SafeET  # parse seguro (evita XXE)

ENCODING = "utf-8"
ARCHIVO_JSON = "data.json"
ARCHIVO_XML = "data.xml"

# JSON (JavaScript Object Notation)
# JSON es un formato ligero de intercambio de datos, fácil de leer y escribir para humanos y
# fácil de parsear y generar para máquinas. En Python, se maneja principalmente con el
# módulo json. Se utiliza comúnmente para APIs web y configuración de aplicaciones.


def cargar_xml(ruta: str):
    """Carga un XML desde archivo con parser seguro (defusedxml)."""
    return SafeET.parse(ruta)


print("--- Diccionario a JSON (dumps) ---")
data = {"nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hijos": ["Ana", "Luis"],
    "casado": True,
    "mascota": None}
json_data = json.dumps(data, indent=4) # indent para formato legible
print("JSON generado:")
print(json_data)

print("\n--- JSON a diccionario (loads) ---")
data_cargada = json.loads(json_data)
print("Diccionario cargado desde JSON:", data_cargada)

print("\n--- Guardar JSON en archivo (dump) ---")
with open(ARCHIVO_JSON, "w", encoding=ENCODING) as json_file:
    json.dump(data, json_file, indent=4)
print(f"JSON guardado en {ARCHIVO_JSON!r}")

print("\n--- Cargar JSON desde archivo (load) ---")
with open(ARCHIVO_JSON, "r", encoding=ENCODING) as json_file:
    data_desde_archivo = json.load(json_file)
print(f"Diccionario cargado desde {ARCHIVO_JSON!r}:", data_desde_archivo)

# XML (eXtensible Markup Language)
# XML es un formato de marcado que define un conjunto de reglas para la codificación de documentos
# en un formato que es tanto legible por humanos como por máquinas. En Python, se puede manejar con
# varias bibliotecas, siendo xml.etree.ElementTree una de las más comunes.

print("\n--- Crear documento XML ---")
root = ET.Element("persona")
nombre = ET.SubElement(root, "nombre")
nombre.text = "Juan"
edad = ET.SubElement(root, "edad")
edad.text = "30"
ciudad = ET.SubElement(root, "ciudad")
ciudad.text = "Madrid"
xml_data = ET.tostring(root, encoding="unicode")
print("XML generado:", xml_data)

print("\n--- Guardar XML en archivo ---")
tree = ET.ElementTree(root)
with open(ARCHIVO_XML, "wb") as xml_file:
    tree.write(xml_file, encoding=ENCODING, xml_declaration=True)
print(f"XML guardado en {ARCHIVO_XML!r}")

print("\n--- Cargar XML desde archivo ---")
tree = cargar_xml(ARCHIVO_XML)
root = tree.getroot()
print(f"Datos cargados desde {ARCHIVO_XML!r}:")
for child in root:
    print(f"{child.tag}: {child.text}")

# Nota: JSON es generalmente más fácil de usar y más eficiente para la mayoría de las aplicaciones
# modernas, mientras que XML puede ser más adecuado para documentos con una estructura compleja
# o cuando se requiere un esquema riguroso.
# JSON es más ligero y fácil de leer, mientras que XML es más verboso y puede ser más difícil de manejar.
# JSON se utiliza comúnmente en APIs web y configuraciones, mientras que XML se usa en documentos y configuraciones más complejas.
# Python ofrece soporte nativo para JSON a través del módulo json, mientras que para XML se utilizan bibliotecas como xml.etree.ElementTree.
# La elección entre JSON y XML depende del caso de uso específico y de las necesidades del proyecto.
# Es importante validar y sanitizar los datos al trabajar con JSON y XML para evitar problemas de seguridad.
# Ambas tecnologías son ampliamente utilizadas y es beneficioso para los desarrolladores estar familiarizados
# con ambas.# La práctica y la experiencia son clave para dominar el manejo de JSON y XML en Python.
# No dudes en consultar la documentación oficial de Python y otros recursos para profundizar en estos temas.

print("\n--- Ejemplo práctico JSON: crear diccionario ---")
data = {
    "nombre": "Raúl",
    "edad": 32,
    "lenguajes": ["Python", "JavaScript", "Go"],
    "activo": True
}
print("data:", data)

file_name_json = "ejemplo.json"

print("\n--- Ejemplo práctico JSON: guardar archivo ---")
with open(file_name_json, "w", encoding=ENCODING) as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
    # dump -> convierte diccionario a JSON y lo guarda en un archivo
    # indent=4 -> lo hace legible con sangría
    # ensure_ascii=False -> respeta caracteres como tildes y ñ

print("Archivo JSON creado y escrito ✅")

print("\n--- Ejemplo práctico JSON: leer archivo ---")
with open(file_name_json, "r", encoding=ENCODING) as file:
    contenido = json.load(file)  # load -> convierte JSON a diccionario de Python
    print("contenido:", contenido)

print("\n--- Ejemplo práctico JSON: dumps (string) ---")
json_string = json.dumps(data, indent=2, ensure_ascii=False)
print("json_string:", json_string)

print("\n--- Ejemplo práctico JSON: eliminar archivo ---")
if os.path.exists(file_name_json):
    os.remove(file_name_json)
    print("Archivo JSON eliminado ✅")

file_name_xml = "ejemplo.xml"

print("\n--- Ejemplo práctico XML: crear árbol ---")
root = ET.Element("persona")       # Nodo raíz
nombre = ET.SubElement(root, "nombre")
nombre.text = "Raúl"
edad = ET.SubElement(root, "edad")
edad.text = "32"
lenguajes = ET.SubElement(root, "lenguajes")

# Agregar sub-elementos dentro de "lenguajes"
for lang in ["Python", "JavaScript", "Go"]:
    ET.SubElement(lenguajes, "lenguaje").text = lang

activo = ET.SubElement(root, "activo")
activo.text = "true"
print("Árbol XML creado: OK")

print("\n--- Ejemplo práctico XML: guardar archivo ---")
tree = ET.ElementTree(root)
tree.write(file_name_xml, encoding=ENCODING, xml_declaration=True)

print("Archivo XML creado y escrito ✅")

print("\n--- Ejemplo práctico XML: leer y parsear ---")
tree = cargar_xml(file_name_xml)
root = tree.getroot()

print("Contenido XML leído:")
for child in root:
    print(child.tag, ":", child.text)

print("\n--- Ejemplo práctico XML: buscar lenguajes ---")
for lang in root.find("lenguajes"):
    print("lenguaje:", lang.text)

print("\n--- Ejemplo práctico XML: eliminar archivo ---")
if os.path.exists(file_name_xml):
    os.remove(file_name_xml)
    print("Archivo XML eliminado ✅")

# Limpiar data.json / data.xml creados en la teoría
for ruta in (ARCHIVO_JSON, ARCHIVO_XML):
    if os.path.exists(ruta):
        os.remove(ruta)
