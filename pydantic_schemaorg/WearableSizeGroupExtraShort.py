from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupExtraShort(WearableSizeGroupEnumeration):
    """Size group \"Extra Short\" for wearables.

    See: https://schema.org/WearableSizeGroupExtraShort
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupExtraShort", alias='@type')
    

