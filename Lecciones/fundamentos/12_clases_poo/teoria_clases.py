# ============================
# 📘 Clases y POO (Programación Orientada a Objetos)
# ============================
# Una clase es una PLANTILLA para crear objetos.
# Define atributos (datos) y métodos (funciones) que tendrán los objetos.
# Se define con la palabra clave `class` y por convención se usa CamelCase.
#
# Sintaxis básica:
# class NombreClase:
#     def __init__(self, parametros):   ← constructor (se ejecuta al crear el objeto)
#         self.atributo = valor         ← guarda datos en la instancia
#     def metodo(self):                 ← función que pertenece al objeto
#         bloque_de_codigo

# ============================
# 🔹 Instancias (crear objetos a partir de una clase)
# ============================
print("--- Clase Persona (instancias) ---")


# Definimos la clase Persona con 2 atributos y 1 método.
class Persona:
    # __init__ es el CONSTRUCTOR: se ejecuta automáticamente al hacer Persona(...)
    # self = referencia al objeto que se está creando (siempre va primero).
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Guardo el nombre que me pasan en el objeto
        self.edad = edad      # Guardo la edad que me pasan en el objeto

    # Método de instancia: usa self para acceder a los datos del objeto.
    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."


# Creamos 2 objetos (instancias) de Persona.
# Al hacer Persona("Alice", 30), Python ejecuta __init__ con nombre="Alice", edad=30.
persona1 = Persona("Alice", 30)
# Llamamos al método saludar() del objeto persona1.
# Internamente, Python pasa persona1 como self.
print("persona1.saludar():", persona1.saludar())

persona2 = Persona("Bob", 25)
print("persona2.saludar():", persona2.saludar())
# persona1 y persona2 son objetos independientes: cada uno tiene SU nombre y SU edad.


# ============================
# 🔹 Atributos de clase vs atributos de instancia
# ============================
print("\n--- Atributos de clase (Circulo) ---")


class Circulo:
    # Atributo de CLASE: compartido por TODOS los círculos (no depende de cada objeto).
    # Se define fuera de __init__, a nivel de la clase.
    pi = 3.14159

    def __init__(self, radio):
        # Atributo de INSTANCIA: cada círculo tiene su propio radio.
        self.radio = radio

    def area(self):
        # Accedemos al atributo de clase con Circulo.pi (o self.pi).
        # El radio viene del objeto (self.radio).
        return Circulo.pi * (self.radio ** 2)


# Creamos un círculo con radio 5 y calculamos su área.
circulo1 = Circulo(5)
print("Área del círculo:", circulo1.area())
# → 3.14159 * 25 = 78.53975


# ============================
# 🔹 Función anidada (concepto previo a closures/decoradores)
# ============================
print("\n--- Función anidada (ejemplo) ---")


# Esto NO es POO, es una función normal con otra función adentro.
# Se incluye acá para comparar con métodos de clase.
def externa(x):
    # interna() solo existe dentro de externa() — no se puede llamar desde afuera.
    def interna(y):
        return x + y       # x viene de externa (closure), y es parámetro de interna
    return interna(x * 2)  # Llama a interna con y = 10 (5*2)


# externa(5) → interna(10) → 5 + 10 = 15
print("Función anidada:", externa(5))


# ============================
# 🔹 Herencia (reutilizar una clase existente)
# ============================
print("\n--- Herencia (Estudiante) ---")


# Estudiante HEREDA de Persona: tiene todo lo de Persona + cosas propias.
# La sintaxis es class Hija(Padre):
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        # super().__init__(...) llama al constructor de Persona.
        # Así no repetimos el código de guardar nombre y edad.
        super().__init__(nombre, edad)
        # Atributo nuevo, propio de Estudiante (Persona no lo tiene).
        self.carrera = carrera

    # Método nuevo que solo tiene Estudiante.
    def estudiar(self):
        # self.nombre viene de Persona (lo heredó).
        return f"{self.nombre} está estudiando {self.carrera}."


# Creamos un Estudiante: tiene saludar() (de Persona) + estudiar() (propio).
estudiante1 = Estudiante("Charlie", 22, "Ingeniería")
# saludar() viene de Persona — no lo redefinimos, lo hereda tal cual.
print("estudiante1.saludar():", estudiante1.saludar())
# estudiar() es propio de Estudiante.
print("estudiante1.estudiar():", estudiante1.estudiar())
# --- Herencia con super() ---
#
# class Estudiante(Persona): → Estudiante hereda de Persona.
#
# def __init__(self, nombre, edad, carrera):
#   - Constructor de Estudiante.
#   - Recibe nombre y edad (de Persona) + carrera (nuevo).
#
# super().__init__(nombre, edad)
#   - super() devuelve un objeto que representa la clase padre (Persona).
#   - Llama al constructor de Persona para inicializar nombre y edad.
#   - Ventaja: reutiliza código, no repetimos lógica de la clase base.
#
# self.carrera = carrera → atributo nuevo, exclusivo de Estudiante.
#
# def estudiar(self): → método propio de Estudiante.
#   - Usa self.nombre (heredado de Persona).
#   - Usa self.carrera (definido en Estudiante).
#   - Devuelve un mensaje: "<nombre> está estudiando <carrera>".
#
# --- Conceptos ---
# - Herencia: Estudiante tiene todo lo de Persona + lo propio.
# - super(): accede a métodos de la clase padre, evita duplicar código.
# - self: referencia al objeto actual, guarda y accede a atributos.


