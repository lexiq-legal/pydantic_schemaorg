from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ContactPage(WebPage):
    """Web page type: Contact page.

    See https://schema.org/ContactPage.

    """

    locals().update({"@type": Field("ContactPage", const=True)})


ContactPage.update_forward_refs()
