from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class SiteNavigationElement(WebPageElement):
    """A navigation element of the page.

    See https://schema.org/SiteNavigationElement.

    """

    locals().update({"@type": Field("SiteNavigationElement", const=True)})


SiteNavigationElement.update_forward_refs()
