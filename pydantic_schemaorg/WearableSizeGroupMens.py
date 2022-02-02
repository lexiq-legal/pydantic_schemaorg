from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMens(WearableSizeGroupEnumeration):
    """Size group \"Mens\" for wearables.

    See: https://schema.org/WearableSizeGroupMens
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupMens", alias='@type')
    

