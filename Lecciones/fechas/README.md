# Fechas — lecciones

Temas: `datetime` → HTTP/APIs → clases + cliente HTTP.

## Cómo correr

```bash
./r fechas/01 teoria
./r fechas/01
./r fechas/02 teoria
./r fechas/02
./r fechas/03 teoria
./r fechas/03
```

O directo:

```bash
.venv/bin/python Lecciones/fechas/01_dates/teoria.py
.venv/bin/python Lecciones/fechas/01_dates/practica.py
```

## Contenido

| # | Carpeta | Qué se ve |
|---|---------|-----------|
| 01 | `01_dates` | `datetime`, `timedelta`, `strftime`, timezone |
| 02 | `02_requests` | `urllib` vs `requests`, GET/POST/PUT, errores |
| 03 | `03_clases` | POO + cliente HTTP encapsulado |

## Tips

- Preferí `datetime.now(timezone.utc)` (fechas con zona).
- Para APIs de prueba usá `jsonplaceholder.typicode.com` (sin API key).
- Nunca subas claves reales al repo; usá variables de entorno.
