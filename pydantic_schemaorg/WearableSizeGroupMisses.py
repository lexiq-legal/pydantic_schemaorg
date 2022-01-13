from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMisses(WearableSizeGroupEnumeration):
    """Size group \"Misses\" (also known as \"Missy\") for wearables.

    See: https://schema.org/WearableSizeGroupMisses
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupMisses", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupMisses.update_forward_refs()
