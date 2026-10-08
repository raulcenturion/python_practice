# Punto de entrada de los modelos.
# from app.models import PostORM  funciona porque este archivo reexporta las clases.
#
# El orden importa: post.py crea la tabla post_tags.
# tag.py la nombra como texto ("post_tags") y SQLAlchemy la busca cuando
# ya están importadas las tres clases, al final de este archivo.

from .author import AuthorORM
from .post import PostORM, post_tags
from .tag import TagORM

# __all__ dice qué nombres son públicos si alguien hace: from app.models import *
__all__ = ["AuthorORM", "PostORM", "TagORM", "post_tags"]
