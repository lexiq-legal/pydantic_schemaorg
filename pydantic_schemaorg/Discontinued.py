from pydantic import Field
from pydantic_schemaorg.ItemAvailability import ItemAvailability


class Discontinued(ItemAvailability):
    """Indicates that the item has been discontinued.

    See https://schema.org/Discontinued.

    """

    locals().update({"@type": Field("Discontinued", const=True)})


Discontinued.update_forward_refs()
