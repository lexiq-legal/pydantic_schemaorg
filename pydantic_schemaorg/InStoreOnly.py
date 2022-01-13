from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class InStoreOnly(ItemAvailability):
    """Indicates that the item is available only at physical locations.

    See: https://schema.org/InStoreOnly
    Model depth: 5
    """

    type_: str = Field("InStoreOnly", const=True, alias="@type")


if TYPE_CHECKING:

    InStoreOnly.update_forward_refs()
