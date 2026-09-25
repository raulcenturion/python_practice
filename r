#!/usr/bin/env bash
# Atajo para correr prácticas/teoría desde la raíz del repo.
#
# Uso:
#   ./r                          → practica.py de la carpeta actual
#   ./r practica                 → igual
#   ./r teoria                   → teoria.py de la carpeta actual
#   ./r 01                       → Lecciones/fundamentos/01_*/practica.py
#   ./r 01 teoria                → Lecciones/fundamentos/01_*/teoria.py
#   ./r 04 practica_operaciones  → Lecciones/fundamentos/04_*/practica_operaciones.py
#   ./r integradores/01          → Lecciones/integradores/01_*/practica.py
#   ./r integradores/00 14b      → previo repaso, un ejercicio
#   ./r logica/01                → Lecciones/logica/01_*/practica.py
#   ./r regex/02 teoria          → Lecciones/regex/02_*/teoria.py
#   ./r scraping/01              → Lecciones/scraping/01_*/practica.py
#   ./r fechas/01 teoria         → Lecciones/fechas/01_*/teoria.py
#   ./r fastapi/00               → fastApi/00_*_practica.py
#   ./r fastapi/00 teoria        → fastApi/00_*_teoria.py
#   ./r ruta/al/archivo.py       → ese archivo

set -e
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

if [[ -x "$ROOT/.venv/bin/python" ]]; then
  PY="$ROOT/.venv/bin/python"
else
  PY="python3"
fi

