from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.ItemAvailability import ItemAvailability


class OnlineOnly(ItemAvailability):
    """Indicates that the item is available only online.

    See: https://schema.org/OnlineOnly
    Model depth: 5
    """

    type_: str = Field("OnlineOnly", const=True, alias="@type")


if TYPE_CHECKING:

    OnlineOnly.update_forward_refs()
