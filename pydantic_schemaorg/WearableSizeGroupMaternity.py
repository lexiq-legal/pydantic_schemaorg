from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupMaternity(WearableSizeGroupEnumeration):
    """Size group \"Maternity\" for wearables.

    See: https://schema.org/WearableSizeGroupMaternity
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupMaternity", alias='@type')
    

