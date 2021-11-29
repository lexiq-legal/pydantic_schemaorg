from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderPickupAvailable(OrderStatus):
    """OrderStatus representing availability of an order for pickup.

    See https://schema.org/OrderPickupAvailable.

    """

    locals().update({"@type": Field("OrderPickupAvailable", const=True)})


OrderPickupAvailable.update_forward_refs()
