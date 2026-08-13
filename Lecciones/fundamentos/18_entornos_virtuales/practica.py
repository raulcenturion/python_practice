# ============================
# 📝 Ejercicios: Entornos virtuales y dependencias
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import sys

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


# Ejercicio 2: Activar
# Activá el entorno:
#   source .venv/bin/activate
# Confirmá que el prompt muestra (.venv)


# Ejercicio 3: Instalar y listar
# Con el venv activo:
#   pip install requests
#   pip list
# Anotá si aparece requests.


# Ejercicio 4: requirements.txt
# Generá/actualizá dependencias:
#   pip freeze > requirements.txt
# Abrí el archivo y confirmá que lista paquetes con versión.


# Ejercicio 5: Script de verificación
# Completá la función debajo para retornar True si el proceso corre en un venv.
# Imprimí también la ruta de sys.executable.


def corriendo_en_venv() -> bool:
    # Tu solución acá
    pass


if __name__ == "__main__":
    print("Resultado ejercicio 5:", corriendo_en_venv())

# Ejercicio 6: Reinstalar desde cero (mental / práctico)
# Desactivá (deactivate), borrá .venv (solo si estás seguro),
# recrealo e instalá con:
#   pip install -r requirements.txt
