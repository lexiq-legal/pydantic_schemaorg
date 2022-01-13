from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupPetite(WearableSizeGroupEnumeration):
    """Size group \"Petite\" for wearables.

    See: https://schema.org/WearableSizeGroupPetite
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupPetite", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupPetite.update_forward_refs()
