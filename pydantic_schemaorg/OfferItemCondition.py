from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class OfferItemCondition(Enumeration):
    """A list of possible conditions for the item.

    See https://schema.org/OfferItemCondition.

    """

    locals().update({"@type": Field("OfferItemCondition", const=True)})


OfferItemCondition.update_forward_refs()
