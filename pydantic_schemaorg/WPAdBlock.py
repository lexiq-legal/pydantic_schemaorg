from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WebPageElement import WebPageElement


class WPAdBlock(WebPageElement):
    """An advertising section of the page.

    See: https://schema.org/WPAdBlock
    Model depth: 4
    """

    type_: str = Field("WPAdBlock", const=True, alias="@type")


if TYPE_CHECKING:

    WPAdBlock.update_forward_refs()
