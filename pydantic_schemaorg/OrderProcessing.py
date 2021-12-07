from pydantic import Field
from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderProcessing(OrderStatus):
    """OrderStatus representing that an order is being processed.

    See https://schema.org/OrderProcessing.

    """
    type_: str = Field("OrderProcessing", const=True, alias='@type')
    

OrderProcessing.update_forward_refs()
