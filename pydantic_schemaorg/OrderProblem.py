from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderProblem(OrderStatus):
    """OrderStatus representing that there is a problem with the order.

    See https://schema.org/OrderProblem.

    """
    type_: str = Field("OrderProblem", const=True, alias='@type')
    

OrderProblem.update_forward_refs()
