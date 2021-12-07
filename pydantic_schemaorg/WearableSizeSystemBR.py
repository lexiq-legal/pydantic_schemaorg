from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemBR(WearableSizeSystemEnumeration):
    """Brazilian size system for wearables.

    See https://schema.org/WearableSizeSystemBR.

    """
    type_: str = Field("WearableSizeSystemBR", const=True, alias='@type')
    

WearableSizeSystemBR.update_forward_refs()
