from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupExtraTall(WearableSizeGroupEnumeration):
    """Size group \"Extra Tall\" for wearables.

    See: https://schema.org/WearableSizeGroupExtraTall
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupExtraTall", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupExtraTall.update_forward_refs()
