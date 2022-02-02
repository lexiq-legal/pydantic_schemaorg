from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class CheckoutPage(WebPage):
    """Web page type: Checkout page.

    See: https://schema.org/CheckoutPage
    Model depth: 4
    """
    type_: str = Field("CheckoutPage", alias='@type')
    

