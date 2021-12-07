from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPAdBlock(WebPageElement):
    """An advertising section of the page.

    See https://schema.org/WPAdBlock.

    """
    type_: str = Field("WPAdBlock", const=True, alias='@type')
    

WPAdBlock.update_forward_refs()
