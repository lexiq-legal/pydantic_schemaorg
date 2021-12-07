from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderInTransit(OrderStatus):
    """OrderStatus representing that an order is in transit.

    See https://schema.org/OrderInTransit.

    """
    type_: str = Field("OrderInTransit", const=True, alias='@type')
    

OrderInTransit.update_forward_refs()
