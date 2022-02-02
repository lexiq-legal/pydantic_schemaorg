from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupPlus(WearableSizeGroupEnumeration):
    """Size group \"Plus\" for wearables.

    See: https://schema.org/WearableSizeGroupPlus
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupPlus", alias='@type')
    

