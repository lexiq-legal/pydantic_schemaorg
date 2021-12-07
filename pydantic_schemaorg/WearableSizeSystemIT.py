from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemIT(WearableSizeSystemEnumeration):
    """Italian size system for wearables.

    See https://schema.org/WearableSizeSystemIT.

    """
    type_: str = Field("WearableSizeSystemIT", const=True, alias='@type')
    

WearableSizeSystemIT.update_forward_refs()
