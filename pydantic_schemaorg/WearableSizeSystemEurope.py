from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemEurope(WearableSizeSystemEnumeration):
    """European size system for wearables.

    See https://schema.org/WearableSizeSystemEurope.

    """
    type_: str = Field("WearableSizeSystemEurope", const=True, alias='@type')
    

WearableSizeSystemEurope.update_forward_refs()
