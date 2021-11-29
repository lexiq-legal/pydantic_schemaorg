from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class UsedCondition(OfferItemCondition):
    """Indicates that the item is used.

    See https://schema.org/UsedCondition.

    """

    locals().update({"@type": Field("UsedCondition", const=True)})


UsedCondition.update_forward_refs()
