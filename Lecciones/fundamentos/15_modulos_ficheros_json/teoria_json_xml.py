# Json y xml en python
import json
import xml.etree.ElementTree as ET # Librería estándar para trabajar con XML
# JSON (JavaScript Object Notation)
# JSON es un formato ligero de intercambio de datos, fácil de leer y escribir para humanos y
# fácil de parsear y generar para máquinas. En Python, se maneja principalmente con el
# módulo json. Se utiliza comúnmente para APIs web y configuración de aplicaciones.
# Ejemplo de conversión de un diccionario a JSON
data = {"nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hijos": ["Ana", "Luis"],
    "casado": True,
    "mascota": None}
# Convertir a JSON
json_data = json.dumps(data, indent=4) # indent para formato legible
print("JSON generado:")
print(json_data)
# Convertir de JSON a diccionario
data_cargada = json.loads(json_data)
print("\nDiccionario cargado desde JSON:")
print(data_cargada)
# Guardar JSON en un archivo
with open("data.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, indent=4)
print("\nJSON guardado en 'data.json'")
# Cargar JSON desde un archivo
with open("data.json", "r", encoding="utf-8") as json_file:
    data_desde_archivo = json.load(json_file)
print("\nDiccionario cargado desde 'data.json':")
print(data_desde_archivo)
# XML (eXtensible Markup Language)
# XML es un formato de marcado que define un conjunto de reglas para la codificación de documentos
# en un formato que es tanto legible por humanos como por máquinas. En Python, se puede manejar con
# varias bibliotecas, siendo xml.etree.ElementTree una de las más comunes.
# Ejemplo de creación de un documento XML
root = ET.Element("persona")
nombre = ET.SubElement(root, "nombre")
nombre.text = "Juan"
edad = ET.SubElement(root, "edad")
edad.text = "30"
ciudad = ET.SubElement(root, "ciudad")
ciudad.text = "Madrid"
# Convertir a cadena XML
xml_data = ET.tostring(root, encoding="unicode")
print("\nXML generado:")
print(xml_data)
# Guardar XML en un archivo
tree = ET.ElementTree(root)
with open("data.xml", "wb") as xml_file:
    tree.write(xml_file, encoding="utf-8", xml_declaration=True)
print("\nXML guardado en 'data.xml'")
# Cargar XML desde un archivo
tree = ET.parse("data.xml")
root = tree.getroot()
print("\nDatos cargados desde 'data.xml':")
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
import json
import os

# ===============================
# 📌 1. Crear un diccionario de Python
# ===============================
data = {
    "nombre": "Raúl",
    "edad": 32,
    "lenguajes": ["Python", "JavaScript", "Go"],
    "activo": True
}

file_name_json = "ejemplo.json"

# ===============================
# ✍️ 2. Guardar datos en un archivo JSON
# ===============================
with open(file_name_json, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
    # dump -> convierte diccionario a JSON y lo guarda en un archivo
    # indent=4 -> lo hace legible con sangría
    # ensure_ascii=False -> respeta caracteres como tildes y ñ

print("✅ Archivo JSON creado y escrito")

# ===============================
# 📖 3. Leer datos desde un archivo JSON
# ===============================
with open(file_name_json, "r", encoding="utf-8") as file:
    contenido = json.load(file)  # load -> convierte JSON a diccionario de Python
    print("\n--- Contenido JSON leído ---")
    print(contenido)

# ===============================
# 🔄 4. Convertir diccionario a string JSON (sin archivo)
# ===============================
json_string = json.dumps(data, indent=2, ensure_ascii=False)
print("\n--- Diccionario convertido a string JSON ---")
print(json_string)

# ===============================
# ❌ 5. Eliminar archivo JSON (opcional)
# ===============================
if os.path.exists(file_name_json):
    os.remove(file_name_json)
    print("\n✅ Archivo JSON eliminado")

import xml.etree.ElementTree as ET
import os

file_name_xml = "ejemplo.xml"

# ===============================
# 📌 1. Crear un árbol XML
# ===============================
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

# ===============================
# ✍️ 2. Guardar XML en un archivo
# ===============================
tree = ET.ElementTree(root)
tree.write(file_name_xml, encoding="utf-8", xml_declaration=True)

print("✅ Archivo XML creado y escrito")

# ===============================
# 📖 3. Leer y parsear un XML
# ===============================
tree = ET.parse(file_name_xml)
root = tree.getroot()

print("\n--- Contenido XML leído ---")
for child in root:
    print(child.tag, ":", child.text)

# ===============================
# 🔎 4. Buscar elementos específicos
# ===============================
print("\n--- Lenguajes encontrados ---")
for lang in root.find("lenguajes"):
    print(lang.text)

# ===============================
# ❌ 5. Eliminar archivo XML (opcional)
# ===============================
if os.path.exists(file_name_xml):
    os.remove(file_name_xml)
    print("\n✅ Archivo XML eliminado")
