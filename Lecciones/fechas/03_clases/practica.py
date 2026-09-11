# ============================
# 📝 Ejercicios: Clases (repaso práctico)
# 📘 Teoría: teoria.py (misma carpeta)
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


def ejercicio_1_mascota() -> None:
    # ENUNCIADO:
    # Creá una clase Mascota con nombre y especie.
    # Agregá presentarse() → "Soy X, un/a Y".
    # Creá una instancia e imprimí presentarse().
    #
    # Guía:
    # class Mascota:
    #     def __init__(self, nombre, especie):
    #         self.nombre = nombre
    #         self.especie = especie
    #     def presentarse(self):
    #         return f"Soy {self.nombre}, un/a {self.especie}"
    #
    # TIP: mirá el ejemplo de Coche arriba.

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 1")


def ejercicio_2_clase_vs_instancia() -> None:
    # ENUNCIADO:
    # En Mascota (o una nueva clase) agregá:
    # - atributo de clase reino = "animal"
    # - atributo de instancia edad
    # Creá 2 mascotas e imprimí reino (clase) y edad (instancia).
    #
    # TIP:
    # class Mascota:
    #     reino = "animal"
    #     def __init__(self, nombre, especie, edad):
    #         self.nombre = nombre
    #         ...
    #         self.edad = edad

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 2")


def ejercicio_3_cumplir_anios() -> None:
    # ENUNCIADO:
    # Agregá cumplir_anios() que sume 1 a self.edad.
    # Imprimí edad antes y después de llamarlo.
    #
    # TIP:
    # def cumplir_anios(self):
    #     self.edad += 1

    # --- TU SOLUCIÓN ---
    raise NotImplementedError("Completá ejercicio 3")


if __name__ == "__main__":
    print("--- Práctica 03 clases ---")
    for fn in (
        ejercicio_1_mascota,
        ejercicio_2_clase_vs_instancia,
        ejercicio_3_cumplir_anios,
    ):
        try:
            fn()
            print(f"✅ {fn.__name__}")
        except NotImplementedError as e:
            print(f"⏳ Pendiente: {e}")
