from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemGS1(WearableSizeSystemEnumeration):
    """GS1 (formerly NRF) size system for wearables.

    See: https://schema.org/WearableSizeSystemGS1
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemGS1", alias='@type')
    

