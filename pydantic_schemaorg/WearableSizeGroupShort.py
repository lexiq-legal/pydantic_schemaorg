from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupShort(WearableSizeGroupEnumeration):
    """Size group \"Short\" for wearables.

    See: https://schema.org/WearableSizeGroupShort
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupShort", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupShort.update_forward_refs()
