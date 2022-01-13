from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Article import Article


class ScholarlyArticle(Article):
    """A scholarly article.

    See: https://schema.org/ScholarlyArticle
    Model depth: 4
    """

    type_: str = Field("ScholarlyArticle", const=True, alias="@type")


if TYPE_CHECKING:

    ScholarlyArticle.update_forward_refs()
