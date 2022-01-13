from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderInTransit(OrderStatus):
    """OrderStatus representing that an order is in transit.

    See: https://schema.org/OrderInTransit
    Model depth: 6
    """

    type_: str = Field("OrderInTransit", const=True, alias="@type")


if TYPE_CHECKING:

    OrderInTransit.update_forward_refs()
