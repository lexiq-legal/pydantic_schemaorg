from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupInfants(WearableSizeGroupEnumeration):
    """Size group \"Infants\" for wearables.

    See: https://schema.org/WearableSizeGroupInfants
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupInfants", alias='@type')
    

