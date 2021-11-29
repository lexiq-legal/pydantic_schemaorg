from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class InStoreOnly(ItemAvailability):
    """Indicates that the item is available only at physical locations.

    See https://schema.org/InStoreOnly.

    """

    locals().update({"@type": Field("InStoreOnly", const=True)})


InStoreOnly.update_forward_refs()
