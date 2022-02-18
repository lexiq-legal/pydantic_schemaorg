from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupGirls(WearableSizeGroupEnumeration):
    """Size group \"Girls\" for wearables.

    See: https://schema.org/WearableSizeGroupGirls
    Model depth: 6
    """
    type_: str = Field(default="WearableSizeGroupGirls", alias='@type', const=True)
    
