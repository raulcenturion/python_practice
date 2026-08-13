# Clases
# Una clase es una plantilla para crear objetos. Define un conjunto de atributos y métodos que los objetos creados a partir de la clase tendrán.
# Se define utilizando la palabra clave class seguida del nombre de la clase y dos puntos.
# La convención es usar CamelCase para los nombres de las clases.
# La sintaxis básica es:
# class NombreClase:
#     def __init__(self, parametros):
#         self.atributo = valor
#     def metodo(self):
#         bloque_de_codigo

print("--- Clase Persona (instancias) ---")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Atributo de instancia

    def saludar(self):  # Método de instancia
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

persona1 = Persona("Alice", 30)
print("persona1.saludar():", persona1.saludar())
persona2 = Persona("Bob", 25)
print("persona2.saludar():", persona2.saludar())

print("\n--- Atributos de clase (Circulo) ---")
class Circulo:
    pi = 3.14159  # Atributo de clase

    def __init__(self, radio):
        self.radio = radio  # Atributo de instancia

    def area(self):
        return Circulo.pi * (self.radio ** 2)

circulo1 = Circulo(5)
print("Área del círculo:", circulo1.area())

print("\n--- Función anidada (ejemplo) ---")
def externa(x):
        def interna(y):
            return x + y
        return interna(x * 2)
print("Función anidada:", externa(5))

print("\n--- Herencia (Estudiante) ---")
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera  # Nuevo atributo de instancia

    def estudiar(self):
        return f"{self.nombre} está estudiando {self.carrera}."

estudiante1 = Estudiante("Charlie", 22, "Ingeniería")
print("estudiante1.saludar():", estudiante1.saludar())
print("estudiante1.estudiar():", estudiante1.estudiar())

print("\n--- Métodos especiales (__str__ / __repr__) ---")
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"

punto1 = Punto(3, 4)
print("str(punto1):", punto1)          # Llama a __str__
print("repr(punto1):", repr(punto1))    # Llama a __repr__

print("\n--- Encapsulamiento (CuentaBancaria) ---")
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado (usa __ para indicar que es privado)
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida."
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida o saldo insuficiente."
    def mostrar_saldo(self):
        return f"Saldo actual: {self.__saldo}"

cuenta1 = CuentaBancaria("David", 1000)
print("mostrar_saldo:", cuenta1.mostrar_saldo())
print("depositar(500):", cuenta1.depositar(500))
print("retirar(200):", cuenta1.retirar(200))
print("mostrar_saldo:", cuenta1.mostrar_saldo())
# Nota: En Python, los atributos y métodos privados son una convención y no una restricción estricta. Se pueden acceder desde fuera de la clase usando el nombre modificado (por ejemplo
# cuenta1._CuentaBancaria__saldo), pero no es recomendable hacerlo.
# Pass es una palabra clave que se utiliza como un marcador de posición para indicar que no se va a implementar nada en ese lugar.
# Se usa comúnmente en clases o funciones que aún no se han implementado.

print("\n--- pass (clase vacía) ---")
class ClaseVacia:
    pass
clase_vacia = ClaseVacia()
print("Instancia de clase vacía creada:", clase_vacia)

print("\n--- @classmethod y @staticmethod ---")
# @classmethod: recibe la clase (cls) como primer argumento. Puede modificar atributos de clase.
# @staticmethod: NO recibe ni self ni cls. Es una función normal que vive dentro de la clase.

class Persona2:
    especie = "Humano"  # Atributo de clase (compartido por todas las instancias)

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        """Modifica el atributo de clase para TODAS las instancias."""
        cls.especie = nueva_especie

    @staticmethod
    def es_mayor(edad):
        """No necesita acceso a la instancia ni a la clase."""
        return edad >= 18

p1 = Persona2("Raúl", 33)
p2 = Persona2("Ana", 25)

print("p1.especie:", p1.especie)  # Humano
print("p2.especie:", p2.especie)  # Humano

Persona2.cambiar_especie("Reptiliano")  # Cambia para TODOS
print("p1.especie (tras cambiar):", p1.especie)  # Reptiliano
print("p2.especie (tras cambiar):", p2.especie)  # Reptiliano

print("Persona2.es_mayor(20):", Persona2.es_mayor(20))      # True (se llama desde la clase)
print("p1.es_mayor(p1.edad):", p1.es_mayor(p1.edad))       # True (también desde la instancia)

print("\n--- Abstracción con ABC ---")
from abc import ABC, abstractmethod


class CuentaBancaria2(ABC):
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def _get_saldo(self):
        return self.__saldo

    def _set_saldo(self, nuevo):
        self.__saldo = nuevo

    @abstractmethod
    def retirar(self, monto):
        pass  # Cada subclase DEBE implementar este método (polimorfismo)

    def ver_saldo(self):
        return f"Saldo: ${self.__saldo}"

class CuentaAhorro(CuentaBancaria2):
    def retirar(self, monto):
        penalidad = monto * 0.05  # 5% de penalidad
        total = monto + penalidad
        if total <= self._get_saldo():
            self._set_saldo(self._get_saldo() - total)
        else:
            print("Fondos insuficientes en cuenta de ahorro")

class CuentaNomina(CuentaBancaria2):
    def retirar(self, monto):
        if monto <= self._get_saldo():
            self._set_saldo(self._get_saldo() - monto)
        else:
            print("Fondos insuficientes en cuenta de nómina")

ahorro = CuentaAhorro("Raúl", 1000)
nomina = CuentaNomina("Raúl", 1000)
ahorro.retirar(100)
nomina.retirar(100)
print("Ahorro:", ahorro.ver_saldo())  # $895.0 (100 + 5% penalidad)
print("Nómina:", nomina.ver_saldo())  # $900.0

# ============================
# 🔹 Resumen POO
# ============================
# - Clase: plantilla para crear objetos (class NombreClase)
# - __init__: constructor, se ejecuta al crear una instancia
# - self: referencia a la instancia actual
# - Atributos de instancia: propios de cada objeto (self.x)
# - Atributos de clase: compartidos por todas las instancias (Clase.x)
# - Encapsulamiento: __privado (name mangling), _protegido (convención)
# - @classmethod: método que recibe la clase (cls), puede modificar atributos de clase
# - @staticmethod: función utilitaria dentro de la clase, sin acceso a self ni cls
# - Herencia: class Hija(Padre) → hereda atributos y métodos
# - Polimorfismo: misma interfaz, diferente implementación
# - ABC + @abstractmethod: obliga a las subclases a implementar métodos
