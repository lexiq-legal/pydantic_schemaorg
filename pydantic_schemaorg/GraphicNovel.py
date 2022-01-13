from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.BookFormatType import BookFormatType


class GraphicNovel(BookFormatType):
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.

    See: https://schema.org/GraphicNovel
    Model depth: 5
    """

    type_: str = Field("GraphicNovel", const=True, alias="@type")


if TYPE_CHECKING:

    GraphicNovel.update_forward_refs()
