# ============================
# 📝 Ejercicios: async / await
# 📘 Teoría: teoria.py (misma carpeta)
# ============================

import asyncio
import time


# 🔸 Ejemplo:
async def saludar(nombre: str) -> str:
    await asyncio.sleep(0.1)
    return f"Hola, {nombre}"


# ============================
# ENUNCIADOS
# ============================

# Ejercicio 1: Primera corutina
# Creá async def ping() que espere 0.2s con asyncio.sleep y retorne "pong".
# Ejecutala con asyncio.run(ping()) e imprimí el resultado.
async def ping():
    await asyncio.sleep(0.2)
    return "pong"


print("Resultado ejercicio 1:")
print(asyncio.run(ping()))


# Ejercicio 2: Secuencial vs concurrente
# Creá async def trabajo(nombre, segundos) que haga await asyncio.sleep(segundos)
# y retorne el nombre.
# Compará:
#   a) await trabajo("A", 0.3); await trabajo("B", 0.3)  (secuencial)
#   b) await asyncio.gather(trabajo("A", 0.3), trabajo("B", 0.3))
# Medí con time.perf_counter() e imprimí ambos tiempos.


async def trabajo(nombre, segundos):
    await asyncio.sleep(segundos)
    return nombre


async def demo_tiempos():
    # a) secuencial: ~0.6s
    inicio = time.perf_counter()
    await trabajo("A", 0.3)
    await trabajo("B", 0.3)
    t_secuencial = time.perf_counter() - inicio

    # b) concurrente con gather: ~0.3s
    # gather se await DENTRO de una corutina; no se pasa directo a asyncio.run()
    inicio = time.perf_counter()
    resultados = await asyncio.gather(trabajo("A", 0.3), trabajo("B", 0.3))
    t_concurrente = time.perf_counter() - inicio

    print("secuencial:", round(t_secuencial, 3), "s")
    print("concurrente:", round(t_concurrente, 3), "s", "→", resultados)


print("Resultado ejercicio 2:")
asyncio.run(demo_tiempos())

# Ejercicio 3: Varias tareas
# Lanzá 5 corutinas con gather (delay 0.2s cada una) e imprimí la lista de resultados.
# El tiempo total debería rondar ~0.2s, no ~1.0s.

print("Resultado ejercicio 3:")


async def demo_varias_tareas():
    # asyncio.sleep() solo espera y retorna None → por eso veías [None, None, ...]
    # Usamos trabajo(...) para que cada corutina devuelva un resultado visible.
    inicio = time.perf_counter()
    resultados = await asyncio.gather(
        *[trabajo(f"T{i}", 0.2) for i in range(1, 6)]
    )
    t_total = time.perf_counter() - inicio
    print("resultados:", resultados)
    print("tiempo total:", round(t_total, 3), "s")  # debería ~0.2s


asyncio.run(demo_varias_tareas())


# Ejercicio 4: Endpoint mental (estilo FastAPI)
# Escribí una función async def get_usuario(user_id: int) que:
# - simule I/O con await asyncio.sleep(0.1)
# - retorne {"id": user_id, "nombre": f"user-{user_id}"}
# Probala con asyncio.run(get_usuario(7))

print("Resultado ejercicio 4:")
async def get_usuario(user_id: int):
    await asyncio.sleep(0.1)
    return {"id": user_id, "nombre": f"user-{user_id}"}

print(asyncio.run(get_usuario(7)))


if __name__ == "__main__":
    print(asyncio.run(saludar("Raúl")))
