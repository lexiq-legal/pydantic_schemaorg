from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupGirls(WearableSizeGroupEnumeration):
    """Size group \"Girls\" for wearables.

    See: https://schema.org/WearableSizeGroupGirls
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupGirls", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupGirls.update_forward_refs()
