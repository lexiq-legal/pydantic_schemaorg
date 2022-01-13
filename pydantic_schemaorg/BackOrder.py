from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class BackOrder(ItemAvailability):
    """Indicates that the item is available on back order.

    See: https://schema.org/BackOrder
    Model depth: 5
    """

    type_: str = Field("BackOrder", const=True, alias="@type")


if TYPE_CHECKING:

    BackOrder.update_forward_refs()
