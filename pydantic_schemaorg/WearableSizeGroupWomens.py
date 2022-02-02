from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupWomens(WearableSizeGroupEnumeration):
    """Size group \"Womens\" for wearables.

    See: https://schema.org/WearableSizeGroupWomens
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupWomens", alias='@type')
    

