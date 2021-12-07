from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPFooter(WebPageElement):
    """The footer section of the page.

    See https://schema.org/WPFooter.

    """
    type_: str = Field("WPFooter", const=True, alias='@type')
    

WPFooter.update_forward_refs()
