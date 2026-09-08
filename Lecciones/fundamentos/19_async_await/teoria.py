# ============================
# 📘 Asincronía: async / await
# ============================
# FastAPI usa funciones async para no bloquear el servidor mientras
# espera I/O (DB, HTTP, disco). Acá está la base de Python.
#
# Analogía rápida:
#   sync  → hacer cola en un solo mostrador (uno espera, nadie más avanza)
#   async → mientras esperás el café, el barista atiende a otra persona

import asyncio
import time

print("--- Lección 19: async / await ---")

# ============================
# 🔹 Conceptos
# ============================
# - Corutina: función definida con `async def`. No se ejecuta al llamarla;
#   retorna un objeto coroutine que hay que `await` o pasar a asyncio.run().
# - await: pausa la corutina actual hasta que termine otra awaitable,
#   y libera el event loop para hacer otra cosa.
# - Event loop: el motor que agenda y ejecuta corutinas.

# --- Async / Await / Event Loop ---
#
# async → declara una función asíncrona.
#   Ejemplo: async def tarea(): return "listo"
#   Permite pausar ejecución y ceder control al event loop.
#
# await → se usa dentro de funciones async.
#   Espera el resultado de otra función asíncrona.
#   Ejemplo: resultado = await tarea()
#
# Event loop → motor que coordina tareas asíncronas.
#   Ejecuta funciones async, espera resultados y sigue con otras tareas.
#   Se maneja con asyncio.run(main()) en Python.
#
# --- En FastAPI ---
# - Los endpoints pueden ser async def.
# - FastAPI usa el event loop para manejar múltiples requests en paralelo.
# - Ejemplo:
#   @app.get("/ping")
#   async def ping():
#       return {"status": "ok"}
#
# --- Buenas prácticas ---
# - Usar async/await en operaciones de I/O (consultas a DB, llamadas HTTP).
# - No usar async innecesariamente en funciones que solo hacen cálculos simples.
# - Recordar que el event loop coordina todo: no bloquearlo con operaciones largas.

# ============================
# 🔹 Función sync vs async
# ============================


def tarea_sync(nombre: str, segundos: float) -> str:
    # time.sleep bloquea TODO el hilo: nadie más puede avanzar mientras duerme.
    time.sleep(segundos)
    return f"{nombre} listo (sync)"


async def tarea_async(nombre: str, segundos: float) -> str:
    # asyncio.sleep es awaitable: cede el control al event loop durante la espera.
    # Otras corutinas pueden correr en ese “tiempo muerto”.
    await asyncio.sleep(segundos)
    return f"{nombre} listo (async)"


# ============================
# 🔹 Ejecutar una corutina (await)
# ============================
async def ejemplo_simple():
    # await espera el resultado de tarea_async antes de seguir.
    # Sin await, solo tendrías el objeto coroutine sin ejecutar.
    resultado = await tarea_async("A", 0.2)
    print("resultado:", resultado)


# ============================
# 🔹 Concurrencia con gather
# ============================
# Tres tareas de 0.3s en paralelo ≈ 0.3s total (no 0.9s).
# gather lanza varias corutinas y espera a que terminen TODAS.
async def ejemplo_concurrente():
    inicio = time.perf_counter()  # reloj de alta precisión
    # Las tres empiezan “a la vez” (cooperan en el mismo event loop).
    resultados = await asyncio.gather(
        tarea_async("download-1", 0.3),
        tarea_async("download-2", 0.3),
        tarea_async("download-3", 0.3),
    )
    duracion = time.perf_counter() - inicio
    print("resultados:", resultados)
    # Debería rondar ~0.30s, no ~0.90s (prueba de concurrencia).
    print("Tiempo total concurrente:", f"{duracion:.2f}s")


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
    # main agrupa los ejemplos; asyncio.run lo arranca desde el mundo sync.
    print("\n--- Ejemplo simple (await) ---")
    await ejemplo_simple()
    print("\n--- Ejemplo concurrente (gather) ---")
    await ejemplo_concurrente()


if __name__ == "__main__":
    # asyncio.run crea el event loop, ejecuta main() y lo cierra al terminar.
    # Es el punto de entrada típico de un script async.
    asyncio.run(main())

# ============================
# 🔹 Resumen
# ============================
# - async def → define una corutina (no se ejecuta al llamarla sola)
# - await → espera un resultado sin bloquear el event loop
# - asyncio.run(main()) → punto de entrada desde código sync
# - asyncio.gather(...) → varias corutinas en paralelo (I/O)
# - time.sleep bloquea; asyncio.sleep cede el control
# - En FastAPI: endpoints async + await a I/O (DB, HTTP, etc.)
# 💡 Async brilla con esperas; no acelera cálculos de CPU por sí solo
