from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Article import Article


class AdvertiserContentArticle(Article):
    """An [[Article]] that an external entity has paid to place or to produce to its specifications."
     "Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored"
     "content, native advertising and other paid content.

    See: https://schema.org/AdvertiserContentArticle
    Model depth: 4
    """
    type_: str = Field("AdvertiserContentArticle", alias='@type')
    

