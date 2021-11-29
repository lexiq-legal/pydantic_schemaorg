from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderCancelled(OrderStatus):
    """OrderStatus representing cancellation of an order.

    See https://schema.org/OrderCancelled.

    """

    locals().update({"@type": Field("OrderCancelled", const=True)})


OrderCancelled.update_forward_refs()
