from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderInTransit(OrderStatus):
    """OrderStatus representing that an order is in transit.

    See https://schema.org/OrderInTransit.

    """

    locals().update({"@type": Field("OrderInTransit", const=True)})


OrderInTransit.update_forward_refs()
