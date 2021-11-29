from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OutOfStock(ItemAvailability):
    """Indicates that the item is out of stock.

    See https://schema.org/OutOfStock.

    """

    locals().update({"@type": Field("OutOfStock", const=True)})


OutOfStock.update_forward_refs()
