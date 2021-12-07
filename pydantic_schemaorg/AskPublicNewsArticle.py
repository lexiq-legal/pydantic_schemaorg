from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class AskPublicNewsArticle(NewsArticle):
    """A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the"
     "public for input, insights, clarifications, anecdotes, documentation, etc., on an"
     "issue, for reporting purposes.

    See https://schema.org/AskPublicNewsArticle.

    """
    type_: str = Field("AskPublicNewsArticle", const=True, alias='@type')
    

AskPublicNewsArticle.update_forward_refs()
