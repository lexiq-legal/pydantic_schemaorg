from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderProcessing(OrderStatus):
    """OrderStatus representing that an order is being processed.

    See: https://schema.org/OrderProcessing
    Model depth: 6
    """
    type_: str = Field("OrderProcessing", alias='@type')
    

