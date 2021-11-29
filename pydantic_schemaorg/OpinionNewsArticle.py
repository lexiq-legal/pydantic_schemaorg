from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class OpinionNewsArticle(NewsArticle):
    """An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions"
     "rather than journalistic reporting of news and events. For example, a [[NewsArticle]]"
     "consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of"
     "a news publication.

    See https://schema.org/OpinionNewsArticle.

    """

    locals().update({"@type": Field("OpinionNewsArticle", const=True)})


OpinionNewsArticle.update_forward_refs()
