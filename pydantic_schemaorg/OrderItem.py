from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional, Any

from pydantic_schemaorg.Intangible import Intangible


class OrderItem(Intangible):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought"
     "offer.

    See: https://schema.org/OrderItem
    Model depth: 3
    """

    type_: str = Field("OrderItem", const=True, alias="@type")
    orderDelivery: "Optional[Union[List[Union[ParcelDelivery, str]], Union[ParcelDelivery, str]]]" = Field(
        None,
        description="The delivery of the parcel related to this order or order item.",
    )
    orderedItem: "Optional[Union[List[Union['OrderItem', Product, Service, str]], Union['OrderItem', Product, Service, str]]]" = Field(
        None,
        description="The item ordered.",
    )
    orderQuantity: "Optional[Union[List[Union[Decimal, str]], Union[Decimal, str]]]" = Field(
        None,
        description="The number of the item ordered. If the property is not set, assume the quantity is one.",
    )
    orderItemNumber: "Optional[Union[List[str], str]]" = Field(
        None,
        description="The identifier of the order item.",
    )
    orderItemStatus: "Optional[Union[List[Union[OrderStatus, str]], Union[OrderStatus, str]]]" = Field(
        None,
        description="The current status of the order item.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.ParcelDelivery import ParcelDelivery

    from pydantic_schemaorg.Product import Product

    from pydantic_schemaorg.Service import Service

    from decimal import Decimal

    from pydantic_schemaorg.OrderStatus import OrderStatus

    OrderItem.update_forward_refs()
