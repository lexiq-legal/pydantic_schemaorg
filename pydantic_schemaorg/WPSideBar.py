from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPSideBar(WebPageElement):
    """A sidebar section of the page.

    See: https://schema.org/WPSideBar
    Model depth: 4
    """
    type_: str = Field("WPSideBar", alias='@type')
    

