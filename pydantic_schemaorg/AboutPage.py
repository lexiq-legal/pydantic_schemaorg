from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class AboutPage(WebPage):
    """Web page type: About page.

    See: https://schema.org/AboutPage
    Model depth: 4
    """
    type_: str = Field("AboutPage", alias='@type')
    

