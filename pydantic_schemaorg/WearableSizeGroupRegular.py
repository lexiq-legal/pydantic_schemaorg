from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupRegular(WearableSizeGroupEnumeration):
    """Size group \"Regular\" for wearables.

    See: https://schema.org/WearableSizeGroupRegular
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupRegular", alias='@type')
    

