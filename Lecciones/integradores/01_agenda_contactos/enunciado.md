# Integrador 01 — Agenda de contactos (fácil)

Cerrás la base del repo con un programa de consola completo.

## Objetivo

Una **agenda CLI** que permita alta, listado, búsqueda y borrado de contactos, guardando todo en un archivo JSON.

## Temas que integra

- Tipos, casting, strings, f-strings
- Listas y diccionarios
- `if` / `while` (menú)
- Funciones con parámetros y retorno
- Archivos + `json`
- `try` / `except` básico (input inválido, archivo faltante)

## Requisitos funcionales

1. Menú en bucle hasta elegir “Salir”:
   - 1) Agregar contacto
   - 2) Listar contactos
   - 3) Buscar por nombre
   - 4) Eliminar por nombre
   - 5) Salir
2. Cada contacto: `nombre` (str), `telefono` (str), `email` (str), `edad` (int).
3. Persistencia en `contactos.json` (misma carpeta).
4. Al iniciar, cargá el JSON si existe; si no, empezá con lista vacía.
5. No dejes que el programa se rompa si el usuario escribe basura en el menú o en la edad.

## Criterios de aceptación

- [ ] El menú vuelve a mostrarse después de cada acción
- [ ] Los contactos sobreviven al cerrar y volver a abrir el programa
- [ ] Buscar es case-insensitive (`ana` encuentra `Ana`)
- [ ] Eliminar avisa si el contacto no existe
- [ ] Edad inválida se maneja con mensaje claro (sin traceback)

## Cómo entregar

Completá `practica.py`. Ejecutá:

```bash
python practica.py
```

## Tip general

Empezá por las funciones `cargar` / `guardar`. El menú queda más fácil cuando la persistencia ya anda.
