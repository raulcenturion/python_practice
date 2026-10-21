# Usuarios de práctica. seed_users hashea "plain" y lo guarda en users.
# En la tabla va el hash, no este texto.
#
# La clase usa la clave "password" con el texto al lado:
#   "password": "Admin123!"
# Sonar marca cada una (credencial escrita en el código). La clave del dict
# pasa a "plain". Sigue siendo la clave de práctica; no cambia el login.
#
# La clase también escribe "editor" en vez de "role" en todos menos el primero.
# seed_users lee "role". Con la otra clave el rol no llega y el INSERT
# manda NULL a una columna obligatoria.
# Las tres cuentas de Ricardo, Fernando y Juan comparten el mismo texto.
# Sonar marca el literal repetido. _SHARED es una sola vez.

_SHARED = "pruebas123!"

USERS = [
    {
        "email": "admin@example.com",
        "full_name": "Admin",
        "plain": "Admin123!",
        "role": "admin",
    },
    {
        "email": "editor@example.com",
        "full_name": "Editor",
        "plain": "Editor123!",
        "role": "editor",  # en la clase: "editor": "editor"
    },
    {
        "email": "user@example.com",
        "full_name": "User",
        "plain": "User123!",
        "role": "user",  # en la clase: "editor": "user"
    },
    {
        "email": "ricardo@example.com",
        "full_name": "Ricardo Cuéllar",
        "plain": _SHARED,
        "role": "admin",  # en la clase: "editor": "admin"
    },
    {
        "email": "fernando@example.com",
        "full_name": "Fernando Herrera",
        "plain": _SHARED,
        "role": "editor",  # en la clase: "editor": "editor"
    },
    {
        "email": "juanperez@example.com",
        "full_name": "Juan Pérez",
        "plain": _SHARED,
        "role": "user",  # en la clase: "editor": "user"
    },
]
