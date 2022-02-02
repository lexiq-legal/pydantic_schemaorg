from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupBoys(WearableSizeGroupEnumeration):
    """Size group \"Boys\" for wearables.

    See: https://schema.org/WearableSizeGroupBoys
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupBoys", alias='@type')
    

