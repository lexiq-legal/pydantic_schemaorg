from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemContinental(WearableSizeSystemEnumeration):
    """Continental size system for wearables.

    See: https://schema.org/WearableSizeSystemContinental
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemContinental", alias='@type')
    

