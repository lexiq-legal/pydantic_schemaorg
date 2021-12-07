from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ItemPage(WebPage):
    """A page devoted to a single item, such as a particular product or hotel.

    See https://schema.org/ItemPage.

    """
    type_: str = Field("ItemPage", const=True, alias='@type')
    

ItemPage.update_forward_refs()
