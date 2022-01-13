from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WebPageElement import WebPageElement


class WPHeader(WebPageElement):
    """The header section of the page.

    See: https://schema.org/WPHeader
    Model depth: 4
    """

    type_: str = Field("WPHeader", const=True, alias="@type")


if TYPE_CHECKING:

    WPHeader.update_forward_refs()
