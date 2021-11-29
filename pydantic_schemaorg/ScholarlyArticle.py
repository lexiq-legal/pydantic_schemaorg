from pydantic import Field
from pydantic_schemaorg.Article import Article


class ScholarlyArticle(Article):
    """A scholarly article.

    See https://schema.org/ScholarlyArticle.

    """

    locals().update({"@type": Field("ScholarlyArticle", const=True)})


ScholarlyArticle.update_forward_refs()
