from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WebPageElement import WebPageElement


class SiteNavigationElement(WebPageElement):
    """A navigation element of the page.

    See: https://schema.org/SiteNavigationElement
    Model depth: 4
    """

    type_: str = Field("SiteNavigationElement", const=True, alias="@type")


if TYPE_CHECKING:

    SiteNavigationElement.update_forward_refs()
