from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPAdBlock(WebPageElement):
    """An advertising section of the page.

    See: https://schema.org/WPAdBlock
    Model depth: 4
    """
    type_: str = Field("WPAdBlock", alias='@type')
    

