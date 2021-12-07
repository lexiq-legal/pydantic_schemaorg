from pydantic import Field
from pydantic_schemaorg.WearableSizeGroupEnumeration import WearableSizeGroupEnumeration


class WearableSizeGroupShort(WearableSizeGroupEnumeration):
    """Size group \"Short\" for wearables.

    See https://schema.org/WearableSizeGroupShort.

    """
    type_: str = Field("WearableSizeGroupShort", const=True, alias='@type')
    

WearableSizeGroupShort.update_forward_refs()
