# ============================
# 📘 Asincronía: async / await
# ============================
# FastAPI usa funciones async para no bloquear el servidor mientras
# espera I/O (DB, HTTP, disco). Acá está la base de Python.

import asyncio
import time

# ============================
# 🔹 Conceptos
# ============================
# - Corutina: función definida con `async def`. No se ejecuta al llamarla;
#   retorna un objeto coroutine que hay que `await` o pasar a asyncio.run().
# - await: pausa la corutina actual hasta que termine otra awaitable,
#   y libera el event loop para hacer otra cosa.
# - Event loop: el motor que agenda y ejecuta corutinas.

# ============================
# 🔹 Función sync vs async
# ============================


def tarea_sync(nombre: str, segundos: float) -> str:
    time.sleep(segundos)  # bloquea TODO el hilo
    return f"{nombre} listo (sync)"


async def tarea_async(nombre: str, segundos: float) -> str:
    await asyncio.sleep(segundos)  # no bloquea el event loop
    return f"{nombre} listo (async)"


# ============================
# 🔹 Ejecutar una corutina
# ============================
async def ejemplo_simple():
    resultado = await tarea_async("A", 0.2)
    print(resultado)


# ============================
# 🔹 Concurrencia con gather
# ============================
# Tres tareas de 0.3s en paralelo ≈ 0.3s total (no 0.9s)
async def ejemplo_concurrente():
    inicio = time.perf_counter()
    resultados = await asyncio.gather(
        tarea_async("download-1", 0.3),
        tarea_async("download-2", 0.3),
        tarea_async("download-3", 0.3),
    )
    duracion = time.perf_counter() - inicio
    print(resultados)
    print(f"Tiempo total concurrente: {duracion:.2f}s")


# ============================
# 🔹 Analogía FastAPI
# ============================
# En FastAPI vas a escribir algo así (conceptual):
#
#   @app.get("/users/{user_id}")
#   async def get_user(user_id: int):
#       user = await db.fetch_user(user_id)  # I/O no bloqueante
#       return user
#
# El `async def` permite atender otras requests mientras espera la DB.


# ============================
# 🔹 Cuándo usar async
# ============================
# ✅ Esperas de red, DB, archivos (I/O bound)
# ❌ Cálculos pesados de CPU (mejor procesos/threads; async no magia CPU)


async def main():
    print("--- simple ---")
    await ejemplo_simple()
    print("--- concurrente ---")
    await ejemplo_concurrente()


if __name__ == "__main__":
    asyncio.run(main())

# ============================
# 🔹 Resumen
# ============================
# - async def → define corutina
# - await → espera un resultado sin bloquear el loop
# - asyncio.run(main()) → punto de entrada
# - asyncio.gather(...) → varias corutinas en paralelo
# - En FastAPI: endpoints async + await a I/O
