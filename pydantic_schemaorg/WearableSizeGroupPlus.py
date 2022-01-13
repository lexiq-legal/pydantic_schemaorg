from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupPlus(WearableSizeGroupEnumeration):
    """Size group \"Plus\" for wearables.

    See: https://schema.org/WearableSizeGroupPlus
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupPlus", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupPlus.update_forward_refs()
