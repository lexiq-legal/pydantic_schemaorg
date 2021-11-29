from pydantic import Field
from pydantic_schemaorg.OfferItemCondition import OfferItemCondition


class RefurbishedCondition(OfferItemCondition):
    """Indicates that the item is refurbished.

    See https://schema.org/RefurbishedCondition.

    """

    locals().update({"@type": Field("RefurbishedCondition", const=True)})


RefurbishedCondition.update_forward_refs()
