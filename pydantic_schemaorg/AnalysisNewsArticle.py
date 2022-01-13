from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.NewsArticle import NewsArticle


class AnalysisNewsArticle(NewsArticle):
    """An AnalysisNewsArticle is a [[NewsArticle]] that, while based on factual reporting,"
     "incorporates the expertise of the author/producer, offering interpretations and"
     "conclusions.

    See: https://schema.org/AnalysisNewsArticle
    Model depth: 5
    """

    type_: str = Field("AnalysisNewsArticle", const=True, alias="@type")


if TYPE_CHECKING:

    AnalysisNewsArticle.update_forward_refs()
