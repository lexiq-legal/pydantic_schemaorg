from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPSideBar(WebPageElement):
    """A sidebar section of the page.

    See https://schema.org/WPSideBar.

    """
    type_: str = Field("WPSideBar", const=True, alias='@type')
    

WPSideBar.update_forward_refs()
