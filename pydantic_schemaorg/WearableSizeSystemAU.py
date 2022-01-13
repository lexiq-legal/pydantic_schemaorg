from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemAU(WearableSizeSystemEnumeration):
    """Australian size system for wearables.

    See: https://schema.org/WearableSizeSystemAU
    Model depth: 6
    """

    type_: str = Field("WearableSizeSystemAU", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemAU.update_forward_refs()
