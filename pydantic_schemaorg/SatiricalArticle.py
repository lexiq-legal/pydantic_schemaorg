from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.Article import Article


class SatiricalArticle(Article):
    """An [[Article]] whose content is primarily [[satirical]](https://en.wikipedia.org/wiki/Satire)"
     "in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not"
     "necessarily also a [[NewsArticle]]. [[ScholarlyArticle]]s are also sometimes satirized.

    See: https://schema.org/SatiricalArticle
    Model depth: 4
    """

    type_: str = Field("SatiricalArticle", const=True, alias="@type")


if TYPE_CHECKING:

    SatiricalArticle.update_forward_refs()
