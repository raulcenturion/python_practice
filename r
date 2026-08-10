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
  if [[ ! -f "$file" ]]; then
    echo "No encontré: $file" >&2
    exit 1
  fi
  echo "→ $PY $file"
  exec "$PY" "$file"
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

# integradores: ./r integradores/01
if [[ "$arg1" == integradores/* ]]; then
  num="${arg1#integradores/}"
  num=$(printf "%02d" "$((10#$num))")
  matches=(Lecciones/integradores/"${num}_"*/)
  run_file "${matches[0]}practica.py"
fi

echo "No entendí: $*" >&2
echo "Ejemplos: ./r 01  |  ./r 01 teoria  |  ./r 04 practica_operaciones  |  ./r integradores/01" >&2
exit 1
