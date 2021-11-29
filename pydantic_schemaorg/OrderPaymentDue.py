from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderPaymentDue(OrderStatus):
    """OrderStatus representing that payment is due on an order.

    See https://schema.org/OrderPaymentDue.

    """

    locals().update({"@type": Field("OrderPaymentDue", const=True)})


OrderPaymentDue.update_forward_refs()
