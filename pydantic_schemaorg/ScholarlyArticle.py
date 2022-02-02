from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Article import Article


class ScholarlyArticle(Article):
    """A scholarly article.

    See: https://schema.org/ScholarlyArticle
    Model depth: 4
    """
    type_: str = Field("ScholarlyArticle", alias='@type')
    

