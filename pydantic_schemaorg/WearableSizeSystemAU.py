from pydantic import Field
from pydantic_schemaorg.WearableSizeSystemEnumeration import WearableSizeSystemEnumeration


class WearableSizeSystemAU(WearableSizeSystemEnumeration):
    """Australian size system for wearables.

    See https://schema.org/WearableSizeSystemAU.

    """
    type_: str = Field("WearableSizeSystemAU", const=True, alias='@type')
    

WearableSizeSystemAU.update_forward_refs()
