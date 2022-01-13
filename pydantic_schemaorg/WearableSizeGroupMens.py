from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMens(WearableSizeGroupEnumeration):
    """Size group \"Mens\" for wearables.

    See: https://schema.org/WearableSizeGroupMens
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupMens", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupMens.update_forward_refs()
