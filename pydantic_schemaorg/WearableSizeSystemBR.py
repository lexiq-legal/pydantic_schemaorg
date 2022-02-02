from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemBR(WearableSizeSystemEnumeration):
    """Brazilian size system for wearables.

    See: https://schema.org/WearableSizeSystemBR
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemBR", alias='@type')
    

