from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class InStock(ItemAvailability):
    """Indicates that the item is in stock.

    See https://schema.org/InStock.

    """

    locals().update({"@type": Field("InStock", const=True)})


InStock.update_forward_refs()
