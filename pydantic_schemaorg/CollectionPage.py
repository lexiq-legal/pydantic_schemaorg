from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class CollectionPage(WebPage):
    """Web page type: Collection page.

    See: https://schema.org/CollectionPage
    Model depth: 4
    """
    type_: str = Field("CollectionPage", alias='@type')
    

