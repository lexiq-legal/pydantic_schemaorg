from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class CheckoutPage(WebPage):
    """Web page type: Checkout page.

    See https://schema.org/CheckoutPage.

    """

    locals().update({"@type": Field("CheckoutPage", const=True)})


CheckoutPage.update_forward_refs()
