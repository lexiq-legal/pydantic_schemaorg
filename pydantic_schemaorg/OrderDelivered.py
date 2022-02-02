from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderDelivered(OrderStatus):
    """OrderStatus representing successful delivery of an order.

    See: https://schema.org/OrderDelivered
    Model depth: 6
    """
    type_: str = Field("OrderDelivered", alias='@type')
    

