from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMaternity(WearableSizeGroupEnumeration):
    """Size group \"Maternity\" for wearables.

    See: https://schema.org/WearableSizeGroupMaternity
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupMaternity", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupMaternity.update_forward_refs()