# ============================
# 🔹 Métodos especiales (__str__ y __repr__)
# ============================
print("\n--- Métodos especiales (__str__ / __repr__) ---")


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # __str__: se ejecuta cuando hacés print(objeto) o str(objeto).
    # Pensalo como "la versión bonita para el usuario".
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

    # __repr__: se ejecuta cuando hacés repr(objeto) o lo ves en la consola interactiva.
    # Pensalo como "la versión técnica para el programador".
    def __repr__(self):
        return f"Punto(x={self.x}, y={self.y})"


punto1 = Punto(3, 4)
# print() llama a __str__ del objeto automáticamente.
print("str(punto1):", punto1)
# repr() llama a __repr__ del objeto.
print("repr(punto1):", repr(punto1))


# ============================
# 🔹 Encapsulamiento (atributos privados)
# ============================
print("\n--- Encapsulamiento (CuentaBancaria) ---")


class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        # __ (doble guion bajo) hace que el atributo sea "privado".
        # No se puede acceder directamente desde fuera con cuenta.__saldo.
        # Python internamente lo renombra a _CuentaBancaria__saldo (name mangling).
        self.__saldo = saldo

    def depositar(self, cantidad):
        # Validamos que la cantidad sea positiva antes de modificar el saldo.
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida."

    def retirar(self, cantidad):
        # Validamos que sea positiva Y que haya fondos suficientes.
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso. Nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad inválida o saldo insuficiente."

    def mostrar_saldo(self):
        # Este método es la ÚNICA forma "correcta" de ver el saldo desde afuera.
        # Eso es encapsulamiento: controlamos el acceso a los datos.
        return f"Saldo actual: {self.__saldo}"


# Creamos una cuenta con $1000 y operamos a través de los métodos.
cuenta1 = CuentaBancaria("David", 1000)
print("mostrar_saldo:", cuenta1.mostrar_saldo())  # $1000
print("depositar(500):", cuenta1.depositar(500))   # $1500
print("retirar(200):", cuenta1.retirar(200))       # $1300
print("mostrar_saldo:", cuenta1.mostrar_saldo())   # $1300
# Nota: cuenta1.__saldo daría AttributeError.
# Se puede forzar con cuenta1._CuentaBancaria__saldo, pero NO se debe hacer.


# ============================
# 🔹 pass (clase vacía / placeholder)
# ============================
print("\n--- pass (clase vacía) ---")


# pass = "no hacer nada". Se usa cuando la sintaxis pide un bloque pero
# todavía no querés escribir código (placeholder).
class ClaseVacia:
    pass


# Se puede instanciar igual, aunque no tiene atributos ni métodos.
clase_vacia = ClaseVacia()
print("Instancia de clase vacía creada:", clase_vacia)


# ============================
# 🔹 @classmethod y @staticmethod
# ============================
print("\n--- @classmethod y @staticmethod ---")
# @classmethod: recibe la CLASE (cls) como primer argumento. Puede modificar atributos de clase.
# @staticmethod: NO recibe ni self ni cls. Es una función normal que vive dentro de la clase.


