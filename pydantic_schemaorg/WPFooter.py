from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPFooter(WebPageElement):
    """The footer section of the page.

    See: https://schema.org/WPFooter
    Model depth: 4
    """
    type_: str = Field("WPFooter", alias='@type')
    

