from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class AskPublicNewsArticle(NewsArticle):
    """A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the"
     "public for input, insights, clarifications, anecdotes, documentation, etc., on an"
     "issue, for reporting purposes.

    See https://schema.org/AskPublicNewsArticle.

    """

    locals().update({"@type": Field("AskPublicNewsArticle", const=True)})


AskPublicNewsArticle.update_forward_refs()
