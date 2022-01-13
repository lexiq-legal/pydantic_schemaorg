from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.NewsArticle import NewsArticle


class AskPublicNewsArticle(NewsArticle):
    """A [[NewsArticle]] expressing an open call by a [[NewsMediaOrganization]] asking the"
     "public for input, insights, clarifications, anecdotes, documentation, etc., on an"
     "issue, for reporting purposes.

    See: https://schema.org/AskPublicNewsArticle
    Model depth: 5
    """

    type_: str = Field("AskPublicNewsArticle", const=True, alias="@type")


if TYPE_CHECKING:

    AskPublicNewsArticle.update_forward_refs()
