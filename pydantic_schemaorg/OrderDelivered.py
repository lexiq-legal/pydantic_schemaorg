from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderDelivered(OrderStatus):
    """OrderStatus representing successful delivery of an order.

    See: https://schema.org/OrderDelivered
    Model depth: 6
    """

    type_: str = Field("OrderDelivered", const=True, alias="@type")


if TYPE_CHECKING:

    OrderDelivered.update_forward_refs()
