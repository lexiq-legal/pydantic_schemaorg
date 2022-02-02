from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderCancelled(OrderStatus):
    """OrderStatus representing cancellation of an order.

    See: https://schema.org/OrderCancelled
    Model depth: 6
    """
    type_: str = Field("OrderCancelled", alias='@type')
    

