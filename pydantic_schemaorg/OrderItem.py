from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.Service import Service
from pydantic_schemaorg.Product import Product
from decimal import Decimal
from pydantic_schemaorg.OrderStatus import OrderStatus
from pydantic_schemaorg.Intangible import Intangible


class OrderItem(Intangible):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought"
     "offer.

    See https://schema.org/OrderItem.

    """

    orderDelivery: Any = Field(
        None,
        description="The delivery of the parcel related to this order or order item.",
    )
    orderedItem: Union[List[Union[Service, Product, Any]], Union[Service, Product, Any]] = Field(
        None,
        description="The item ordered.",
    )
    orderQuantity: Optional[Union[List[Decimal], Decimal]] = Field(
        None,
        description="The number of the item ordered. If the property is not set, assume the quantity is one.",
    )
    orderItemNumber: Optional[Union[List[str], str]] = Field(
        None,
        description="The identifier of the order item.",
    )
    orderItemStatus: Optional[Union[List[OrderStatus], OrderStatus]] = Field(
        None,
        description="The current status of the order item.",
    )
    locals().update({"@type": Field("OrderItem", const=True)})


OrderItem.update_forward_refs()
