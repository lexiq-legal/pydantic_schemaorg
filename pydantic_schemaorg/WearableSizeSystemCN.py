from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemCN(WearableSizeSystemEnumeration):
    """Chinese size system for wearables.

    See https://schema.org/WearableSizeSystemCN.

    """
    type_: str = Field("WearableSizeSystemCN", const=True, alias='@type')
    

WearableSizeSystemCN.update_forward_refs()
