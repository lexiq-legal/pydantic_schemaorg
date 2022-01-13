from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """Enumerates common size systems specific for wearable products

    See: https://schema.org/WearableSizeSystemEnumeration
    Model depth: 5
    """

    type_: str = Field("WearableSizeSystemEnumeration", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemEnumeration.update_forward_refs()
