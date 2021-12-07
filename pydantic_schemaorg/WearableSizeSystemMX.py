from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemMX(WearableSizeSystemEnumeration):
    """Mexican size system for wearables.

    See https://schema.org/WearableSizeSystemMX.

    """
    type_: str = Field("WearableSizeSystemMX", const=True, alias='@type')
    

WearableSizeSystemMX.update_forward_refs()
