from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPSideBar(WebPageElement):
    """A sidebar section of the page.

    See https://schema.org/WPSideBar.

    """

    locals().update({"@type": Field("WPSideBar", const=True)})


WPSideBar.update_forward_refs()
