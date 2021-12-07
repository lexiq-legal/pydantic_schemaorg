from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class CollectionPage(WebPage):
    """Web page type: Collection page.

    See https://schema.org/CollectionPage.

    """
    type_: str = Field("CollectionPage", const=True, alias='@type')
    

CollectionPage.update_forward_refs()
