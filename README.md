# welcomePy

Repo de estudio de Python: teoría + prácticas alineadas (base previa a FastAPI).

## Estructura

```text
Clases_teoria/     → teoría por tema
  fundamentos/
  fechas/
  logica/
  regex/
  scraping/

Ejercicios/        → enunciados y prácticas (espejo de la teoría)
  fundamentos/
  fechas/
  logica/
  regex/
  scraping/
```

## Cómo estudiar

1. Leé el tema en `Clases_teoria/<tema>/...`
2. Resolvé el archivo correspondiente en `Ejercicios/<tema>/...`
3. Cada ejercicio apunta a su teoría en el encabezado (`📘 Teoría: ...`)

## Checklist pre-FastAPI

| Tema | Teoría | Práctica | Estado |
|------|--------|----------|--------|
| Variables y tipos | `fundamentos/02`–`04` | `02`, `04`, `04b` | Cubierto |
| Listas / dict / tuplas / sets | `08`–`09`, `14`, `22`–`23` | `07`, `11` | Cubierto |
| if / for / while | `06`, `10`–`12` | `06`, `08`, `09` | Cubierto |
| Funciones y módulos | `13`, `17` | `10`, `15` | Cubierto |
| try/except + excepciones custom | `16` | `13` | Cubierto |
| Clases y herencia | `15`, `19` | `12` | Cubierto |
| Modelos de datos (Pydantic) | `29_modelos_datos_pydantic` | `18_modelos_datos_pydantic` | Cubierto |
| Archivos y JSON | `20`, `21` | `15` | Cubierto |
| venv + pip + requirements | `27_entornos_virtuales` (+ `26`) | `16_entornos_virtuales` | Cubierto |
| Decoradores (`@app.get` style) | `25_decoradores` | `14_hof_decoradores` | Cubierto |
| async / await | `28_async_await` | `17_async_await` | Cubierto |

## Fundamentos (orden sugerido)

| Ejercicio | Teoría |
|----------|--------|
| `01_print.py` | `01_print_comentarios.py` |
| `02_tipos_de_datos.py` | `02_tipos_de_datos.py` |
| `03_casting.py` | `03_casting.py` |
| `04_variables.py` | `04_variables.py` |
| `04b_operaciones_aritmeticas.py` | `04_variables.py` (operadores) |
| `05_input_strings.py` | `05_input.py` |
| `06_condicionales_booleanos.py` | `06` + `07` |
| `07_listas.py` | `08` + `09` |
| `08_while.py` | `10_while.py` |
| `09_for_rangos.py` | `11` + `12` |
| `10_funciones.py` | `13_funciones.py` |
| `11_diccionarios_tuplas_sets.py` | `22` + `23` + `14` |
| `12_clases_poo.py` | `15` + `19` |
| `13_excepciones.py` | `16_excepciones.py` |
| `14_hof_decoradores.py` | `24` + `25` |
| `15_modulos_ficheros_json.py` | `17` + `20` + `21` |
| `16_entornos_virtuales.py` | `27_entornos_virtuales.py` |
| `17_async_await.py` | `28_async_await.py` |
| `18_modelos_datos_pydantic.py` | `29_modelos_datos_pydantic.py` |