class Persona2:
    # Atributo de CLASE: compartido por todas las instancias de Persona2.
    especie = "Humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        """Modifica el atributo de clase para TODAS las instancias.
        cls = la clase en sí (Persona2), no una instancia particular."""
        cls.especie = nueva_especie

    @staticmethod
    def es_mayor(edad):
        """No necesita acceso a la instancia (self) ni a la clase (cls).
        Es como una función suelta, pero la agrupamos dentro de Persona2
        porque tiene sentido conceptualmente."""
        return edad >= 18


# Creamos 2 instancias. Ambas comparten especie = "Humano".
p1 = Persona2("Raúl", 33)
p2 = Persona2("Ana", 25)

print("p1.especie:", p1.especie)  # Humano
print("p2.especie:", p2.especie)  # Humano

# Llamamos al @classmethod desde la CLASE (no desde una instancia).
# Cambia especie para TODOS los objetos, porque modifica el atributo de clase.
Persona2.cambiar_especie("Reptiliano")
print("p1.especie (tras cambiar):", p1.especie)  # Reptiliano
print("p2.especie (tras cambiar):", p2.especie)  # Reptiliano

# @staticmethod se puede llamar desde la clase O desde una instancia.
# No modifica nada de la clase ni del objeto — solo devuelve un resultado.
print("Persona2.es_mayor(20):", Persona2.es_mayor(20))  # True (llamada desde la clase)
print("p1.es_mayor(p1.edad):", p1.es_mayor(p1.edad))    # True (llamada desde instancia)


# ============================
# 🔹 Abstracción con ABC (clases abstractas)
# ============================
print("\n--- Abstracción con ABC ---")
# ABC = Abstract Base Class. Sirve para definir una "plantilla obligatoria":
# la clase base dice QUÉ métodos deben existir, pero NO los implementa.
# Cada subclase DEBE implementarlos (si no, da error al instanciar).

from abc import ABC, abstractmethod


class CuentaBancaria2(ABC):
    """Clase abstracta: NO se puede instanciar directamente.
    Define la estructura que toda cuenta debe tener."""

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # __saldo es privado: solo accesible dentro de esta clase (y con helpers).
        self.__saldo = saldo_inicial

    def depositar(self, monto):
        """Método concreto (ya implementado): todas las cuentas depositan igual."""
        if monto > 0:
            self.__saldo += monto

    def _get_saldo(self):
        """Helper protegido (_) para que las subclases lean el saldo privado.
        Usamos _ (un guion bajo) = "protegido" (convención: solo para uso interno)."""
        return self.__saldo

    def _set_saldo(self, nuevo):
        """Helper protegido para que las subclases modifiquen el saldo privado."""
        self.__saldo = nuevo

    @abstractmethod
    def retirar(self, monto):
        """Método ABSTRACTO: cada subclase DEBE implementar su propia versión.
        Si no lo hace, Python lanza TypeError al intentar instanciarla."""
        #pass - > acá va el codigo que va a implementar la subclase

    def ver_saldo(self):
        return f"Saldo: ${self.__saldo}"
# --- Uso de super() en métodos sobrescritos ---
#
# class Persona: → clase base con __init__ y __str__.
# class Estudiante(Persona): → clase hija que hereda de Persona.
#
# super().__init__(nombre, edad)
#   → llama al constructor de Persona para inicializar atributos heredados.
#
# def __str__(self):
#   base = super().__str__() → reutiliza el método __str__ de Persona.
#   return f"{base}, estudiante de {self.carrera}"
#   → extiende la lógica del padre agregando información propia.
#
# --- Concepto ---
# - super() no es solo para constructores.
# - También se usa en métodos sobrescritos para reutilizar y ampliar la lógica del padre.
# - Esto evita duplicar código y mantiene la herencia limpia.


# CuentaAhorro hereda de CuentaBancaria2 y OBLIGA a implementar retirar().
class CuentaAhorro(CuentaBancaria2):
    def retirar(self, monto):
        # Esta cuenta cobra 5% de penalidad por cada retiro.
        penalidad = monto * 0.05
        total = monto + penalidad  # Lo que realmente se descuenta.
        if total <= self._get_saldo():
            # _get_saldo() y _set_saldo() vienen de la clase padre.
            # Son la forma de acceder al __saldo privado desde la subclase.
            self._set_saldo(self._get_saldo() - total)
        else:
            print("Fondos insuficientes en cuenta de ahorro")


# CuentaNomina: otra subclase, sin penalidad.
class CuentaNomina(CuentaBancaria2):
    def retirar(self, monto):
        # Retira directo si hay fondos (sin penalidad).
        if monto <= self._get_saldo():
            self._set_saldo(self._get_saldo() - monto)
        else:
            print("Fondos insuficientes en cuenta de nómina")


# Ambas cuentas arrancan con $1000.
ahorro = CuentaAhorro("Raúl", 1000)
nomina = CuentaNomina("Raúl", 1000)

# Retiramos $100 de cada una.
ahorro.retirar(100)  # Descuenta 100 + 5 (penalidad) = 105
nomina.retirar(100)  # Descuenta 100 exactos

print("Ahorro:", ahorro.ver_saldo())  # $895.0  (1000 - 105)
print("Nómina:", nomina.ver_saldo())  # $900.0  (1000 - 100)
# → Mismo método retirar(), distinto comportamiento = POLIMORFISMO.


# ============================
# 🔹 Resumen POO
# ============================
# - Clase: plantilla para crear objetos (class NombreClase)
# - __init__: constructor, se ejecuta al crear una instancia
# - self: referencia a la instancia actual
# - Atributos de instancia: propios de cada objeto (self.x)
# - Atributos de clase: compartidos por todas las instancias (Clase.x)
# - Herencia: class Hija(Padre) → hereda atributos y métodos; super() llama al padre
# - __str__ / __repr__: controlan cómo se muestra el objeto en print / consola
# - Encapsulamiento: __privado (name mangling), _protegido (convención)
# - @classmethod: recibe la clase (cls), puede modificar atributos de clase
# - @staticmethod: función utilitaria dentro de la clase, sin acceso a self ni cls
# - pass: placeholder para clases/funciones vacías
# - ABC + @abstractmethod: obliga a las subclases a implementar métodos
# - Polimorfismo: misma interfaz (retirar), diferente implementación por subclase
