from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OutOfStock(ItemAvailability):
    """Indicates that the item is out of stock.

    See: https://schema.org/OutOfStock
    Model depth: 5
    """

    type_: str = Field("OutOfStock", const=True, alias="@type")


if TYPE_CHECKING:

    OutOfStock.update_forward_refs()
