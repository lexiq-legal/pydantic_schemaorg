from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemFR(WearableSizeSystemEnumeration):
    """French size system for wearables.

    See https://schema.org/WearableSizeSystemFR.

    """
    type_: str = Field("WearableSizeSystemFR", const=True, alias='@type')
    

WearableSizeSystemFR.update_forward_refs()
