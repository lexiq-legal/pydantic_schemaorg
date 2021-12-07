from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class SiteNavigationElement(WebPageElement):
    """A navigation element of the page.

    See https://schema.org/SiteNavigationElement.

    """
    type_: str = Field("SiteNavigationElement", const=True, alias='@type')
    

SiteNavigationElement.update_forward_refs()
