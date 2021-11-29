from pydantic import Field
from pydantic_schema_org.OfferItemCondition import OfferItemCondition


class NewCondition(OfferItemCondition):
    """Indicates that the item is new.

    See https://schema.org/NewCondition.

    """

    locals().update({"@type": Field("NewCondition", const=True)})


NewCondition.update_forward_refs()