run_file() {
  local file="$1"
  shift
  if [[ ! -f "$file" ]]; then
    echo "No encontré: $file" >&2
    exit 1
  fi
  if [[ $# -gt 0 ]]; then
    echo "→ $PY $file $*"
  else
    echo "→ $PY $file"
  fi
  exec "$PY" "$file" "$@"
}

# Sin args: practica.py en el directorio desde donde se invocó (si no, cwd)
if [[ $# -eq 0 ]]; then
  if [[ -f "practica.py" ]]; then
    run_file "practica.py"
  fi
  echo "Uso: ./r 01   |   ./r 01 teoria   |   ./r practica   |   ./r archivo.py" >&2
  exit 1
fi

arg1="$1"
arg2="${2:-practica}"

# Ruta directa a un .py
if [[ "$arg1" == *.py ]]; then
  run_file "$arg1"
fi

# practica / teoria en carpeta actual
if [[ "$arg1" == "practica" || "$arg1" == "teoria" ]]; then
  run_file "${arg1}.py"
fi

# Número de lección fundamentos:
#   ./r 01
#   ./r 01 teoria
#   ./r 04 practica_operaciones
if [[ "$arg1" =~ ^[0-9]{1,2}$ ]]; then
  num=$(printf "%02d" "$((10#$arg1))")
  kind="$arg2"
  kind="${kind%.py}"  # permite ./r 04 practica_operaciones.py
  matches=(Lecciones/fundamentos/"${num}_"*/)
  if [[ ! -d "${matches[0]}" ]]; then
    echo "No hay lección fundamentos ${num}_*" >&2
    exit 1
  fi
  lesson_dir="${matches[0]}"

  if [[ "$kind" == "teoria" ]]; then
    if [[ -f "${lesson_dir}teoria.py" ]]; then
      run_file "${lesson_dir}teoria.py"
    fi
    t=( "${lesson_dir}"teoria_*.py )
    run_file "${t[0]}"
  fi

  # practica, practica_operaciones, u otro .py de la lección
  target="${lesson_dir}${kind}.py"
  if [[ -f "$target" ]]; then
    run_file "$target"
  fi

  echo "No encontré ${kind}.py en ${lesson_dir}" >&2
  echo "Archivos disponibles:" >&2
  ls -1 "$lesson_dir"*.py >&2
  exit 1
fi

# integradores:
#   ./r integradores/01
#   ./r integradores/00                 → 00_previo_* (primer match) + args
#   ./r integradores/00_previo 14b      → carpeta que coincida + ejercicio
#   ./r integradores/00_repaso_presupuesto
if [[ "$arg1" == integradores/* ]]; then
  rest="${arg1#integradores/}"
  extra=("${@:2}")

  # Si viene solo el número (00, 01…), glob num_*
  if [[ "$rest" =~ ^[0-9]{1,2}$ ]]; then
    num=$(printf "%02d" "$((10#$rest))")
    matches=(Lecciones/integradores/"${num}_"*/)
    if [[ ! -d "${matches[0]}" ]]; then
      echo "No hay integrador ${num}_*" >&2
      exit 1
    fi
    # Con varios 00_*, preferí el "previo" si existe; si no, el primero.
    target_dir="${matches[0]}"
    for m in "${matches[@]}"; do
      if [[ "$m" == *previo* ]]; then
        target_dir="$m"
        break
      fi
    done
    # Si el usuario pidió presupuesto explícitamente vía 2º token especial:
    if [[ "${extra[0]:-}" == "presupuesto" ]]; then
      for m in "${matches[@]}"; do
        if [[ "$m" == *presupuesto* ]]; then
          target_dir="$m"
          break
        fi
      done
      extra=("${extra[@]:1}")
    fi
    run_file "${target_dir}practica.py" "${extra[@]}"
  fi

  # Ruta/parcial de carpeta: integradores/00_previo  o  integradores/00_repaso_presupuesto
  matches=(Lecciones/integradores/*"${rest}"*/)
  if [[ ! -d "${matches[0]}" ]]; then
    matches=(Lecciones/integradores/"${rest}"*/)
  fi
  if [[ -d "${matches[0]}" ]]; then
    run_file "${matches[0]}practica.py" "${extra[@]}"
  fi

  echo "No encontré integrador que coincida con: $rest" >&2
  echo "Carpetas:" >&2
  ls -1d Lecciones/integradores/*/ >&2
  exit 1
fi

# Area lessons: ./r logica/01  |  ./r regex/02 teoria  |  ./r scraping/01  |  ./r fechas/01  |  ./r fastapi/00
if [[ "$arg1" == logica/* || "$arg1" == regex/* || "$arg1" == scraping/* || "$arg1" == fechas/* || "$arg1" == fastapi/* ]]; then
  area="${arg1%%/*}"
  # En disco la carpeta se llama fastApi (camelCase)
  if [[ "$area" == "fastapi" ]]; then
    area="fastApi"
  fi
  rest="${arg1#*/}"
  kind="${2:-practica}"
  kind="${kind%.py}"
  extra=("${@:3}")

  if [[ "$rest" =~ ^[0-9]{1,2}$ ]]; then
    num=$(printf "%02d" "$((10#$rest))")
    # fastApi: archivos en la raíz, no en una subcarpeta.
    #   00_hola_practica.py / 00_hola_teoria.py / 00_hola_main.py
    if [[ "$area" == "fastApi" ]]; then
      if [[ "$kind" == "teoria" ]]; then
        file=(fastApi/"${num}"_*_teoria.py)
      else
        file=(fastApi/"${num}"_*_practica.py)
      fi
      if [[ -f "${file[0]}" ]]; then
        run_file "${file[0]}" "${extra[@]}"
      fi
      echo "No hay ${kind} para fastapi/${num}" >&2
      ls -1 fastApi/"${num}"_*.py 2>/dev/null >&2 || true
      exit 1
    fi
    matches=(Lecciones/"${area}"/"${num}_"*/)
  else
    if [[ "$area" == "fastApi" ]]; then
      matches=("${area}"/*"${rest}"*/)
    else
      matches=(Lecciones/"${area}"/*"${rest}"*/)
    fi
  fi

  if [[ ! -d "${matches[0]}" ]]; then
    echo "No hay lección ${area}/${rest}" >&2
    if [[ "$area" == "fastApi" ]]; then
      ls -1d fastApi/*/ 2>/dev/null >&2 || true
    else
      ls -1d Lecciones/"${area}"/*/ 2>/dev/null >&2 || true
    fi
    exit 1
  fi

  lesson_dir="${matches[0]}"
  if [[ "$kind" == "teoria" ]]; then
    run_file "${lesson_dir}teoria.py" "${extra[@]}"
  fi
  if [[ -f "${lesson_dir}${kind}.py" ]]; then
    run_file "${lesson_dir}${kind}.py" "${extra[@]}"
  fi
  echo "No encontré ${kind}.py en ${lesson_dir}" >&2
  ls -1 "$lesson_dir"*.py 2>/dev/null >&2 || true
  exit 1
fi

echo "No entendí: $*" >&2
echo "Ejemplos: ./r 01  |  ./r 01 teoria  |  ./r integradores/00 14b  |  ./r logica/01  |  ./r fechas/01 teoria  |  ./r scraping/01" >&2
exit 1
