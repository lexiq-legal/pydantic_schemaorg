from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupBig(WearableSizeGroupEnumeration):
    """Size group \"Big\" for wearables.

    See: https://schema.org/WearableSizeGroupBig
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupBig", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupBig.update_forward_refs()
