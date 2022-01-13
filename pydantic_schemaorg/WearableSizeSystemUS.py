from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemUS(WearableSizeSystemEnumeration):
    """United States size system for wearables.

    See: https://schema.org/WearableSizeSystemUS
    Model depth: 6
    """

    type_: str = Field("WearableSizeSystemUS", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemUS.update_forward_refs()
