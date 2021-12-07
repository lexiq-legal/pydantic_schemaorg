from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderDelivered(OrderStatus):
    """OrderStatus representing successful delivery of an order.

    See https://schema.org/OrderDelivered.

    """
    type_: str = Field("OrderDelivered", const=True, alias='@type')
    

OrderDelivered.update_forward_refs()
