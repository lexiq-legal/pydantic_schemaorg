from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderCancelled(OrderStatus):
    """OrderStatus representing cancellation of an order.

    See https://schema.org/OrderCancelled.

    """
    type_: str = Field("OrderCancelled", const=True, alias='@type')
    

OrderCancelled.update_forward_refs()
