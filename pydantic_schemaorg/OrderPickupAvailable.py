from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderPickupAvailable(OrderStatus):
    """OrderStatus representing availability of an order for pickup.

    See: https://schema.org/OrderPickupAvailable
    Model depth: 6
    """

    type_: str = Field("OrderPickupAvailable", const=True, alias="@type")


if TYPE_CHECKING:

    OrderPickupAvailable.update_forward_refs()
