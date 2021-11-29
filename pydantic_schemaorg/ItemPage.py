from pydantic import Field
from pydantic_schemaorg.WebPage import WebPage


class ItemPage(WebPage):
    """A page devoted to a single item, such as a particular product or hotel.

    See https://schema.org/ItemPage.

    """

    locals().update({"@type": Field("ItemPage", const=True)})


ItemPage.update_forward_refs()
