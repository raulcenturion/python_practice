# Punto de entrada de los modelos.
# from app.models import PostORM  funciona porque este archivo reexporta las clases.
#
# El orden importa: post.py crea la tabla post_tags.
# tag.py la nombra como texto ("post_tags") y SQLAlchemy la busca cuando
# ya están importadas las tres clases, al final de este archivo.

# Sección 13. author.py se queda en el disco, pero ya no se importa.
# PostORM.author pasó a PostORM.user. Si este archivo siguiera importando
# AuthorORM, SQLAlchemy buscaría back_populates="author" y fallaría al arrancar.
# from .author import AuthorORM
from .category import CategoryORM
from .post import PostORM, post_tags
from .tag import TagORM
from .user import User

# __all__ dice qué nombres son públicos si alguien hace: from app.models import *
# User entra en la sección 11. CategoryORM entra en la 13.
# Importarlos acá registra las tablas en Base, y create_all las crea.
__all__ = ["CategoryORM", "PostORM", "TagORM", "User", "post_tags"]
