from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemMX(WearableSizeSystemEnumeration):
    """Mexican size system for wearables.

    See: https://schema.org/WearableSizeSystemMX
    Model depth: 6
    """

    type_: str = Field("WearableSizeSystemMX", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemMX.update_forward_refs()
