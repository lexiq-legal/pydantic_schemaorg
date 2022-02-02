from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class SiteNavigationElement(WebPageElement):
    """A navigation element of the page.

    See: https://schema.org/SiteNavigationElement
    Model depth: 4
    """
    type_: str = Field("SiteNavigationElement", alias='@type')
    

