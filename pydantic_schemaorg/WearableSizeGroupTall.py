from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupTall(WearableSizeGroupEnumeration):
    """Size group \"Tall\" for wearables.

    See: https://schema.org/WearableSizeGroupTall
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupTall", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupTall.update_forward_refs()
