from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderReturned(OrderStatus):
    """OrderStatus representing that an order has been returned.

    See https://schema.org/OrderReturned.

    """

    locals().update({"@type": Field("OrderReturned", const=True)})


OrderReturned.update_forward_refs()
