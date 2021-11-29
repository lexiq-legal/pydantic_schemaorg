from pydantic import Field
from pydantic_schema_org.WebPageElement import WebPageElement


class WPFooter(WebPageElement):
    """The footer section of the page.

    See https://schema.org/WPFooter.

    """

    locals().update({"@type": Field("WPFooter", const=True)})


WPFooter.update_forward_refs()
