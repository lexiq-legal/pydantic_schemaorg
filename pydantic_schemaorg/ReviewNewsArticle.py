from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.CriticReview import CriticReview

from pydantic_schemaorg.NewsArticle import NewsArticle


class ReviewNewsArticle(CriticReview, NewsArticle):
    """A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment"
     "of a service, product, performance, or artistic or literary work.

    See: https://schema.org/ReviewNewsArticle
    Model depth: 5
    """

    type_: str = Field("ReviewNewsArticle", const=True, alias="@type")


if TYPE_CHECKING:

    ReviewNewsArticle.update_forward_refs()
