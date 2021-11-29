from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class ItemAvailability(Enumeration):
    """A list of possible product availability options.

    See https://schema.org/ItemAvailability.

    """

    locals().update({"@type": Field("ItemAvailability", const=True)})


ItemAvailability.update_forward_refs()
