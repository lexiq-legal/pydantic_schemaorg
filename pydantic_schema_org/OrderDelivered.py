from pydantic import Field
from pydantic_schema_org.OrderStatus import OrderStatus


class OrderDelivered(OrderStatus):
    """OrderStatus representing successful delivery of an order.

    See https://schema.org/OrderDelivered.

    """

    locals().update({"@type": Field("OrderDelivered", const=True)})


OrderDelivered.update_forward_refs()
