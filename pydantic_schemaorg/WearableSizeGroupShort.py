from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupShort(WearableSizeGroupEnumeration):
    """Size group \"Short\" for wearables.

    See: https://schema.org/WearableSizeGroupShort
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupShort", alias='@type')
    

