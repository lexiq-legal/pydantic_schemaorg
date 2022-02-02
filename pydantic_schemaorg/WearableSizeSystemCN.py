from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemCN(WearableSizeSystemEnumeration):
    """Chinese size system for wearables.

    See: https://schema.org/WearableSizeSystemCN
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemCN", alias='@type')
    

