from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from decimal import Decimal


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class OrderItem(Intangible):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought"
     "offer.

    See: https://schema.org/OrderItem
    Model depth: 3
    """
    type_: str = Field(default="OrderItem", alias='@type', constant=True)
    orderDelivery: Optional[Union[List[Union['ParcelDelivery', str]], 'ParcelDelivery', str]] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",
    )
    orderedItem: Optional[Union[List[Union['Service', 'OrderItem', 'Product', str]], 'Service', 'OrderItem', 'Product', str]] = Field(
        default=None,
        description="The item ordered.",
    )
    orderQuantity: Optional[Union[List[Union[int, float, 'Number', str]], int, float, 'Number', str]] = Field(
        default=None,
        description="The number of the item ordered. If the property is not set, assume the quantity is one.",
    )
    orderItemNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The identifier of the order item.",
    )
    orderItemStatus: Optional[Union[List[Union['OrderStatus', str]], 'OrderStatus', str]] = Field(
        default=None,
        description="The current status of the order item.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.ParcelDelivery import ParcelDelivery
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.OrderStatus import OrderStatus
