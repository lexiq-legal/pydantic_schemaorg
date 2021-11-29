from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderProblem(OrderStatus):
    """OrderStatus representing that there is a problem with the order.

    See https://schema.org/OrderProblem.

    """

    locals().update({"@type": Field("OrderProblem", const=True)})


OrderProblem.update_forward_refs()
