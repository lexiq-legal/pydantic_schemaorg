from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemUS(WearableSizeSystemEnumeration):
    """United States size system for wearables.

    See https://schema.org/WearableSizeSystemUS.

    """
    type_: str = Field("WearableSizeSystemUS", const=True, alias='@type')
    

WearableSizeSystemUS.update_forward_refs()
