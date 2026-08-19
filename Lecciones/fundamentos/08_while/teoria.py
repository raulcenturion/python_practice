# ============================
# 📘 Bucle while
# ============================
# Idea clave: while repite un bloque MIENTRAS la condición sea True.
#
#   while condición:
#       # se ejecuta una y otra vez
#
# Herramientas que vas a ver acá:
#   break    → sale del bucle YA (no sigue)
#   continue → salta al próximo ciclo (no ejecuta lo de abajo)
#   else     → corre solo si el while terminó SIN break

MSG_FIN = "Fin del ejemplo while."
LABEL_VALOR = "valor:"

# ---------------------------
# Contar del 1 al 5
# ---------------------------
# Meta: imprimir 1, 2, 3, 4, 5 y después cortar.
# El contador EMPIEZA en 1 y SUBE en cada vuelta (contador += 1).
# Cuando contador llega a 6, la condición contador <= 5 es False → sale.
print("--- Contar del 1 al 5 ---")
contador = 1
while contador <= 5:
    print(LABEL_VALOR, contador)
    contador += 1  # sin esto, el while sería infinito
print(MSG_FIN)

# ---------------------------
# Sumar hasta superar 20 (input)
# ---------------------------
# Meta: pedir números al usuario y ir sumando hasta pasar 20.
# Acá la condición mira la variable 'suma', no un contador fijo.
print("\n--- Sumar hasta superar 20 (input) ---")
print("Idea: el while sigue mientras suma <= 20")
suma = 0
while suma <= 20:
    numero = int(input("Ingrese un número para sumar: "))
    suma += numero
    print(f"Suma actual: {suma}")
print("La suma ha superado 20.")
# --- Operador += y casteo inicial ---
# suma += numero → es una forma abreviada de:
#   suma = suma + numero
#   Sirve para acumular valores en una variable de manera más clara y compacta.
#
# suma = 0 → ya es un entero (int) por defecto.
#   No hace falta castear, pero se puede escribir suma = int(0).
#   El resultado es exactamente el mismo, porque 0 ya es de tipo int.
#
# En resumen:
# - += acumula sumando el valor a la variable.
# - int(0) es redundante, ya que 0 en Python es entero por defecto.

# ---------------------------
# break + input (menú infinito hasta que digan salir)
# ---------------------------
# Meta: while True (bucle "infinito") + break para cortar a propósito.
# lower() hace que 'Salir', 'SALIR' y 'salir' cuenten igual.
print("\n--- break con input ---")
print("Idea: while True se corta solo con break")
while True:
    entrada = input("Ingrese 'salir' para terminar el bucle: ")
    if entrada.lower() == "salir":
        print("Salida pedida por el usuario.")
        break  # corta el while de inmediato
    print(f"Usted ingresó: {entrada}")

# ---------------------------
# continue — saltar pares
# ---------------------------
# Meta: mostrar solo impares del 1 al 10.
# Si el número es par → continue (no llega al print de esa vuelta).
# Importante: el contador se incrementa ANTES del continue,
# para no quedar atrapados en el mismo valor.
print("\n--- continue (saltar pares) ---")
print("Idea: continue salta el resto del cuerpo y va a la siguiente vuelta")
contador = 0
while contador < 10:
    contador += 1
    if contador % 2 == 0:  # % 2 == 0 → es par
        continue
    print(f"Número impar: {contador}")
print(MSG_FIN)

# ---------------------------
# else con while (sin break → else SÍ corre)
# ---------------------------
# Meta: vaciar una cola con pop(0). Si nunca usamos break, corre el else.
# while cola:  → mientras la lista tenga elementos (lista no vacía = True)
# El if actual == 99 nunca se cumple acá; solo muestra dónde iría un break.
print("\n--- else con while (sin break → else corre) ---")
print("Idea: else del while = 'terminé normal, sin break'")
cola = [1, 2, 3, 4, 5]
while cola:
    actual = cola.pop(0)  # saca el primero
    print(LABEL_VALOR, actual)
    if actual == 99:
        break
else:
    print("Cola vacía sin break → else del while.")

# ---------------------------
# Condición inicial falsa + else
# ---------------------------
# Meta: si el while NI SIQUIERA entra, el else igual se ejecuta.
# cola_vacia es [] → en un if/while cuenta como False.
print("\n--- Condición inicial falsa + else ---")
print("Idea: lista vacía → no entra al while → igual corre else")
cola_vacia: list[int] = []
while cola_vacia:
    actual = cola_vacia.pop()
    print(LABEL_VALOR, actual)
    if actual == 99:
        break
else:
    print("No entró al while; igual corre else.")

# ---------------------------
# break → el else NO se ejecuta
# ---------------------------
# Meta: contrastar con el ejemplo anterior.
# Al llegar a 3 hacemos break → el else del while se saltea.
print("\n--- break (else NO se ejecuta) ---")
print("Idea: si hubo break, el else del while NO corre")
contador = 1
while contador <= 5:
    print(LABEL_VALOR, contador)
    if contador == 3:
        print("Contador es 3, salgo con break.")
        break
    contador += 1
else:
    print("Esto no se imprime porque hubo break.")

# ---------------------------
# continue + else (else SÍ corre)
# ---------------------------
# Meta: continue NO es break. Saltás una vuelta, pero el bucle sigue.
# Si terminás sin break, el else corre igual.
print("\n--- continue + else (else sí corre) ---")
print("Idea: continue no cancela el else; solo break lo cancela")
cola = [1, 2, 3, 4, 5]
while cola:
    actual = cola.pop(0)
    if actual == 3:
        print("Salto el 3 con continue.")
        continue  # no imprime el 3, pero sigue el while
    if actual == 99:  # nunca ocurre; deja claro que break cancelaría el else
        break
    print(f"Número: {actual}")
else:
    print("Terminó sin break → else del while.")

# ---------------------------
# Contar 1..5 saltando el 3
# ---------------------------
# Meta: mismo patrón que "saltar pares", pero saltando un valor concreto.
# Ojo: al hacer continue hay que haber incrementado el contador,
# si no te quedás en un bucle infinito en el 3.
print("\n--- Contar 1..5 saltando el 3 ---")
print("Idea: continue para no imprimir el 3")
contador = 1
while contador <= 5:
    if contador == 3:
        contador += 1
        continue
    print(LABEL_VALOR, contador)
    contador += 1
print(MSG_FIN)

# ---------------------------
# try/except dentro de while
# ---------------------------
# Meta: pedir enteros hasta que el usuario mande -1.
# Si escribe "hola", int(...) lanza ValueError → lo capturamos
# y el while sigue (no se cae el programa).
print("\n--- try/except dentro de while (input) ---")
print("Idea: errores de conversión no rompen el bucle")
while True:
    try:
        numero = int(input("Ingrese un número entero (o -1 para salir): "))
        if numero == -1:
            print("Salida con -1.")
            break
        print(f"Usted ingresó: {numero}")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
print(MSG_FIN)

# ---------------------------
# Mini mapa mental
# ---------------------------
# while condición:  → repetir mientras sea True
# break             → salir ya
# continue          → siguiente vuelta
# else              → solo si terminó sin break
# try/except        → manejar inputs inválidos sin romper el programa
