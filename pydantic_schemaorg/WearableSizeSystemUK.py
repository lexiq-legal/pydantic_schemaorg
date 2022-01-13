from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from pydantic_schemaorg.WearableSizeSystemEnumeration import (
    WearableSizeSystemEnumeration,
)


class WearableSizeSystemUK(WearableSizeSystemEnumeration):
    """United Kingdom size system for wearables.

    See: https://schema.org/WearableSizeSystemUK
    Model depth: 6
    """

    type_: str = Field("WearableSizeSystemUK", const=True, alias="@type")


if TYPE_CHECKING:

    WearableSizeSystemUK.update_forward_refs()
