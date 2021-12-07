from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle
from pydantic_schemaorg.CriticReview import CriticReview


class ReviewNewsArticle(NewsArticle, CriticReview):
    """A [[NewsArticle]] and [[CriticReview]] providing a professional critic's assessment"
     "of a service, product, performance, or artistic or literary work.

    See https://schema.org/ReviewNewsArticle.

    """
    type_: str = Field("ReviewNewsArticle", const=True, alias='@type')
    

ReviewNewsArticle.update_forward_refs()
