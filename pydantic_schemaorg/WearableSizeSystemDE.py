from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemDE(WearableSizeSystemEnumeration):
    """German size system for wearables.

    See: https://schema.org/WearableSizeSystemDE
    Model depth: 6
    """

    type_: str = Field("WearableSizeSystemDE", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemDE.update_forward_refs()
