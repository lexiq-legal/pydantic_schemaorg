from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class AboutPage(WebPage):
    """Web page type: About page.

    See https://schema.org/AboutPage.

    """
    type_: str = Field("AboutPage", const=True, alias='@type')
    

AboutPage.update_forward_refs()
