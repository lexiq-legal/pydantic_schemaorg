from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemDE(WearableSizeSystemEnumeration):
    """German size system for wearables.

    See: https://schema.org/WearableSizeSystemDE
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemDE", alias='@type')
    

