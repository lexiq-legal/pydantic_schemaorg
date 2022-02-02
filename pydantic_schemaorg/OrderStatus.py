from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.StatusEnumeration import StatusEnumeration


class OrderStatus(StatusEnumeration):
    """Enumerated status values for Order.

    See: https://schema.org/OrderStatus
    Model depth: 5
    """
    type_: str = Field("OrderStatus", alias='@type')
    

