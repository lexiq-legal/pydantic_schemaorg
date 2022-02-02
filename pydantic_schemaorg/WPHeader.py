from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPHeader(WebPageElement):
    """The header section of the page.

    See: https://schema.org/WPHeader
    Model depth: 4
    """
    type_: str = Field("WPHeader", alias='@type')
    

