from pydantic import Field
from pydantic_schema_org.ItemAvailability import ItemAvailability


class BackOrder(ItemAvailability):
    """Indicates that the item is available on back order.

    See https://schema.org/BackOrder.

    """

    locals().update({"@type": Field("BackOrder", const=True)})


BackOrder.update_forward_refs()
