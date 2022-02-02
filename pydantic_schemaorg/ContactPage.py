from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ContactPage(WebPage):
    """Web page type: Contact page.

    See: https://schema.org/ContactPage
    Model depth: 4
    """
    type_: str = Field("ContactPage", alias='@type')
    

