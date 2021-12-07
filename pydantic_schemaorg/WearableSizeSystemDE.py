from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemDE(WearableSizeSystemEnumeration):
    """German size system for wearables.

    See https://schema.org/WearableSizeSystemDE.

    """
    type_: str = Field("WearableSizeSystemDE", const=True, alias='@type')
    

WearableSizeSystemDE.update_forward_refs()
