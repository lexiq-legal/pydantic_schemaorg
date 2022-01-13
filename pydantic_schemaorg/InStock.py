from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class InStock(ItemAvailability):
    """Indicates that the item is in stock.

    See: https://schema.org/InStock
    Model depth: 5
    """

    type_: str = Field("InStock", const=True, alias="@type")


if TYPE_CHECKING:

    InStock.update_forward_refs()
