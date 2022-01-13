from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class LimitedAvailability(ItemAvailability):
    """Indicates that the item has limited availability.

    See: https://schema.org/LimitedAvailability
    Model depth: 5
    """

    type_: str = Field("LimitedAvailability", const=True, alias="@type")


if TYPE_CHECKING:

    LimitedAvailability.update_forward_refs()
