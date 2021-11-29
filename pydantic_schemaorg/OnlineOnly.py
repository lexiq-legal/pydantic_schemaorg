from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OnlineOnly(ItemAvailability):
    """Indicates that the item is available only online.

    See https://schema.org/OnlineOnly.

    """

    locals().update({"@type": Field("OnlineOnly", const=True)})


OnlineOnly.update_forward_refs()
