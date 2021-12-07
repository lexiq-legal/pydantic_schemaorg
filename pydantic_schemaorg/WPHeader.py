from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPHeader(WebPageElement):
    """The header section of the page.

    See https://schema.org/WPHeader.

    """
    type_: str = Field("WPHeader", const=True, alias='@type')
    

WPHeader.update_forward_refs()
