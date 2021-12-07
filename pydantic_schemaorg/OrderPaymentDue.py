from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderPaymentDue(OrderStatus):
    """OrderStatus representing that payment is due on an order.

    See https://schema.org/OrderPaymentDue.

    """
    type_: str = Field("OrderPaymentDue", const=True, alias='@type')
    

OrderPaymentDue.update_forward_refs()
