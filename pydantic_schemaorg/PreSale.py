from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class PreSale(ItemAvailability):
    """Indicates that the item is available for ordering and delivery before general availability.

    See: https://schema.org/PreSale
    Model depth: 5
    """

    type_: str = Field("PreSale", const=True, alias="@type")


if TYPE_CHECKING:

    PreSale.update_forward_refs()
