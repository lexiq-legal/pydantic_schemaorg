from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class SoldOut(ItemAvailability):
    """Indicates that the item has sold out.

    See: https://schema.org/SoldOut
    Model depth: 5
    """

    type_: str = Field("SoldOut", const=True, alias="@type")


if TYPE_CHECKING:

    SoldOut.update_forward_refs()
