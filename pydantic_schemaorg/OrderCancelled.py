from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderCancelled(OrderStatus):
    """OrderStatus representing cancellation of an order.

    See: https://schema.org/OrderCancelled
    Model depth: 6
    """

    type_: str = Field("OrderCancelled", const=True, alias="@type")


if TYPE_CHECKING:

    OrderCancelled.update_forward_refs()
