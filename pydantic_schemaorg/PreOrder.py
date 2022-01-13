from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class PreOrder(ItemAvailability):
    """Indicates that the item is available for pre-order.

    See: https://schema.org/PreOrder
    Model depth: 5
    """

    type_: str = Field("PreOrder", const=True, alias="@type")


if TYPE_CHECKING:

    PreOrder.update_forward_refs()
