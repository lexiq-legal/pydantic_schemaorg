from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class AnalysisNewsArticle(NewsArticle):
    """An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting,"
     "incorporates the expertise of the author/producer, offering interpretations and"
     "conclusions.

    See https://schema.org/AnalysisNewsArticle.

    """

    locals().update({"@type": Field("AnalysisNewsArticle", const=True)})


AnalysisNewsArticle.update_forward_refs()
