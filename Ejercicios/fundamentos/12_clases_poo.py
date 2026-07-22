# ============================
# 📝 Ejercicios: Clases y POO
# 📘 Teoría: Clases_teoria/fundamentos/15_clases.py + 19_herencia_polimorfismo.py
# ============================

# 🔸 Ejemplo:
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"{self.nombre} hace un sonido"

class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Guau!"

rex = Perro("Rex")
print(rex.hablar())  # Rex dice: Guau!

# ============================
# Ejercicio 1: Clase Persona
# Creá una clase Persona con nombre y edad.
# Agregá un método presentarse() que retorne "Soy X, tengo Y años".
# Creá 2 instancias y probá el método.


# Ejercicio 2: Encapsulamiento
# Creá una clase CuentaBancaria con titular y __saldo (privado).
# Agregá métodos depositar(), retirar() y ver_saldo().
# Probá que no se pueda acceder directamente a __saldo.


# Ejercicio 3: Herencia
# Creá una clase Vehículo con marca y modelo.
# Creá una clase Auto que herede de Vehículo y agregue el atributo puertas.
# Creá una instancia de Auto y mostrá todos sus atributos.


# Ejercicio 4: Polimorfismo
# Creá las clases Gato y Pato, ambas con un método hablar().
# Creá una función hacer_hablar(animal) que llame a animal.hablar().
# Probá pasándole instancias de Gato y Pato.


# Ejercicio 5: @classmethod y @staticmethod
# Creá una clase Empleado con un atributo de clase empresa = "TechCorp".
# Agregá un @classmethod para cambiar la empresa.
# Agregá un @staticmethod que valide si un email contiene "@".


# Ejercicio 6: Clase abstracta
# Creá una clase abstracta Figura con un método abstracto area().
# Creá Cuadrado y Circulo que implementen area().
# Probá ambas.

