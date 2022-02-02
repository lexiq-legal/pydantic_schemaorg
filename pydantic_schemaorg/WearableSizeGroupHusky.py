from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupHusky(WearableSizeGroupEnumeration):
    """Size group \"Husky\" (or \"Stocky\") for wearables.

    See: https://schema.org/WearableSizeGroupHusky
    Model depth: 6
    """
    type_: str = Field("WearableSizeGroupHusky", alias='@type')
    

