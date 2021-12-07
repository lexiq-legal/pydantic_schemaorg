from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class OrderStatus(StatusEnumeration):
    """Enumerated status values for Order.

    See https://schema.org/OrderStatus.

    """
    type_: str = Field("OrderStatus", const=True, alias='@type')
    

OrderStatus.update_forward_refs()
