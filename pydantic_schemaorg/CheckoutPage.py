from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class CheckoutPage(WebPage):
    """Web page type: Checkout page.

    See https://schema.org/CheckoutPage.

    """
    type_: str = Field("CheckoutPage", const=True, alias='@type')
    

CheckoutPage.update_forward_refs()
