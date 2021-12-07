from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ContactPage(WebPage):
    """Web page type: Contact page.

    See https://schema.org/ContactPage.

    """
    type_: str = Field("ContactPage", const=True, alias='@type')
    

ContactPage.update_forward_refs()
