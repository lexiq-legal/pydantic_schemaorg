from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class SoldOut(ItemAvailability):
    """Indicates that the item has sold out.

    See https://schema.org/SoldOut.

    """

    locals().update({"@type": Field("SoldOut", const=True)})


SoldOut.update_forward_refs()
