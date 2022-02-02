from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemMX(WearableSizeSystemEnumeration):
    """Mexican size system for wearables.

    See: https://schema.org/WearableSizeSystemMX
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemMX", alias='@type')
    

