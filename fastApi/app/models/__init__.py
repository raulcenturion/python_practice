# Punto de entrada de los modelos.
# from app.models import PostORM  funciona porque este archivo reexporta las clases.
#
# El orden importa: post.py crea la tabla post_tags.
# tag.py la nombra como texto ("post_tags") y SQLAlchemy la busca cuando
# ya están importadas las tres clases, al final de este archivo.

from .author import AuthorORM
from .post import PostORM, post_tags
from .tag import TagORM
from .user import User

# __all__ dice qué nombres son públicos si alguien hace: from app.models import *
# User entra en la sección 11. Importarlo acá registra la tabla users en Base.
# create_all la crea porque el repository de posts ya importa este paquete.
__all__ = ["AuthorORM", "PostORM", "TagORM", "User", "post_tags"]
