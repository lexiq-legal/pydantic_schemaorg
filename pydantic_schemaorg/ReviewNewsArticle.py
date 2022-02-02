from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle
from pydantic_schemaorg.CriticReview import CriticReview


class ReviewNewsArticle(NewsArticle, CriticReview):
    """A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment"
     "of a service, product, performance, or artistic or literary work.

    See: https://schema.org/ReviewNewsArticle
    Model depth: 5
    """
    type_: str = Field("ReviewNewsArticle", alias='@type')
    

