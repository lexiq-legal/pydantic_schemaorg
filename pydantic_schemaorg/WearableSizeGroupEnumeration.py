from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.SizeGroupEnumeration import SizeGroupEnumeration


class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    """Enumerates common size groups (also known as \"size types\") for wearable products.

    See: https://schema.org/WearableSizeGroupEnumeration
    Model depth: 5
    """
    type_: str = Field("WearableSizeGroupEnumeration", alias='@type')
    

