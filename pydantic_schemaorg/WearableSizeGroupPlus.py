from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupPlus(WearableSizeGroupEnumeration):
    """Size group \"Plus\" for wearables.

    See https://schema.org/WearableSizeGroupPlus.

    """
    type_: str = Field("WearableSizeGroupPlus", const=True, alias='@type')
    

WearableSizeGroupPlus.update_forward_refs()
