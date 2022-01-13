from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.OrderStatus import OrderStatus


class OrderProblem(OrderStatus):
    """OrderStatus representing that there is a problem with the order.

    See: https://schema.org/OrderProblem
    Model depth: 6
    """

    type_: str = Field("OrderProblem", const=True, alias="@type")


if TYPE_CHECKING:

    OrderProblem.update_forward_refs()
