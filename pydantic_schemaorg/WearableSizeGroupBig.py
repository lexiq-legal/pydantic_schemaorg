from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupBig(WearableSizeGroupEnumeration):
    """Size group \"Big\" for wearables.

    See: https://schema.org/WearableSizeGroupBig
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupBig", alias='@type')
    

