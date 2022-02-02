from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderPaymentDue(OrderStatus):
    """OrderStatus representing that payment is due on an order.

    See: https://schema.org/OrderPaymentDue
    Model depth: 6
    """
    type_: str = Field("OrderPaymentDue", alias='@type')
    

