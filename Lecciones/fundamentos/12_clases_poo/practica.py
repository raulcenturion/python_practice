# ============================
# 📝 Ejercicios: Clases y POO
# 📘 Teoría: teoria_clases.py, teoria_herencia.py (misma carpeta)
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
print("Ejercicio 1:")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} años"


persona1 = Persona("Juan", 30)
persona2 = Persona("Ana", 25)
print(persona1.presentarse())
print(persona2.presentarse())


# Ejercicio 2: Encapsulamiento
# Creá una clase CuentaBancaria con titular y __saldo (privado).
# Agregá métodos depositar(), retirar() y ver_saldo().
# Probá que no se pueda acceder directamente a __saldo.

print("Ejercicio 2:")
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo
    
    def depositar(self, cantidad):
        self.__saldo += cantidad
    def retirar(self, cantidad):
        self.__saldo -= cantidad
    def ver_saldo(self):
        return self.__saldo

cuenta1 = CuentaBancaria("Juan", 1000)
print(cuenta1.ver_saldo())
cuenta1.depositar(500)
print(cuenta1.ver_saldo())

# Ejercicio 3: Herencia
# Creá una clase Vehículo con marca y modelo.
# Creá una clase Auto que herede de Vehículo y agregue el atributo puertas.
# Creá una instancia de Auto y mostrá todos sus atributos.

print("Ejercicio 3:")
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas
auto1 = Auto("Ford", "Fiesta", 4)
print(auto1.marca)
print(auto1.modelo)
print(auto1.puertas)


# Ejercicio 4: Polimorfismo
# Creá las clases Gato y Pato, ambas con un método hablar().
# Creá una función hacer_hablar(animal) que llame a animal.hablar().
# Probá pasándole instancias de Gato y Pato.

print("Ejercicio 4:")
class Gato:
    def hablar(self):
        return "Miau"
class Pato:
    def hablar(self):
        return "Cuac"
def hacer_hablar(animal):
    print(animal.hablar())
gato = Gato()
pato = Pato()
hacer_hablar(gato)
hacer_hablar(pato)  

# Ejercicio 5: @classmethod y @staticmethod
# Creá una clase Empleado con un atributo de clase empresa = "TechCorp".
# Agregá un @classmethod para cambiar la empresa.
# Agregá un @staticmethod que valide si un email contiene "@".

print("Ejercicio 5:")   
class Empleado:
    empresa = "TechCorp"
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
    @classmethod
    def cambiar_empresa(cls, nueva_empresa):
        cls.empresa = nueva_empresa
    @staticmethod
    def validar_email(email):
        return "@" in email
empleado1 = Empleado("Juan", "Programador")
print(empleado1.empresa)
empleado1.cambiar_empresa("TechCorp")
print(empleado1.empresa)
print(empleado1.validar_email("juan@gmail.com"))
print(empleado1.validar_email("juangmail.com"))

# Ejercicio 6: Clase abstracta
# Creá una clase abstracta Figura con un método abstracto area().
# Creá Cuadrado y Circulo que implementen area().
# Probá ambas.

print("Ejercicio 6:")
from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(self):
        """Cada subclase DEBE implementar su propio cálculo de área."""
        raise NotImplementedError


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio


cuadrado = Cuadrado(10)
circulo = Circulo(5)
print(cuadrado.area())
print(circulo.area())
