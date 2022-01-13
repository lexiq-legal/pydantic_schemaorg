from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupInfants(WearableSizeGroupEnumeration):
    """Size group \"Infants\" for wearables.

    See: https://schema.org/WearableSizeGroupInfants
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupInfants", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupInfants.update_forward_refs()
