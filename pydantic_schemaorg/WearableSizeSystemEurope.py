from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemEurope(WearableSizeSystemEnumeration):
    """European size system for wearables.

    See: https://schema.org/WearableSizeSystemEurope
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemEurope", alias='@type')
    

