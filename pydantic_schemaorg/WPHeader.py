from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPHeader(WebPageElement):
    """The header section of the page.

    See https://schema.org/WPHeader.

    """

    locals().update({"@type": Field("WPHeader", const=True)})


WPHeader.update_forward_refs()
