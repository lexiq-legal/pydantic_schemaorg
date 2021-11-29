from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class PreOrder(ItemAvailability):
    """Indicates that the item is available for pre-order.

    See https://schema.org/PreOrder.

    """

    locals().update({"@type": Field("PreOrder", const=True)})


PreOrder.update_forward_refs()
