from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderProcessing(OrderStatus):
    """OrderStatus representing that an order is being processed.

    See https://schema.org/OrderProcessing.

    """

    locals().update({"@type": Field("OrderProcessing", const=True)})


OrderProcessing.update_forward_refs()
