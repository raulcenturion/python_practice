# Sección 9. Script de ejemplo, no es parte de la API.
# Mide cuánto tardan varios GET al mismo tiempo contra /posts/async o /posts/sync.
#
# Está comentado para que no dispare requests al correr el archivo por accidente.
# Para usarlo:
#   1. En app/api/v1/posts/router.py descomentá la ruta /async (o /sync).
#   2. Desde la carpeta fastapi/, con el venv activo: fastapi dev app/main.py
#   3. Descomentá el bloque de abajo y corré: python request_test.py
#
# Qué se espera ver:
#   Cuatro pedidos juntos, cada ruta de la clase espera 8 segundos fijos.
#   Contra /async, el tiempo total de pared queda cerca de 8 s: las esperas se solapan
#   porque await asyncio.sleep suelta el event loop.
#   Contra /sync, time.sleep retiene un hilo por pedido. Con pocos pedidos el pool
#   de hilos de FastAPI también los solapa. La diferencia se nota cuando hay muchos
#   pedidos sync a la vez: cada sleep ocupa un hilo y los demás esperan turno.
#
# El script manda ?t=3, 5.5, 7.8 y 9.7. La ruta de la clase no usa t, así que
# ese número no cambia los 8 segundos. Quedó así en el ejemplo de la clase.
#
# asyncio  → biblioteca estándar. gather dispara las cuatro corrutinas juntas.
# httpx    → cliente HTTP. AsyncClient es la versión async (hay que await).
# time     → biblioteca estándar. perf_counter mide segundos reales, no el sleep del server.

# import asyncio
# import time
#
# import httpx
#
# URL = "http://127.0.0.1:8000/posts/async"
#
#
# async def hit(t, client: httpx.AsyncClient):
#     # t es la duración que el script quisiera pedir. La ruta de la clase lo ignora.
#     start = time.perf_counter()
#     r = await client.get(URL, params={"t": t})
#     elapsed = time.perf_counter() - start
#     return t, elapsed, r.json()
#
#
# async def main():
#     # El timeout tiene que ser mayor que la espera del server (8 s en la clase).
#     timeout = httpx.Timeout(20.0)
#     # Límites de conexiones abiertas al mismo tiempo contra el server local.
#     limits = httpx.Limits(max_keepalive_connections=10, max_connections=20)
#
#     async with httpx.AsyncClient(timeout=timeout, limits=limits) as client:
#         start = time.perf_counter()
#         # gather espera a las cuatro. return_exceptions=True no corta si una falla:
#         # la excepción vuelve dentro de la lista y se imprime abajo.
#         results = await asyncio.gather(
#             hit(3.0, client),
#             hit(5.5, client),
#             hit(7.8, client),
#             hit(9.7, client),
#             return_exceptions=True,
#         )
#         total = time.perf_counter() - start
#
#     print("\n--- Resultados ---")
#     for res in results:
#         if isinstance(res, Exception):
#             print("Error:", repr(res))
#         else:
#             t, elapsed, body = res
#             print(f"sleep={t:<4}  tardó={elapsed:.2f}s  respuesta={body}")
#     print(f"\nTiempo total de pared: {total:.2f}s\n")
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
