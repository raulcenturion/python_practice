# ============================
# 📝 Ejercicios: async / await
# 📘 Teoría: Clases_teoria/fundamentos/28_async_await.py
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


# Ejercicio 2: Secuencial vs concurrente
# Creá async def trabajo(nombre, segundos) que haga await asyncio.sleep(segundos)
# y retorne el nombre.
# Compará:
#   a) await trabajo("A", 0.3); await trabajo("B", 0.3)  (secuencial)
#   b) await asyncio.gather(trabajo("A", 0.3), trabajo("B", 0.3))
# Medí con time.perf_counter() e imprimí ambos tiempos.


# Ejercicio 3: Varias tareas
# Lanzá 5 corutinas con gather (delay 0.2s cada una) e imprimí la lista de resultados.
# El tiempo total debería rondar ~0.2s, no ~1.0s.


# Ejercicio 4: Endpoint mental (estilo FastAPI)
# Escribí una función async def get_usuario(user_id: int) que:
# - simule I/O con await asyncio.sleep(0.1)
# - retorne {"id": user_id, "nombre": f"user-{user_id}"}
# Probala con asyncio.run(get_usuario(7))


# Plantilla opcional para el ejercicio 2:
async def demo_tiempos():
    # Tu solución acá
    pass


if __name__ == "__main__":
    print(asyncio.run(saludar("Raúl")))
    # asyncio.run(demo_tiempos())
