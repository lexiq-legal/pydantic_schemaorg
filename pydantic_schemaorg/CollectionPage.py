from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class CollectionPage(WebPage):
    """Web page type: Collection page.

    See https://schema.org/CollectionPage.

    """

    locals().update({"@type": Field("CollectionPage", const=True)})


CollectionPage.update_forward_refs()
