from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemFR(WearableSizeSystemEnumeration):
    """French size system for wearables.

    See: https://schema.org/WearableSizeSystemFR
    Model depth: 6
    """

    type_: str = Field("WearableSizeSystemFR", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemFR.update_forward_refs()
