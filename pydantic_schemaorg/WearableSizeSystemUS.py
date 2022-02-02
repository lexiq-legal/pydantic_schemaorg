from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemUS(WearableSizeSystemEnumeration):
    """United States size system for wearables.

    See: https://schema.org/WearableSizeSystemUS
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemUS", alias='@type')
    

