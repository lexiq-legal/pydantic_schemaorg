from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderPickupAvailable(OrderStatus):
    """OrderStatus representing availability of an order for pickup.

    See https://schema.org/OrderPickupAvailable.

    """
    type_: str = Field("OrderPickupAvailable", const=True, alias='@type')
    

OrderPickupAvailable.update_forward_refs()
