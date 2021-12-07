from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemJP(WearableSizeSystemEnumeration):
    """Japanese size system for wearables.

    See https://schema.org/WearableSizeSystemJP.

    """
    type_: str = Field("WearableSizeSystemJP", const=True, alias='@type')
    

WearableSizeSystemJP.update_forward_refs()
