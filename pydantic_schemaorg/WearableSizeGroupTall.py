from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupTall(WearableSizeGroupEnumeration):
    """Size group \"Tall\" for wearables.

    See: https://schema.org/WearableSizeGroupTall
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupTall", alias='@type')
    

