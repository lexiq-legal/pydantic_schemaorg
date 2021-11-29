from pydantic import Field
from pydantic_schemaorg.WebPageElement import WebPageElement


class WPAdBlock(WebPageElement):
    """An advertising section of the page.

    See https://schema.org/WPAdBlock.

    """

    locals().update({"@type": Field("WPAdBlock", const=True)})


WPAdBlock.update_forward_refs()
