from pydantic import Field
from pydantic_schema_org.OfferItemCondition import OfferItemCondition


class DamagedCondition(OfferItemCondition):
    """Indicates that the item is damaged.

    See https://schema.org/DamagedCondition.

    """

    locals().update({"@type": Field("DamagedCondition", const=True)})


DamagedCondition.update_forward_refs()
