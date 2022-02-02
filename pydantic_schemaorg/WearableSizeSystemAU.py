from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemAU(WearableSizeSystemEnumeration):
    """Australian size system for wearables.

    See: https://schema.org/WearableSizeSystemAU
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemAU", alias='@type')
    

