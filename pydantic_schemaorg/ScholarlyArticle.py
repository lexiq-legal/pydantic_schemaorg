from pydantic import Field
from pydantic_schemaorg.Article import Article


class ScholarlyArticle(Article):
    """A scholarly article.

    See https://schema.org/ScholarlyArticle.

    """
    type_: str = Field("ScholarlyArticle", const=True, alias='@type')
    

ScholarlyArticle.update_forward_refs()
