from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemFR(WearableSizeSystemEnumeration):
    """French size system for wearables.

    See: https://schema.org/WearableSizeSystemFR
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemFR", alias='@type')
    

