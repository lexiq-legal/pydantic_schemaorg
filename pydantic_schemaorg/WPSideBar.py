from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WebPageElement import WebPageElement


class WPSideBar(WebPageElement):
    """A sidebar section of the page.

    See: https://schema.org/WPSideBar
    Model depth: 4
    """

    type_: str = Field("WPSideBar", const=True, alias="@type")


if TYPE_CHECKING:

    WPSideBar.update_forward_refs()
