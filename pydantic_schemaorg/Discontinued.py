from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class Discontinued(ItemAvailability):
    """Indicates that the item has been discontinued.

    See: https://schema.org/Discontinued
    Model depth: 5
    """

    type_: str = Field("Discontinued", const=True, alias="@type")


if TYPE_CHECKING:

    Discontinued.update_forward_refs()
