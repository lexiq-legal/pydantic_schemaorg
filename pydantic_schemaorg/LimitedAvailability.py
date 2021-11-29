from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class LimitedAvailability(ItemAvailability):
    """Indicates that the item has limited availability.

    See https://schema.org/LimitedAvailability.

    """

    locals().update({"@type": Field("LimitedAvailability", const=True)})


LimitedAvailability.update_forward_refs()
