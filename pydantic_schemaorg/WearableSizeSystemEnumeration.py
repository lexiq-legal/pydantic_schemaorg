from pydantic import Field
from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    """Enumerates common size systems specific for wearable products

    See https://schema.org/WearableSizeSystemEnumeration.

    """
    type_: str = Field("WearableSizeSystemEnumeration", const=True, alias='@type')
    

WearableSizeSystemEnumeration.update_forward_refs()
