from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemIT(WearableSizeSystemEnumeration):
    """Italian size system for wearables.

    See: https://schema.org/WearableSizeSystemIT
    Model depth: 6
    """
    type_: str = Field("WearableSizeSystemIT", alias='@type')
    

