from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemJP(WearableSizeSystemEnumeration):
    """Japanese size system for wearables.

    See: https://schema.org/WearableSizeSystemJP
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemJP", alias='@type')
    

