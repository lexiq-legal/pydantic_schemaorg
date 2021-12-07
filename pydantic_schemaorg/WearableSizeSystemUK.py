from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemUK(WearableSizeSystemEnumeration):
    """United Kingdom size system for wearables.

    See https://schema.org/WearableSizeSystemUK.

    """
    type_: str = Field("WearableSizeSystemUK", const=True, alias='@type')
    

WearableSizeSystemUK.update_forward_refs()
