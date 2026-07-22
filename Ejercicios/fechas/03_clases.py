# ============================
# 📝 Ejercicios: Clases (repaso práctico)
# 📘 Teoría: Clases_teoria/fechas/03_clases.py
# ============================

# 🔸 Ejemplo:
class Coche:
    tipo = "vehículo"

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def arrancar(self):
        return f"El coche {self.marca} {self.modelo} arrancó!"


mi_coche = Coche("Toyota", "Corolla", "rojo")
print(mi_coche.arrancar())

# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Clase básica
# Creá una clase Mascota con nombre y especie.
# Agregá un método presentarse() que retorne "Soy X, un/a Y".


# Ejercicio 2: Atributo de clase vs instancia
# Agregá un atributo de clase "reino = animal" y uno de instancia "edad".
# Creá 2 mascotas e imprimí ambos tipos de atributos.


# Ejercicio 3: Método que modifica estado
# Agregá un método cumplir_anios() que sume 1 a la edad.
# Probá llamarlo e imprimí la edad antes y después.
