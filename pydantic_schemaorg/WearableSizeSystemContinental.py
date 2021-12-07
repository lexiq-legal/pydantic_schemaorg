from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemContinental(WearableSizeSystemEnumeration):
    """Continental size system for wearables.

    See https://schema.org/WearableSizeSystemContinental.

    """
    type_: str = Field("WearableSizeSystemContinental", const=True, alias='@type')
    

WearableSizeSystemContinental.update_forward_refs()
