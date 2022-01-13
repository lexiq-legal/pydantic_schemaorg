from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemEurope(WearableSizeSystemEnumeration):
    """European size system for wearables.

    See: https://schema.org/WearableSizeSystemEurope
    Model depth: 6
    """

    type_: str = Field("WearableSizeSystemEurope", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemEurope.update_forward_refs()
