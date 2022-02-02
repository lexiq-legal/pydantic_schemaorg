from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderReturned(OrderStatus):
    """OrderStatus representing that an order has been returned.

    See: https://schema.org/OrderReturned
    Model depth: 6
    """
    type_: str = Field("OrderReturned", alias='@type')
    

