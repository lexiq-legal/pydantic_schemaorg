from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupJuniors(WearableSizeGroupEnumeration):
    """Size group \"Juniors\" for wearables.

    See: https://schema.org/WearableSizeGroupJuniors
    Model depth: 6
    """

    type_: str = Field("WearableSizeGroupJuniors", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeGroupJuniors.update_forward_refs()
